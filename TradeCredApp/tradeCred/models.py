from django.db import models

# Create your models here.


class VendorModel(models.Model):
    invoice_number = models.IntegerField()
    document_number = models.IntegerField()
    type_of_invoice = models.CharField(max_length=100)
    net_due_date = models.DateField()
    doc_date = models.DateField()
    pstng_date = models.DateField()
    amount = models.IntegerField()
    vendor_code = models.CharField(max_length=100)
    vendor_name = models.TextField()
    vendor_type = models.CharField(max_length=100)
