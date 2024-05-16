from django.db import models

# Create your models here.

# Create your models here.

# resume data model

class Student_data(models.Model):
    # student detail------
    created=models.DateTimeField(auto_now_add=True,null=True)
    s_name=models.CharField(max_length=100)
    s_email=models.EmailField()
    s_mobile=models.CharField(max_length=12)
    s_address=models.TextField()
    # course detail
    c_desc=models.TextField()
    c_amt=models.PositiveIntegerField()
    c_rec_amt=models.PositiveIntegerField()
    c_rec_amt_word = models.TextField()
    c_pen_amt=models.PositiveIntegerField()
    c_due_date=models.CharField(max_length=100)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return str(self.s_name)
class Image(models.Model):
    company_logo=models.ImageField(upload_to="logo/", null=True)
    

