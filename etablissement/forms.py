from django import forms
from etablissement.models import Inscription, Eleve, Matiere, Classe,Etablissement, Professeur, Comptabilite, Foyer
from etablissement.models import Emploi_Temps, Resultat


class InscriptionForm(forms.ModelForm):
	class Meta:
		model = Inscription
		fields = '__all__'

class EleveForm(forms.ModelForm):
	class Meta:
		model = Eleve
		fields = '__all__'

class MatiereForm(forms.ModelForm):
	class Meta:
		model = Matiere
		fields = '__all__'


class ClassForm(forms.ModelForm):
	class Meta:
		model = Classe
		fields = '__all__'

class EtablissementForm(forms.ModelForm):
	class Meta:
		model = Etablissement
		fields = '__all__'

class ProfesseurForm(forms.ModelForm):
	class Meta:
		model = Professeur
		fields = '__all__'

class ComptabiliteForm(forms.ModelForm):
	class Meta:
		model = Comptabilite
		fields = '__all__'

class FoyerForm(forms.ModelForm):
	class Meta:
		model = Foyer
		fields = '__all__'

class EmploiTempsForm(forms.ModelForm):
	class Meta:
		model = Emploi_Temps
		fields = '__all__'

class ResultatForm(forms.ModelForm):
	class Meta:
		model = Resultat
		fields = '__all__'


class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur",max_length=30)
	password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)