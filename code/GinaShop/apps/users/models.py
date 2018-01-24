from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户配置model
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    mobile = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female",
                              verbose_name="性别")
    gender = models.CharField(max_length=11, verbose_name="电话")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        # 给模型类起一个更可读的名字
        verbose_name = "用户"
        # 模型的复数形式
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码model
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 给模型类起一个更可读的名字
        verbose_name = "短信验证码"
        # 模型的复数形式
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
