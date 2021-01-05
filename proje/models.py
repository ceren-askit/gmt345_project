from django.db import models

# Create your models here.
class Academician(models.Model):
    aca_name = models.CharField(max_length=15)
    aca_surname = models.CharField(max_length=15)
    aca_email = models.EmailField()

class Student(models.Model):
    s_id = models.IntegerField( primary_key=True)
    s_name = models.CharField(max_length=15)
    s_surname = models.CharField(max_length=15)
    s_email = models.EmailField()

class Courses(models.Model):
    c_id = models.CharField(max_length=6 , primary_key=True)
    c_name = models.CharField(max_length=30)

class LectureNotes(models.Model):
    l_course = models.ForeignKey(Courses, on_delete= models.CASCADE)

class Videos(models.Model):
    v_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

class Books(models.Model):
    b_course = models.ForeignKey(Courses, on_delete=models.CASCADE)




