from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


# ----------------- PostAdmin -------------
def clear_rate_new(ModelAdmin, request, queryset):  # выборочно обнуляем рейтинги
    queryset.update(rate_new=0)

clear_rate_new.short_description = 'Обнулить рейтинг'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'choice_types', 'time_in', 'rate_new', 'get_categories',)
    list_filter = ('title', 'rate_new',)
    search_fields = ('title', 'categories_post__category_name')
    actions = [clear_rate_new]  # добавляем действия в список

# ----------------- CategoryAdmin -------------
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'get_subscribers',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)

# -------------  PostCategoryAdmin -------------------

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'post',)
    list_filter = ('category',)


# -------------   Author -------------------
def clear_rating(ModelAdmin, request, queryset):  # выборочно обнуляем рейтинги
    queryset.update(rating=0)

clear_rating.short_description = 'Обнулить рейтинг'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'get_user_categories',)
    list_filter = ('user', 'rating',)
    search_fields = ('user', 'rating',)
    actions = [clear_rating]



# -----------------    регистрация ----------------------
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment)

