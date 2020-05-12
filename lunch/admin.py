from django.contrib import admin
from lunch.models import Lunch


# Register your models here.

class LunchAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created_by',
			'menu',
		]
	list_per_page = 5


	list_display_links = ['item_name', 'menu']

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
		'menu',
	]

admin.site.register(Lunch, LunchAdmin)
