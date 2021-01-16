from django.db import models

# Create your models here.

class towels(models.Model):

    Name = models.CharField(max_length=70)
    Size2448 = models.BooleanField(default=False, blank=True, null=True)
    Size2754 = models.BooleanField(default=False, blank=True, null=True)
    Size3060 = models.BooleanField(default=False, blank=True, null=True)
    Prize = models.IntegerField(blank = True,null = True)
    Image = models.ImageField(upload_to='pics',blank = True,null = True)
    MinimumQt = models.CharField(max_length=50, blank=True, null=True)

    greenbool = models.BooleanField(default=False)
    greenbool1 = models.ImageField(upload_to='pics',blank = True,null = True)
    greenbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    yellowbool = models.BooleanField(default=False)
    yellowbool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    yellowbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    pinkbool = models.BooleanField(default=False)
    pinkbool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    pinkbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    redbool = models.BooleanField(default=False)
    redbool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    redbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    saffbool = models.BooleanField(default=False)
    saffbool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    saffbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    bluebool = models.BooleanField(default=False)
    bluebool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    bluebool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    purplebool = models.BooleanField(default=False)
    purplebool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    purplebool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    mintbool = models.BooleanField(default=False)
    mintbool1 = models.ImageField(upload_to='pics', blank=True, null=True)
    mintbool2 = models.ImageField(upload_to='pics', blank=True, null=True)

    browmbool = models.BooleanField(default=False)
    brownbool1 = models.ImageField(upload_to='pics',blank = True,null=True)
    brownbool2 = models.ImageField(upload_to='pics',blank = True,null=True)

    combobool = models.BooleanField(default=False, blank=True, null=True)
    combobool1 = models.ImageField(upload_to='pics', blank=True, null=True)

    Stock = models.BooleanField(default=False)
    Material = models.CharField(max_length=30, blank=True, null=True)

    tickforembroideryboolt = models.BooleanField(default=False)
    tickforsmoothboolt = models.BooleanField(default=False)
    tickforbathboolt = models.BooleanField(default=False)
    tickforfilamentboolt = models.BooleanField(default=False)



class napkinss(models.Model):

    Nname = models.CharField(max_length=70)
    Size1421 = models.BooleanField(default=False, blank=True, null=True)
    Size1218 = models.BooleanField(default=False, blank=True, null=True)

    Prizen = models.IntegerField(blank = True,null = True)
    Imagen = models.ImageField(upload_to='pics',blank = True,null = True)
    MinimumQn = models.CharField(max_length=50, blank=True, null=True)

    greenbooln = models.BooleanField(default=False)
    greenbooln1 = models.ImageField(upload_to='pics',blank = True,null = True)
    greenbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    yellowbooln = models.BooleanField(default=False)
    yellowbooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    yellowbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    pinkbooln = models.BooleanField(default=False)
    pinkbooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    pinkbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    redbooln = models.BooleanField(default=False)
    redbooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    redbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    saffbooln = models.BooleanField(default=False)
    saffbooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    saffbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    bluebooln = models.BooleanField(default=False)
    bluebooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    bluebooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    purplebooln = models.BooleanField(default=False)
    purplebooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    purplebooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    mintbooln = models.BooleanField(default=False)
    mintbooln1 = models.ImageField(upload_to='pics', blank=True, null=True)
    mintbooln2 = models.ImageField(upload_to='pics', blank=True, null=True)

    browmbooln = models.BooleanField(default=False)
    brownbooln1 = models.ImageField(upload_to='pics',blank = True,null=True)
    brownbooln2 = models.ImageField(upload_to='pics',blank = True,null=True)

    combobooln = models.BooleanField(default=False, blank=True, null=True)
    combobooln1 = models.ImageField(upload_to='pics', blank=True, null=True)

    Stockn = models.BooleanField(default=False)
    Materialn = models.CharField(max_length=30, blank=True, null=True)

    tickforembroiderybooln = models.BooleanField(default=False)
    tickforsmoothbooln = models.BooleanField(default=False)
    tickforbathbooln = models.BooleanField(default=False)
    tickforfilamentbooln = models.BooleanField(default=False)

