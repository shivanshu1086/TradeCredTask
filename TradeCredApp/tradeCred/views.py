from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views.generic import View
from pyexcel_xls import get_data

from .models import VendorModel


def index(request):
    return render(request, 'index.html')


def import_excel_file(self, *args, **kwargs):
    data = get_data("static/test_documents_upload.xls")
    data_dict = dict(data)
    for i in range(1, len(data_dict['Documents'][1:]) + 1):
        temp = data_dict['Documents'][i]
        try:
            try:
                VendorModel.objects.get(document_number=temp[1])
                return "exists"
            except ObjectDoesNotExist:
                VendorModel.objects.create(
                    invoice_number=temp[0], document_number=temp[1],
                    type_of_invoice=temp[2], net_due_date=temp[3],
                    doc_date=temp[4], pstng_date=temp[5], amount=temp[6],
                    vendor_code=temp[7], vendor_name=temp[8], vendor_type=temp[9])
        except Exception as ex:
            print(ex)
            return False
    print("Success")
    return True


class Upload_data(View):
    def get(self, *args, **kwargs):
        response = import_excel_file(self, *args, **kwargs)
        if response is True:
            messages.success(self.request, "The data has been uploaded successfully!")
            return render(self.request, 'upload.html')
        elif response is "exists":
            messages.info(self.request, "Some data already exists. Try fresh rows!")
            return redirect("/")
        elif response is False:
            messages.info(self.request, "There is some error importing sheet. Please try again!")
            return redirect("/")


def get_all_vendors(model_data):
    vendors_query_set = VendorModel.objects.values('vendor_name')
    vendors_set = set()
    for i in range(0, len(vendors_query_set)):
        vendors_set.add(vendors_query_set[i]['vendor_name'])
    vendors_list = list(vendors_set)
    return vendors_list


class See_Vendors_data(View):
    def get(self, *args, **kwargs):
        model_data = VendorModel.objects.all()
        if (len(model_data) > 1):
            vendors_data = get_all_vendors(model_data)
            content = {
                'vendors': vendors_data,
                'vendors_data': model_data,
            }
            return render(self.request, "see_data.html", content)
        messages.info(self.request, 'Insert Data First!')
        return redirect("/")


class Delete_data(View):
    def get(self, *args, **kwargs):
        VendorModel.objects.all().delete()
        messages.success(self.request, "Deleted successfully!")
        return redirect("/")
