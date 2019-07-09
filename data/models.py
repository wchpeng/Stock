from django.db import models

from Stock.enums import ENUM_STOCK_TYPE


class StockHistory(models.Model):
    # 股票历史信息
    code = models.CharField(max_length=6, verbose_name='股票代码', db_index=True)
    now = models.FloatField(default=0.00, verbose_name="现价")
    low = models.FloatField(default=0.00, verbose_name="今日最低价")
    high = models.FloatField(default=0.00, verbose_name="今日最高价")
    turnover = models.IntegerField(verbose_name="交易股数")
    volume = models.FloatField(verbose_name="交易金额")
    buy = models.FloatField(default=0.00, verbose_name="竞买价")
    sell = models.FloatField(default=0.00, verbose_name="竞卖价")
    datetime = models.DateTimeField(verbose_name="现在时间")

    ask1 = models.FloatField(default=0.00, verbose_name="卖一价")
    ask1_volume = models.IntegerField(default=0, verbose_name="卖一量")
    ask2 = models.FloatField(default=0.00, verbose_name="卖二价")
    ask2_volume = models.IntegerField(default=0, verbose_name="卖二量")
    ask3 = models.FloatField(default=0.00, verbose_name="卖三价")
    ask3_volume = models.IntegerField(default=0, verbose_name="卖三量")
    ask4 = models.FloatField(default=0.00, verbose_name="卖四价")
    ask4_volume = models.IntegerField(default=0, verbose_name="卖四量")
    ask5 = models.FloatField(default=0.00, verbose_name="卖五价")
    ask5_volume = models.IntegerField(default=0, verbose_name="卖五量")
    bind1 = models.FloatField(default=0.00, verbose_name="买一价")
    bind1_volume = models.IntegerField(default=0, verbose_name="买一量")
    bind2 = models.FloatField(default=0.00, verbose_name="买二价")
    bind2_volume = models.IntegerField(default=0, verbose_name="买二量")
    bind3 = models.FloatField(default=0.00, verbose_name="买三价")
    bind3_volume = models.IntegerField(default=0, verbose_name="买三量")
    bind4 = models.FloatField(default=0.00, verbose_name="买四价")
    bind4_volume = models.IntegerField(default=0, verbose_name="买四量")
    bind5 = models.FloatField(default=0.00, verbose_name="买五价")
    bind5_volume = models.IntegerField(default=0, verbose_name="买五量")

    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "股票历史"
        verbose_name_plural = "股票历史"


class Stock(models.Model):
    # 所有股票的基本信息表(包括实时数据)
    code = models.CharField(max_length=6, verbose_name='股票代码')
    name = models.CharField(max_length=32, verbose_name='公司名称')
    enum_stock_type = models.CharField(max_length=2, choices=ENUM_STOCK_TYPE, verbose_name="股票类型")
    now = models.FloatField(default=0.00, verbose_name="现价")
    low = models.FloatField(default=0.00, verbose_name="今日最低价")
    high = models.FloatField(default=0.00, verbose_name="今日最高价")
    turnover = models.IntegerField(verbose_name="交易股数")
    volume = models.FloatField(verbose_name="交易金额")
    buy = models.FloatField(default=0.00, verbose_name="竞买价")
    sell = models.FloatField(default=0.00, verbose_name="竞卖价")
    open = models.FloatField(default=0.00, verbose_name="开盘价")
    close = models.FloatField(default=0.00, verbose_name="收盘价（昨天）")
    datetime = models.DateTimeField(verbose_name="现在时间")

    ask1 = models.FloatField(default=0.00, verbose_name="卖一价")
    ask1_volume = models.IntegerField(default=0, verbose_name="卖一量")
    ask2 = models.FloatField(default=0.00, verbose_name="卖二价")
    ask2_volume = models.IntegerField(default=0, verbose_name="卖二量")
    ask3 = models.FloatField(default=0.00, verbose_name="卖三价")
    ask3_volume = models.IntegerField(default=0, verbose_name="卖三量")
    ask4 = models.FloatField(default=0.00, verbose_name="卖四价")
    ask4_volume = models.IntegerField(default=0, verbose_name="卖四量")
    ask5 = models.FloatField(default=0.00, verbose_name="卖五价")
    ask5_volume = models.IntegerField(default=0, verbose_name="卖五量")
    bind1 = models.FloatField(default=0.00, verbose_name="买一价")
    bind1_volume = models.IntegerField(default=0, verbose_name="买一量")
    bind2 = models.FloatField(default=0.00, verbose_name="买二价")
    bind2_volume = models.IntegerField(default=0, verbose_name="买二量")
    bind3 = models.FloatField(default=0.00, verbose_name="买三价")
    bind3_volume = models.IntegerField(default=0, verbose_name="买三量")
    bind4 = models.FloatField(default=0.00, verbose_name="买四价")
    bind4_volume = models.IntegerField(default=0, verbose_name="买四量")
    bind5 = models.FloatField(default=0.00, verbose_name="买五价")
    bind5_volume = models.IntegerField(default=0, verbose_name="买五量")

    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return "%s %s" % (self.code, self.name)

    class Meta:
        verbose_name = "股票"
        verbose_name_plural = "股票"


class StockRecommend(models.Model):
    # 推荐的股票表（根据相关策略计算得到）
    stock_code = models.CharField(max_length=6, verbose_name='股票代码')
    stock_name = models.CharField(max_length=32, verbose_name='公司名称')
    strategy = models.CharField(max_length=32, verbose_name='策略')
    latest = models.BooleanField(default=True, verbose_name='最新')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return "%s %s %s" % (self.stock_code, self.stock_name, self.strategy)

    class Meta:
        verbose_name = "股票推荐"
        verbose_name_plural = "股票推荐"
