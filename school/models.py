from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email =  models.EmailField()
    password = models.CharField(max_length=70)

    # # upon submitting 'ContactForm', it will redirect to this "thankyou-page" url
    # def get_absolute_url(self):
    #     return reverse("thankyou-page")
    
    def get_absolute_url(self):
        """
        upon submitting 'ContactForm', it will show the student details.
        Since it's "DetailView", we must pass "pk" to see the details.
        """
        return reverse("student-detail", kwargs={"pk": self.pk})


