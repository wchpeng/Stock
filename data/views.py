from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.db.models.query_utils import Q

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

        obj_list = self.get_obj_list()
        data = {"data": obj_list.values('code', 'name', 'datetime')}

        return super(StockListView, self).get(request, *args, **data)

    def get_obj_list(self):
        q = self.request.GET.get('q', None)
        all = self.request.GET.get('all', None)
        per_page = self.request.GET.get('per_page', 40)

        if q is None:
            obj_list = Stock.objects.all()
        else:
            obj_list = Stock.objects.filter(Q(code__contains=q) | Q(name__contains=q))

        if all:
            return obj_list
        return obj_list[0:int(per_page)]
