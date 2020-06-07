from django.db import models

# Create your models here.
class Brend(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Audio(models.Model):
    #Headphone
    objects = models.Manager()
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)
    frequency_headphone = models.CharField(max_length = 30)
    impedance = models.CharField(max_length=10)
    driver = models.CharField(max_length = 50)
    #Microphone
    frequency_microphone = models.CharField(max_length=30)
    sensitivity = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Keyboard(models.Model):
    objects = models.Manager()
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    key_switch = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    light_effects = models.CharField(max_length=200)
    lifespan = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Mice(models.Model):
    objects = models.Manager()
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    sensor = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    dpi = models.CharField("DPI presets",max_length=50)
    speed = models.CharField(max_length = 50)
    switch = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name