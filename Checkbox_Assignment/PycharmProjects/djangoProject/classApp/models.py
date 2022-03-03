from django.db import models


# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField()

#Creating records using th model's construtor and Saving the Object into database
obj1 = djangoClasses(title='firstTitle', course_number=1, instructor_name='firstInstructor', duration=1.0)
obj1.save()
obj2 = djangoClasses(title='secondTitle', course_number=2, instructor_name='secondInstructor', duration=2.0)
obj2.save()
obj3 = djangoClasses(title='thirdTitle', course_number=3, instructor_name='thirdInstructor', duration=3.0)
obj3.save()