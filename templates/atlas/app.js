/*eslint-globals L*/

(function () {

    'use strict';

    var regionsGeoJson;
    var regionsShapes;

    var map, popupTpl, regionsListContainer, regionListItemTpl;

    function renderMarkers(data) {

        var markerClusters = new L.MarkerClusterGroup({
            showCoverageOnHover: false,
            maxClusterRadius: 40,
            spiderfyDistanceMultiplier: 2
        });

        _.each(data.data, function (markerData) {

            // lon,lat on test data :(
            var rawCoordinates = markerData.coordinates.split(',');
            var coordinates = [ parseFloat(rawCoordinates[1]), parseFloat(rawCoordinates[0]) ];

            var marker = new L.Marker(coordinates);
            markerClusters.addLayer(marker);

            marker.data = markerData;
            marker.on('click', onMarkerClick);

        });

        map.addLayer(markerClusters);
    }

    function onMarkerClick(e) {
        var marker = e.target;
        var popupData = marker.data;

        //wrap data in an object to avoid ref errors when rendering template
        var popup = L.popup().setContent( popupTpl( {data: popupData }) );
        marker.bindPopup( popup );
        marker.openPopup();
    }

    function initRegionsListEvents() {
        regionsListContainer.find('a').each(function() {
            // console.log(arguments)
        });
        regionsListContainer.find('a').on('click', function (e) {
            var latlonStr = $(e.currentTarget).data('latlon');
            var latlon = latlonStr.split(',');

            //shift a bit to the west to compensate space taken by right controls
            //TODO : only desktop
            latlon[1] = parseFloat(latlon[1]) + 1;
            map.setView(latlon, 8);

            if (regionsShapes) {
                map.removeLayer(regionsShapes);
            }

            regionsShapes = L.geoJson(regionsGeoJson, {
                filter: function(feature) {
                    return feature.properties.NAME_2 === $(this).html();
                }.bind(this)
            }).addTo(map);
        });
    }


    function updateFilters() {
        function updateCheckboxList(name) {
            var values = _.map( $('#' + name + ' input'), function(el) {return el.checked; });
            $('[data-countof=' + name + ']').text( _.contains(values, false) ? _.compact(values).length + '/' + values.length : 'toutes' );
        }
        updateCheckboxList('actionType');
        updateCheckboxList('population');

    }

    function init() {
        L.Icon.Default.imagePath = './images/leaflet';

        map = L.map('map', {
            center: [-18.766947, 49],
            zoom: 6,
            minZoom: 4,
            maxZoom: 10
        });

        L.tileLayer('http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png').addTo(map);

        $.ajax('./testData.json').done( renderMarkers );

        popupTpl = _.template( $('.js-tpl-popup').html() );

        regionsListContainer = $('.js-regions');
        regionListItemTpl = _.template('<li><a href="#" data-latlon="<%= center %>"><%= name %></a></li>');


        updateFilters();


        //move that to a sass loop later :)
        _.each($('#actionType .checkboxList input'), function(el, index) {
            $('<span class="icon"></span>').insertBefore(el).css('background-position', '-' + index * 30 + 'px' + ' 0');
        });

        _.each($('#population .checkboxList input'), function(el, index) {
            $('<span class="icon"></span>').insertBefore(el).css('background-position', '-' + index * 30 + 'px' + ' 0');
        });


        $('.js-showfilters').on('click', function () {
            $('.js-filters').addClass('opened');
        });

        $('.js-closeFilters').on('click', function() {
            $('.js-filters').removeClass('opened');
        });

        $('.js-filterFieldList input').on('change', function () {
            updateFilters();
        });

        $.getJSON( 'geo/faritra.json', function(geojson) {
            regionsGeoJson = geojson;
            regionsShapes = L.geoJson(geojson, {
                onEachFeature: function(feature, layer) {
                    var center = layer.getBounds().getCenter();
                    var regionListItem = regionListItemTpl({
                        name: feature.properties.NAME_2,
                        center: center.lat + ',' + center.lng
                    });
                    $(regionListItem).appendTo(regionsListContainer);
                    // console.log(feature)
                }
            });

            initRegionsListEvents();
        } );
    }

    init();

})();
