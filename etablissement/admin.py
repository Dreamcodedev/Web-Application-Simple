from django.contrib import admin

# Register your models here.
from etablissement.models import Inscription, Etablissement, Classe
class InscriptionAdmin(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'NNI','etablissement','classe',)
	list_filter = ('etablissement','classe',)
	#date_hierarchy = 'date'
	#ordering = ('date', )
	search_fields = ('nom', 'NNI')
class ClassAdmin(admin.ModelAdmin):
	list_display = ('nom_classe','categorie')
	search_fields = ('categorie','categorie')

class EtablissementAdmin(admin.ModelAdmin):
	list_display = ('nom_etablissement','nom_etablissement')
	search_fields = ('nom_etablissement','nom_etablissement')



admin.site.register(Inscription,InscriptionAdmin)
admin.site.register(Etablissement,EtablissementAdmin)
admin.site.register(Classe,ClassAdmin)
