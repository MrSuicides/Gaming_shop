from django.contrib import admin
from .models import Audio, Keyboard, Mice, Brend
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'brend')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_description = "Изображение"

@admin.register(Mice)
class MiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'brend')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_description = "Изображение"

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'brend')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_description = "Изображение"


admin.site.register(Brend)


