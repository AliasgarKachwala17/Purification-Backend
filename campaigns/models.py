from django.db import models
from django.utils import timezone

# Create your models here.
class Campaign(models.Model):
    CATEGORY_CHOICES =[
        ('sadaqah','Sadaqah'),
        ('zakat-al-mal','Zakat-al-Mal'),
        ('zakat-al-fitr','Zakat-al-Fitr'),
        ('others','Others')
    ]
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="campaign_images/", null=True, blank=True)
    description = models.TextField()
    type_of_category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default=CATEGORY_CHOICES[0])
    tags = models.JSONField(default=list)
    goal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    raised = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    is_featured = models.BooleanField(default=False)

    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def daysleft(self):
        """Compute days remaining until end_date."""
        today = timezone.localdate()
        delta = (self.end_date - today).days
        return max(delta, 0)