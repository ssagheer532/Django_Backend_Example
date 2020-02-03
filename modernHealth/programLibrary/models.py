from django.db import models
import uuid
from django.db import models

activityTypes = (('html', 'HTML'),('mcq', 'MCQ'))


class HTML(models.Model):
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4(), primary_key=True)
    # Use this website to encode/decode: https://www.base64encode.org/
    encodedContent = models.CharField(max_length=1000, default='None')


class MCQ(models.Model):
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4(), primary_key=True)
    question = models.CharField(max_length=500, default='None')
    optionOne = models.CharField(max_length=500, default='None')
    optionTwo = models.CharField(max_length=500, default='None')
    optionThree = models.CharField(max_length=500, default='None')
    optionFour = models.CharField(max_length=500, default='None')
    optionFive = models.CharField(max_length=500, default='None')


class Section(models.Model):
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # save image on s3 and store the s3 path here
    overviewImage = models.CharField(max_length=500)
    orderIndex = models.IntegerField(unique=True)
    activityType = models.CharField(choices=activityTypes, default='HTML', max_length=500)
    mcq = models.ManyToManyField(MCQ)
    html = models.ManyToManyField(HTML)


class Program(models.Model):
    id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=50)
    sections = models.ManyToManyField(Section)


