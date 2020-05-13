from django.contrib import admin
from invoice.models import Invoice


# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
	list_display = [
			'invoice_number',
			'date_of_issue',
			'unit_price',
			'discount_amount',
			# 'canteen.name',
			# 'user.username',
			'total_price',
			'is_active',
			# 'created_by',
		]
	list_per_page = 5


	# list_display_links = ['invoice_number', 'canteen.name']

	# list_editable = ['item_price',]

	search_fields = ['invoice_number',]

	list_filter = ['invoice_number',]

	fields = [
		# while creating user these field comes
		'invoice_number',
		'unit_price',
		'discount_amount',
		'total_price',
	]

admin.site.register(Invoice, InvoiceAdmin)
