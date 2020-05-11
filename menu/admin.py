from django.contrib import admin
from menu.models import Menu

admin.site.site_header = "Menu Items"

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'description',
			'today_special',
			'breakfast',
			'lunch',
			'snacks',
			'dinner',
		]
	list_per_page = 5


	list_display_links = ['name','description',
					'breakfast', 'lunch', 'snacks', 'dinner']

	list_editable = ['today_special',]

	search_fields = ['name',]

	list_filter = ['name',]

	fields = [
		# while creating user these field comes
		'name',
		'description',
		'today_special',
		'breakfast',
		'lunch',
		'snacks',
		'dinner',
	]

admin.site.register(Menu, MenuAdmin)