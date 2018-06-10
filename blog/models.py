from django.db import models

# Create your models here.
'''
title
pub_day
body
image

'''

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


#add model to settings

# create a migragation

# migrate a model

# add to admin
