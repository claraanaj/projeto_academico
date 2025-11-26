from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome} - {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome completo")
    nome_do_pai = models.CharField(max_length=150, verbose_name="Nome do pai", blank=True)
    nome_da_mae = models.CharField(max_length=150, verbose_name="Nome da mãe", blank=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="E-mail")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da instituição")
    site = models.URLField(verbose_name="Site", blank=True)
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


class Turno(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class Curso(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração em meses")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Disciplina(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class DisciplinaPorCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")
    carga_horaria = models.IntegerField(verbose_name="Carga horária")

    def __str__(self):
        return f"{self.disciplina.nome} - {self.curso.nome}"

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Curso"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data de previsão de término")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.curso.nome}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota")
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE, verbose_name="Tipo de avaliação")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno", null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas", default=0)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome} - {self.numero_faltas} faltas"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"