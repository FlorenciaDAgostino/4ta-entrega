from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"    

class Televisores(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha_publicación = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
    
class Celulares (models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
    
class Heladeras (models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
    
class Lavarropas (models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'