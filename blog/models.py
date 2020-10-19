from django.db import models
from django.urls import reverse
# At This stage we are creating a model for our database
# The model has three field in the total but
# the Author field has a primary key because of DB model on one is to many
# An Author can have multiple post but not the other way round


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    text = models.TextField()

    def __str__(self):
        return self.title[:30]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

# Reverse is a very handy utility function Django provides us to reference an object by
# its URL template name, in this case post_detail. If you recall our URL pattern is the following

