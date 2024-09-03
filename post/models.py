from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ( 'WB' , 'Web Development'),  # first save in db , second apear in web
    ('DB','Desktop Development'),
    ('DS','Data Science'),
)
class Post(models.Model):
    title = models.CharField(max_length=50 , unique=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField()
    published = models.BooleanField(default=True)
    email = models.EmailField(max_length=254 , null=True, blank=True) 
    # null -> ignore data in field
    # blank -> ignore data in field in form
    views_count = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICE , max_length=20)

    def __str__(self):
        return self.title
