from django.db import models

# Create your models here.
class about(models.Model):
    name = models.CharField(max_length=50)
    aboutus = models.TextField()
    adress = models.TextField(max_length=500)
    email = models.EmailField()
    addressF = models.CharField(max_length=500)
    addressI = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Branches(models.Model):
    name = models.CharField(max_length=50)
    aboutus = models.TextField()
    address = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='media/photos/branches')
    more_photo1 = models.ImageField(upload_to='media/photos/branches')
    more_photo2 = models.ImageField(upload_to='media/photos/branches')  
    more_photo3 = models.ImageField(upload_to='media/photos/branches')
    more_photo4 = models.ImageField(upload_to='media/photos/branches')
    more_photo5 = models.ImageField(upload_to='media/photos/branches')

    def __str__(self):
        return self.name
    
class Meno_starter(models.Model):
    branche = models.ForeignKey(Branches, on_delete=models.CASCADE)
    starter = models.CharField(max_length=50)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='media/photos/meno') 

    def __str__(self):
        return self.branche

class Meno_dish(models.Model):
    branche = models.ForeignKey(Branches, on_delete=models.CASCADE)
    dish = models.CharField(max_length=50)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='media/photos/meno/dish') 

    def __str__(self):
        return self.branche
    
class Meno_desert(models.Model):
    branche = models.ForeignKey(Branches, on_delete=models.CASCADE)
    desert = models.CharField(max_length=50)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='media/photos/meno/desert') 

    def __str__(self):
        return self.branche
    

class Meno_dreink(models.Model):
    branche = models.ForeignKey(Branches, on_delete=models.CASCADE)
    dreink = models.CharField(max_length=50)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='media/photos/meno/dreink') 

    def __str__(self):
        return self.branche


MENO = [
    ('starter','Starter'),
    ('dish','Dish'),
    ('desert','Desert'),
    ('dreink','Dreink')
]
class Pricing_off(models.Model):
    prise_off = models.IntegerField()
    location = models.ForeignKey(Branches, on_delete=models.CASCADE)
    meno = models.CharField(max_length=50, choices=MENO)

    def __str__(self):
        return self.location
    

    