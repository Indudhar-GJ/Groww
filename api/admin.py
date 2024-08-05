from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CourseChapter)
admin.site.register(BoughtCourses)
admin.site.register(Quiz)
