from django.contrib import admin

from .models import Rating, Testimonial


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'rated_by', 'rating']


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'testimonial')
    search_fields = ('order', 'user__username', 'testimonial')


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Rating, RatingAdmin)
