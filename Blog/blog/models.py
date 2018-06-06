from django.db import models
from django.utils import timezone

class Category(models.Model):
    uri_categories = models.CharField(max_length=30)
    def __str__(self):
        return self.uri_categories
        
class Language(models.Model):
    programming_language = models.CharField(max_length=30)
    def __str__(self):
        return self.programming_language

class Uri(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    number = models.IntegerField(default=None) 
    language_type = models.ForeignKey(Language, on_delete=models.CASCADE)
    code = models.TextField()
    pub_date = models.DateTimeField(blank=False, null=True)
    def __str__(self):
        return "%s  - URI%s - %s - %s" % (self.category, self.number, self.title,
                self.language_type)

