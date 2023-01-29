from django.contrib import admin
from .models import Quote
from .models import Author
from .models import AuthorPhoto


admin.site.register(AuthorPhoto)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):

    def name(self, obj):
        return obj.author.name

    fields = ["description", "author"]
    list_display = ["description", "author"]
