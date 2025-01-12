from django.contrib import admin
from .models import Course, CourseCategory, Purchase, Batch
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','status')
admin.site.register(Course,CourseAdmin)

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(CourseCategory,CourseCategoryAdmin)

admin.site.register(Purchase)

class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_name',)
admin.site.register(Batch,BatchAdmin)