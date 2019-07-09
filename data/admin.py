from django.contrib import admin

from data.models import Stock, StockHistory, StockRecommend


class StockAdmin(admin.ModelAdmin):

    list_display = ['code', 'name', 'enum_stock_type', 'now', 'low', 'high', 'datetime', 'update_time', 'create_time']
    search_fields = ['code', 'name']
    ordering = ('-now', 'id')


class StockHistoryAdmin(admin.ModelAdmin):

    list_display = ['code', 'now', 'low', 'high', 'datetime', 'update_time', 'create_time']
    search_fields = ['code']


class StockRecommendAdmin(admin.ModelAdmin):

    list_display = ['stock_code', 'stock_name', 'strategy', 'latest', 'create_time']
    search_fields = ['stock_code', 'stock_name']


admin.site.register(Stock, StockAdmin)
admin.site.register(StockHistory, StockHistoryAdmin)
admin.site.register(StockRecommend)
