from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    post_type_choices = models.TextChoices("Post Type", ["Article", "Opinion", "Review"])
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    is_published = models.BooleanField()
    post_type  = models.CharField(max_length=64, choices = post_type_choices.choices, default=post_type_choices.Article)

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}"


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.name}, {self.content}"
