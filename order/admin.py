from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.



class OrderAdmin(admin.ModelAdmin):
	# list_display = [
	# 		# 'menu',
	# 		'item_name',
	# 		'item_price',
	# 		'created',
	# 		'is_active',
	# 		# 'created_by',
	# 	]
	# list_per_page = 5


	# list_display_links = ['item_name', ]

	# list_editable = ['item_price',]

	# search_fields = ['item_name',]

	# list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		'menu',
		'item',
		'price',
		'title',
	]

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
	# list_display = [
	# 		# 'menu',
	# 		'item_name',
	# 		'item_price',
	# 		'created',
	# 		'is_active',
	# 		# 'created_by',
	# 	]
	# list_per_page = 5


	# list_display_links = ['item_name', ]

	# list_editable = ['item_price',]

	# search_fields = ['item_name',]

	# list_filter = ['item_name',]

	fields = [
		# while creating user these field comes
		# 'menu',
		'item_name',
		'price',
	]

admin.site.register(OrderItem, OrderItemAdmin)