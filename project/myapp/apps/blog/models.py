from django.db import models
from ckeditor.fields import RichTextField

# Por ahora Ligue no es de interez


class Ligue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la liga',
                            max_length=50,
                            null=False,
                            blank=False)
    state = models.BooleanField('Liga activada / desactivada', default=True)

    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'

    def __str__(self):
        return self.name


# fin Ligue


class Discipline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la disciplina',
                            max_length=50,
                            null=False,
                            blank=False)
    state = models.BooleanField('Disciplina activada / desactivada',
                                default=True)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de categoria',
                            max_length=100,
                            null=False,
                            blank=False)
    state = models.BooleanField('Categoria activada / desactivada',
                                default=True)
    Discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    creationDate = models.DateField('Fecha de creación',
                                    auto_now=False,
                                    auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categrias'

    def __str__(self):
        return self.name


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=50, null=False, blank=False)
    lastName = models.CharField('Apellido',
                                max_length=50,
                                null=False,
                                blank=False)
    facebook = models.CharField('Facebook',
                                max_length=50,
                                blank=True,
                                null=True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null=True)
    instagram = models.CharField('Instagram',
                                 max_length=50,
                                 blank=True,
                                 null=True)
    email = models.CharField('Correo', max_length=50, blank=True, null=True)
    state = models.BooleanField('Autor activo / No activo', default=True)
    creationDate = models.DateField('Fecha de creaciÃ³n',
                                    auto_now=False,
                                    auto_now_add=True)
    time = models.TimeField('Hora de publicación',
                            blank=False,
                            null=False,
                            auto_now=False,
                            auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0} {1}'.format(self.name, self.lastName)


class Contry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Pais', max_length=50, null=False, blank=False)

    class META:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=80, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    description = models.CharField('Descripción',
                                   max_length=100,
                                   null=False,
                                   blank=False)
    content = RichTextField()
    image = models.URLField('Imagen URL',
                            max_length=255,
                            null=False,
                            blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    outstandingType1 = models.BooleanField('Destacado tipo 1  SI/ NO',
                                           default=False)
    outstandingType2 = models.BooleanField('Destacado tipo 2  SI/ NO',
                                           default=False)
    state = models.BooleanField('Publicado / No publicado', default=False)
    creationDate = models.DateField('Fecha de creación',
                                    auto_now=False,
                                    auto_now_add=True)
    time = models.TimeField('Hora de publicación',
                            blank=False,
                            null=False,
                            auto_now=False,
                            auto_now_add=True)

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-creationDate']

    def __str__(self):
        return self.title


class Stadium(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=False, blank=False)
    city = models.CharField('Ciudad', max_length=100, null=True, blank=False)
    Contry = models.ForeignKey(Contry,
                               related_name='EstadiumContry',
                               on_delete=models.CASCADE,
                               null=True)

    class Meta:
        verbose_name = 'Estadio'
        verbose_name_plural = 'Estadios'

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category,
                                 related_name='Categoria',
                                 on_delete=models.CASCADE,
                                 null=True)
    Contry = models.ForeignKey(Contry,
                               related_name='TeamContry',
                               on_delete=models.CASCADE,
                               null=True)
    logo = models.ImageField(upload_to='logo/',
                             verbose_name='Logo',
                             name='teamLogo')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return '{}-{}: {}'.format(self.Contry, self.category, self.name)

    def contry(self):
        return self.Contry


class BlackboardResults(models.Model):
    id = models.AutoField(primary_key=True)
    winnerTeam = models.ForeignKey(Team,
                                   verbose_name='Equipo ganador',
                                   related_name='Ganador',
                                   on_delete=models.CASCADE,
                                   null=True)
    runsScoredWinner = models.IntegerField('Carreras', null=False, blank=False)
    loserTeam = models.ForeignKey(Team,
                                  verbose_name='Visitante',
                                  related_name='Visitante',
                                  on_delete=models.CASCADE,
                                  null=True)
    runsScoredLoser = models.IntegerField('Carreras', null=False, blank=False)
    date = models.DateField('Fecha de juego',
                            auto_now=False,
                            auto_now_add=False)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    state = models.BooleanField('Publicar SI/NO', default=False)

    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'
        ordering = ['-date']

    def __str__(self):
        return '{} vs {}'.format(self.winnerTeam, self.loserTeam)
