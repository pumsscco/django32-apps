#coding=UTF8
from django.db import models

class Stock(models.Model):  #股票交易记录
    id = models.AutoField(primary_key=True)
    date=models.DateField(help_text='成交日期', verbose_name='成交日期')
    code=models.CharField(max_length=6, help_text='股票代码')
    name=models.CharField(max_length=16, help_text='股票名称')
    OPERATION_CHOICES=(
        (u'证券买入', u'证券买入'),
        (u'证券卖出', u'证券卖出'),
        (u'股息入帐', u'股息入账'),
        (u'红股入帐', u'红股入账'),
        (u'申购中签', u'申购中签'),
        (u'股息红利税补', u'股息红利税补'),
    )
    operation=models.CharField(max_length=24, choices=OPERATION_CHOICES, help_text='操作类型')
    volume=models.SmallIntegerField(help_text='成交数量')
    balance=models.IntegerField(help_text='变动后持股数量')
    price=models.DecimalField(max_digits=5, decimal_places=2, help_text='成交均价')
    turnover=models.DecimalField(max_digits=8, decimal_places=2, help_text='成交金额')
    amount=models.DecimalField(max_digits=8, decimal_places=2, help_text='发生金额')
    brokerage=models.DecimalField(max_digits=5, decimal_places=2, help_text='佣金')
    stamps=models.DecimalField(max_digits=5, decimal_places=2, help_text='印花税')
    transfer_fee=models.DecimalField(max_digits=4, decimal_places=2, help_text='过户费', default=0.00)


    def __unicode__(self):
        return "成交日期:%s;股票名称:%s;操作类型:%s;成交数量:%d" % (self.date,self.name,self.operation,self.volume)

    class Meta:
        db_table='stock'
        unique_together=('date','code','operation','price')
        ordering=['-date']


