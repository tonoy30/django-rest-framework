from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='reviews')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(0)
                                 ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['email', 'course']

    def __str__(self):
        return '{0.rating} by {0.email} for {0.course}'.format(self)
