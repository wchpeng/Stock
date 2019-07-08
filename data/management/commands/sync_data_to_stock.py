# 同步最新数据到 stock 表（每只股票的实时信息）
import time

from django.core.management.base import CommandError, BaseCommand

from data.models import Stock
from ._utils import get_all_stock_info


class Command(BaseCommand):

    help = '同步最新数据到 stock 表（每只股票的实时信息）'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("start aync data to stock: >>>>>>>>>>>>>>>>>>>>>>")
        t0 = time.time()
        data = get_all_stock_info()
        if data:
            for code, val in data.items():
                kwargs = {
                    'datetime': val.get('datetime') or '%s %s' % (val.get('date', ''), val.get('time', '')),
                    'now': val['now'],
                    'low': val['low'],
                    'high': val['high'],
                    'turnover': val['turnover'],
                    'volume': val['volume'],
                    'buy': val['buy'],
                    'sell': val['sell'],
                    'open': val['open'],
                    'close': val['close'],
                    'ask1': val.get('ask1', 0.00),
                    'ask1_volume': val.get('ask1_volume', 0), 
                    'ask2': val.get('ask2', 0.00),
                    'ask2_volume': val.get('ask2_volume', 0),
                    'ask3': val.get('ask3', 0.00),
                    'ask3_volume': val.get('ask3_volume', 0), 
                    'ask4': val.get('ask4', 0.00),
                    'ask4_volume': val.get('ask4_volume', 0), 
                    'ask5': val.get('ask5', 0.00),
                    'ask5_volume': val.get('ask5_volume', 0),
                    'bind1': val.get('bind1', 0.00),
                    'bind1_volume': val.get('bind1_volume', 0), 
                    'bind2': val.get('bind2', 0.00),
                    'bind2_volume': val.get('bind2_volume', 0),
                    'bind3': val.get('bind3', 0.00),
                    'bind3_volume': val.get('bind3_volume', 0), 
                    'bind4': val.get('bind4', 0.00),
                    'bind4_volume': val.get('bind4_volume', 0), 
                    'bind5': val.get('bind5', 0.00),
                    'bind5_volume': val.get('bind5_volume', 0),
                }

                try:
                    stock = Stock.objects.get(code=code[2:])
                except Stock.DoesNotExist:
                    kwargs['code'] = code[2:]
                    kwargs['name'] = val['name']
                    kwargs['enum_stock_type'] = code[:2]
                    stock = Stock()
                    print('----------------------------------------------')
                    print(kwargs)
                    print('----------------------------------------------')

                for k, v in kwargs.items():
                    setattr(stock, k, v)
                stock.save()
        print("cost: %.2f <<<<<<<<<<<<<<<<<<<<<<<<" % (time.time()-t0))
