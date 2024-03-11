from modeltranslation.admin import TranslationAdmin
from .models import Author, Category, Post, Comment, PostCategory
from modeltranslation.translator import register, TranslationOptions


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('user', )  # не надо было использовать поле OneToOneField


class AuthorAdmin(TranslationAdmin):
    model = Author


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


class CategoryAdmin(TranslationAdmin):
    model = Category


#@register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')  # ?


# class PostAdmin(TranslationAdmin):
#     model = Post
