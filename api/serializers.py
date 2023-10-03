from rest_framework import serializers
from .models import Invoice, InvoiceDetail


#Invoice Serializer
class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = [
            'id',
            'description',
            'quantity',
            'unit_price',
            'price',
        ]

#Invoice Detail Serializer
class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = [
            'id',
            'date',
            'customer_name',
            'invoice_details',
        ]

    def get_invoice_details(self, invoice):
        return InvoiceDetailSerializer(invoice.invoice_details, many=True).data