from django.contrib import admin
from .models import Category, Costs, Types


admin.site.register(Costs)
admin.site.register(Category)
admin.site.register(Types)