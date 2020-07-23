from django.db import models
from datetime import datetime
# Create your models here.


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Catagories"
        # it onerwrites default TutorialCategorys model in admin

    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    # forign key points to the mectioned model's primary key ,if explicitly not mentioned using to_field
    tutorial_category = models.ForeignKey(
        TutorialCategory, verbose_name="Category", default=1, on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"
        # it onerwrites default TutorialCategorys model in admin

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        "date published", default=datetime.now())
    tutorial_series = models.ForeignKey(
        TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title
