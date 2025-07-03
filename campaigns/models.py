from django.db import models

# Create your models here.
class Campaign(models.Model):
    CATEGORY_CHOICES =[
        ('sadaqah','Sadaqah'),
        ('zakat-al-mal','Zakat-al-mal'),
        ('zakat-al-Fitr','Zakat-al-Fitr'),
        ('others','Others')
    ]
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="campaign_images/", null=True, blank=True)
    description = models.TextField()
    type_of_category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default=CATEGORY_CHOICES[0])
    

    def __str__(self):
        return self.title
    