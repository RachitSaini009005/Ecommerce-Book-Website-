
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Books_author_book_registration(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/')
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    pageno = models.PositiveIntegerField(default=0)
    format = models.CharField(max_length=50)
    edition = models.CharField(max_length=50, blank=True, null=True)
    keywords = models.CharField(max_length=255)
    availability = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    
