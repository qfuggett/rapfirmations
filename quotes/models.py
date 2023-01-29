from django.db import models


class Author(models.Model):
    "Author model"

    name = models.CharField(max_length=55)

    def __str__(self):
        return f'%s' % (self.name)

    def __repr__(self):
        return f'Author: %s' % (self.name)


class AuthorPhoto(models.Model):
    "AuthorPhoto model"

    photo = models.CharField(max_length=254)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Quote(models.Model):
    "Quote model"

    description = models.CharField(max_length=25)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'Quote: %s %s' % (self.description, self.author)

    def __repr__(self):
        return f'Quote: %s %s' % (self.description, self.author)
