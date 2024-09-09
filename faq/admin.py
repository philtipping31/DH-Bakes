from django.contrib import admin
from .models import FAQ, FAQCategory

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'category')
    search_fields = ('question', 'answer')
    ordering = ('order',)

class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(FAQ, FAQAdmin)
admin.site.register(FAQCategory, FAQCategoryAdmin)
