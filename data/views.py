from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from data.models import StockHistory, Stock


class StockInfoView(TemplateView):

    template_name = 'data/stock_info.html'

    def get(self, request, code, **kwargs):

        stock_history_info = StockHistory.objects.filter(code=code).values_list('now', 'datetime')
        stock_info = get_object_or_404(Stock, code=code)

        series = [i[0] for i in stock_history_info]
        x_axis = [i[1].strftime("%Y/%m/%d %H") for i in stock_history_info]

        data = {
            'code': code,
            'name': stock_info.name,
            'e_charts': {
                'x_axis': x_axis,
                'series': series
            }
        }
        return super(StockInfoView, self).get(request, **data)


class StockListView(TemplateView):

    template_name = 'data/stock_list.html'

    def get(self, request, *args, **kwargs):

        data = {"data": Stock.objects.all().values('code', 'name')}

        return super(StockListView, self).get(request, *args, **data)