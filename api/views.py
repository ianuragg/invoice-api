from rest_framework.response import Response
from .serializers import InvoiceSerializer
from .models import Invoice, InvoiceDetail
from rest_framework import viewsets


#Invoices API
class InvoiceApi(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        invoice = serializer.save()

        # Create or update invoice details
        invoice_details_data = request.data.get('invoice_details', [])
        for invoice_detail_data in invoice_details_data:
            invoice_detail = InvoiceDetail(
                invoice=invoice,
                description=invoice_detail_data['description'],
                quantity=invoice_detail_data['quantity'],
                unit_price=invoice_detail_data['unit_price'],
                price=invoice_detail_data['price'],
            )
            invoice_detail.save()

        return Response(serializer.data)
    

    def update(self, request, pk, format=None):
        invoice = Invoice.objects.get(id=pk)
        serializer = self.serializer_class(invoice, data=request.data)
        serializer.is_valid(raise_exception=True)

        # Update the invoice details
        invoice_details_data = request.data.get('invoice_details', [])
        for invoice_detail_data in invoice_details_data:
            invoice_detail = InvoiceDetail.objects.get(id=invoice_detail_data['id'])
            invoice_detail.description = invoice_detail_data['description']
            invoice_detail.quantity = invoice_detail_data['quantity']
            invoice_detail.unit_price = invoice_detail_data['unit_price']
            invoice_detail.price = invoice_detail_data['price']
            invoice_detail.save()

        # Update the invoice
        serializer.save()

        return Response(serializer.data)