from django.db import models

# Create your models here.

##THIS IS A CLASS THAT DEFINES OBJECTS IN THE DATABASE AND THE PARAMETERS ASSOCIATED WITH THEM
##YOU MUST ADD IT TO ADMIN.PY AND REGISTER IT THERE IN ORDER TO USE IT AS A SUPERUSER
class djangoClasses(models.Model):
    Title = models.CharField(max_length=100, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default="", blank=True, null=False)

    objects = models.Manager()

##THIS DEFINES WHAT REPRESENTATION OF AN OBJECT GETS RETURNED TO THE USER IF __str__() IS CALLED
    def __str__(self):
        return self.Title