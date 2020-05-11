from django.contrib import admin
from breakfast.models import Breakfast


# Register your models here.
class BreakfastAdmin(admin.ModelAdmin):
	list_display = [
			'item_name',
			'item_price',
			'created',
			'is_active',
			'created_by',
		]
	list_per_page = 5


	list_display_links = ['item_name',]

	list_editable = ['item_price',]

	search_fields = ['item_name',]

	list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'item_name',
		'item_price',
	]

admin.site.register(Breakfast, BreakfastAdmin)
