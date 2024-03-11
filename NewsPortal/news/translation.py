#from modeltranslation.admin import TranslationAdmin

from .models import Author, Category, Post, Comment, PostCategory
#from modeltranslation.translator import register, TranslationOptions


# class AuthorTranslationOptions(TranslationOptions):
#     fields = ('user', )  # указываем, какие именно поля надо переводить в виде кортежа

# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('category_name',)


# class CategoryAdmin(TranslationAdmin):
#     model = Category
