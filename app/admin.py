from django.contrib import admin
from .models import *


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1
    fk_name = 'ocupacao'


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1


class DisciplinaPorCursoInline(admin.TabularInline):
    model = DisciplinaPorCurso
    extra = 1


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [PessoaInline]


@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'cidade']
    search_fields = ['nome', 'email']
    list_filter = ['cidade']
    inlines = [CursoInline]


@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [CursoInline]


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'carga_horaria_total', 'duracao_meses', 'area_saber', 'instituicao']
    search_fields = ['nome']
    list_filter = ['area_saber', 'instituicao']
    inlines = [DisciplinaPorCursoInline]


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'area_saber']
    search_fields = ['nome']
    list_filter = ['area_saber']
    inlines = [AvaliacaoInline]


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'turno', 'curso']
    search_fields = ['nome']
    list_filter = ['turno', 'curso']


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'data_nasc', 'cidade', 'ocupacao']
    search_fields = ['nome', 'cpf', 'email']
    list_filter = ['cidade', 'ocupacao']


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    search_fields = ['nome', 'uf']
    list_filter = ['uf']


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(DisciplinaPorCurso)
class DisciplinaPorCursoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'disciplina', 'turno', 'carga_horaria']
    search_fields = ['curso__nome', 'disciplina__nome']
    list_filter = ['curso', 'turno']


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicao', 'data_inicio', 'data_previsao_termino']
    search_fields = ['pessoa__nome', 'curso__nome']
    list_filter = ['curso', 'instituicao']


@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'pessoa', 'disciplina', 'curso', 'nota', 'tipo_avaliacao']
    search_fields = ['descricao', 'pessoa__nome', 'disciplina__nome']
    list_filter = ['curso', 'disciplina', 'tipo_avaliacao']


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'disciplina', 'curso', 'numero_faltas']
    search_fields = ['pessoa__nome', 'disciplina__nome']
    list_filter = ['curso', 'disciplina']


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'disciplina', 'curso', 'data']
    search_fields = ['pessoa__nome', 'descricao']
    list_filter = ['curso', 'disciplina', 'data']