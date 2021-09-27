from django.db import models

class Contry(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Pais', max_length = 50, null = False, blank= False)
    class META:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    def __str__(self):
        return self.name

class State(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Estado', max_length = 50, null = False, blank= False)
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE)
    class META:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    def __str__(self):
        return '{0} {1}'.format(self.name, self.contry)

class Ligue(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de la liga', max_length = 50, null = False, blank= False)
    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'
    def __str__(self):
        return self.name


class Category (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de categoria', max_length = 100, null = False, blank= False)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categrias'
    def __str__(self):
        return self.name


class School (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length = 100, null =False, blank = False)
    logo = models.ImageField(upload_to='logo')
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    phoneNumber1 = models.CharField('Telefono primario', max_length=20, blank=True, null= True)
    phoneNumber2 = models.CharField('Telefono alterno', max_length=20, blank=True, null= True)
    state = models.BooleanField('Escuela activa  SI/NO', default = True)


class Team (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length = 100, null =False, blank = False)
    logo = models.ImageField(upload_to='logo')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    state = models.BooleanField('Equipo activo SI/NO', default = True)
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    phoneNumber1 = models.CharField('Telefono primario', max_length=20, blank=True, null= True)
    phoneNumber2 = models.CharField('Telefono alterno', max_length=20, blank=True, null= True)

class PositionPlay (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Posición', max_length = 50, null =False, blank = False)
    shorten = models.CharField('Abreviatura', max_length = 2, null =False, blank = False)

class Player (models.Model):
    id = models.AutoField(primary_key = True)
    numberID = models.CharField('Cédula', max_length = 8, null =True, blank = True)
    photoPlayer = models.ImageField(upload_to='photoPlayer')
    name = models.CharField('Nombre', max_length = 50, null =False, blank = False)
    lastName = models.CharField('Apellido', max_length = 50, null=False, blank=False)
    # sudo, derecho, ambidiestro, posición etc, (hablar con enger), averaje
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    position = models.ForeignKey(PositionPlay, on_delete=models.CASCADE)
    numberPlayer = models.CharField('Número de camiseta', max_length = 2, null =False, blank = False)
    rigth = models.BooleanField('Derecho SI/NO', default = False)
    left = models.BooleanField('Surdo SI/NO', default = False)
    rigthAndLeft = models.BooleanField('Ambidiestro SI/NO', default = False)
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    state = models.BooleanField('Jugador activo SI/NO', default = True)
    dateOfBirth = models.DateField('Fecha de nacimiento', auto_now = False, auto_now_add = False)

