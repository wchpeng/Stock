from django.contrib import admin

from data.models import Stock, StockHistory, StockRecommend


admin.site.register(Stock)
admin.site.register(StockHistory)
admin.site.register(StockRecommend)
