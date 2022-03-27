from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView

import forecast_pred
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill,SaleItem


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []
        listsend = []
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        # saleitem = SaleItem.objects.filter('billno_id')
        listsend = forecast_pred.trythis()
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases,
            'listsend' : listsend
            # 'saleitme'  : saleitem
        }

        return render(request, self.template_name, context)

    def getList(self):

            # import function to run
            from forecast_pred import trythis

            # call function
            valussss = trythis()

            # return user to required page
            return HttpResponseRedirect(valussss)



class AboutView(TemplateView):
    template_name = "about.html"


