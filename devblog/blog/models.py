from django.db import models

class Category(models.Model):
        title = models.CharField(max_length=255)
        slug = models.SlugField()
        
        class Meta:
            verbose_name_plural = 'Categories'

        def __str__(self):
           return self.title 

class Posts(models.Model):
        category=models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
        title=models.CharField(max_length=255)
        slug=models.SlugField()
        
        intro=models.TextField()
        body=models.TextField()
        pub_date=models.DateTimeField(auto_now_add=True)
        
        class Meta:
            verbose_name_plural = "Posts's"

        def __str__(self):
            return self.title

class Comment(models.Model):
        post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        body=models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
           return '%s - %s' % (self.post.title, self.name)
