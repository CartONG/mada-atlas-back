# Register your models here.
from django.contrib import admin
#from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from models import organisme, utilisateur, action, categorie, avancement, status

class ActionAdmin(admin.ModelAdmin):
    fields = ['categories', 'titre', 'date', 'duree', 'description', 'localisation', 'illustration',  'responsable', 'avancement', 'organisme']
    list_display = ('get_categories', 'titre', 'organisme', 'date', 'duree', 'description', 'localisation', 'illustration', 'responsable', 'avancement', 'creation', 'maj')
    def get_categories(self, obj):
        return "\n".join([c.nom for c in obj.categories.all()])
    list_editable = ('titre', 'date', 'duree', 'description', 'localisation', 'illustration', 'responsable', 'avancement')  #  Any field in list_editable must also be in list_display. You can't edit a field that's not displayed!
    list_filter = ('categories', 'organisme', 'localisation', 'avancement')
    search_fields = ['titre', 'description','get_categories']
    readonly_fields = ('creation', 'maj')
    #list_display_links = ('region', 'categories')  # The same field can't be listed in both list_editable and list_display_links -- a field can't be both a form and a link.


#admin.site.register(mdgRegion, admin.OSMGeoAdmin)
#admin.site.register(mdgRegion, LeafletGeoAdmin)
admin.site.register(organisme)
admin.site.register(utilisateur)
#admin.site.register(action, ActionAdmin)
admin.site.register(action, LeafletGeoAdmin)
admin.site.register(categorie)
admin.site.register(avancement)
admin.site.register(status)

