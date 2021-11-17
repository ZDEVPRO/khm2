from django.contrib import admin
from home.models import ContactMessage, Logo, Teacher, News, Total, Pages, ContactFooter, AboutIndex, AboutFooter, \
    ContactAboutPage, Hometitle


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'phone', 'image_tag']
    readonly_fields = ('image_tag',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'create_on_time', 'create_on_date']
    readonly_fields = ('image_tag', 'create_on_time', 'create_on_date')
    prepopulated_fields = {'slug': ('title',)}


class TotalAdmin(admin.ModelAdmin):
    list_display = ['num_students', 'num_teachers', 'num_groups', 'num_room']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'creat_at']
    readonly_fields = ('name', 'subject', 'phone', 'message', 'ip',)


class PagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


class ContactFooterAdmin(admin.ModelAdmin):
    list_display = ['phone', 'adress']


class AboutIndexAdmin(admin.ModelAdmin):
    list_display = ['title']


class AboutFooterAdmin(admin.ModelAdmin):
    list_display = ['title']


class HometitleAdmin(admin.ModelAdmin):
    list_display = ['title']


class ContactAboutAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address', 'email']


class LogoAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Logo, LogoAdmin)
admin.site.register(Hometitle, HometitleAdmin)
admin.site.register(AboutFooter, AboutFooterAdmin)
admin.site.register(ContactAboutPage, ContactAboutAdmin)
admin.site.register(AboutIndex, AboutIndexAdmin)
admin.site.register(ContactFooter, ContactFooterAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Total, TotalAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
