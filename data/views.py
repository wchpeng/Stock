from django.shortcuts import render
from django.views.generic.base import TemplateView


class StockInfoView(TemplateView):

    template_name = 'stock/stock_info'

    def get(self, request, *args, **kwargs):
        data = {
            'code': '',
            'name': '',
            'e_charts': {}
        }
        return super(StockInfoView, self).get(request, *args, **data)
