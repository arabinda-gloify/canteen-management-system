from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'email', 'first_name', 'last_name', 'gender', 'contact_no',
		'is_admin', 'is_active', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)