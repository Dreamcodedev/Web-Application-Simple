#-*- coding: utf-8 -*-
"""E_SCHOOL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.urls import path
from etablissement.views import connexion,inscription,EmploiTemps, Resultat,deconnexion, Whatsapp,Matiere
from etablissement.views import Eleve,Classe, Etablissement, Professeur, Comptabilite, Foyer, Time_Table, ResultatAdmin

urlpatterns = [
    path('login/', connexion,name='login'),
    #path('home/', home,name='home'),
    path('admin/inscription/', inscription,name='inscription'),
    path('emploi_temps/', EmploiTemps,name='emploi_temps'),
    path('resultat/', Resultat,name='resultat'),
    path('logout/', deconnexion,name='logout'),
    path('admin/Whatsapp/', Whatsapp,name='whatsapp'),
    path('admin/Matiere/', Matiere,name='matiere'),
    path('admin/Eleve/', Eleve,name='eleve'),
    path('admin/Classe/', Classe,name='classe'),
    path('admin/Etablissement/', Etablissement,name='etablissement'),
    path('admin/Professeur/', Professeur,name='professeur'),
    path('admin/Comptabilite/', Comptabilite,name='comptabilite'),
    path('admin/Foyer/', Foyer,name='foyer'),
    path('admin/EmploiTemps/', Time_Table,name='emploitempsadmin'),
    path('admin/Resultat/', ResultatAdmin,name='resultatadmin'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
