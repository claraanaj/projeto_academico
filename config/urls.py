from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('areas-saber/', AreasSaberView.as_view(), name='areas_saber'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('disciplinas-curso/', DisciplinasPorCursoView.as_view(), name='disciplinas_curso'),
    path('tipos-avaliacao/', TiposAvaliacaoView.as_view(), name='tipos_avaliacao'),
]