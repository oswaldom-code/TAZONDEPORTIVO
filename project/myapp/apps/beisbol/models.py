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
    class META:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    def __str__(self):
        return self.name

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
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    phoneNumber1 = models.CharField('Telefono primario', max_length=20, blank=True, null= True)
    phoneNumber2 = models.CharField('Telefono alterno', max_length=20, blank=True, null= True)
    state = models.BooleanField('Escuela activa  SI/NO', default = True)


class Tem (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length = 100, null =False, blank = False)
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    phoneNumber1 = models.CharField('Telefono primario', max_length=20, blank=True, null= True)
    phoneNumber2 = models.CharField('Telefono alterno', max_length=20, blank=True, null= True)
    state = models.BooleanField('Equipo activo SI/NO', default = True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE)


class Player (models.Model):
    id = models.AutoField(primary_key = True)
    numberID = models.CharField('Cédula', max_length = 8, null =True, blank = True)
    name = models.CharField('Nombre', max_length = 50, null =False, blank = False)
    lastName = models.CharField('Apellido', max_length = 50, null=False, blank=False)
    # Foto, sudo, derecho, ambidiestro, posición etc, (hablar con enger), averaje
    numberPlayer = models.CharField('Número de camiseta', max_length = 2, null =False, blank = False)
    facebook = models.CharField('Facebook', max_length=50, blank=True, null= True)
    twitter = models.CharField('Twitter', max_length=50, blank=True, null= True)
    instagram = models.CharField('Instagram', max_length=50, blank=True, null= True)
    email = models.CharField('Correo', max_length=50, blank=True, null= True)
    state = models.BooleanField('Jugador activo SI/NO', default = True)
    dateOfBirth = models.DateField('Fecha de nacimiento', auto_now = False, auto_now_add = False)
    tem = models.ForeignKey('Tem', on_delete=models.CASCADE)
