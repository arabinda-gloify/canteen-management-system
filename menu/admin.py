from django.contrib import admin
from menu.models import Menu

admin.site.site_header = "Menu Items"

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'description',
			
		]
	list_per_page = 4


	list_display_links = ['name','description']

	# list_editable = ['name',]

	search_fields = ['name', 'description']

	list_filter = ['name',]

	fields = [
		# while creating user these field comes
		'name',
		'description',
		'is_active',
		
	]



admin.site.register(Menu, MenuAdmin)