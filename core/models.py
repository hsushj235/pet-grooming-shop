from django.db import models

# Create your models here.
class Contract(models.Model):
    """在线预约记录"""

    PET_TYPE_CHOICES = [
        ('dog', '狗狗'),
        ('cat', '猫咪'),
        ('other', '其他'),
    ]

    pet_name = models.CharField('宠物姓名', max_length=100)
    pet_type = models.CharField('宠物类型', max_length=20, choices=PET_TYPE_CHOICES, default='dog')
    breed = models.CharField('品种', max_length=100, blank=True, default='')
    weight = models.DecimalField('体重(kg)', max_digits=5, decimal_places=1, blank=True, null=True)
    service = models.CharField('服务项目', max_length=200)
    date = models.DateField('预约日期')
    time = models.CharField('预约时段', max_length=20)
    phone = models.CharField('主人手机号', max_length=20)
    remark = models.TextField('备注信息', blank=True, default='')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '预约记录'
        verbose_name_plural = '预约记录'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.pet_name} - {self.service} ({self.date} {self.time})"
