from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    st_date = models.DateField(auto_now=False, auto_now_add=False)
    prof_name = models.ManyToManyField('Prof')
    user = models.ForeignKey('auth.User', null=True, blank=True,
                             on_delete=models.SET_NULL)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class SubChapter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hour = models.DecimalField(max_digits=3, decimal_places=0)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Prof (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
