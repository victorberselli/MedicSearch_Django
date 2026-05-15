from django.contrib import admin

# Register your models here.
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birthday', 'birth', 'specialtiesList', 'addressesList',)
    empty_value_display = 'Vazio'
    list_display_links = ('user', 'role')
    list_filter = ('user__is_active',)
    #fields = ('user', ('role',), 'image', 'birthday', 'specialties', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )

    

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
    
    birth.empty_value_display = '___/___/_____'

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]
    
    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)