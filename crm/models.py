from django.db import models


# Create your models here.

class Customer(models.Model):
    """客户表"""
    first_name = models.CharField(max_length=32, null=True, verbose_name="姓")
    last_name = models.CharField(max_length=32, null=True, verbose_name="名")
    address = models.TextField(null=True, verbose_name="地址")
    head_url = models.CharField(max_length=128, null=True, verbose_name="头像")

    create_time = models.DateTimeField(verbose_name="创建时间", null=True, auto_now_add=True)
    creator = models.ForeignKey("User", related_name="creator", verbose_name="创建者", default=1)
    modify_time = models.DateTimeField(verbose_name="修改时间", null=True, auto_now=True)
    modifier = models.ForeignKey("User", related_name="modifier", verbose_name="修改者", default=1)
    company = models.ForeignKey("Company", verbose_name="单位名称", default=1)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户"


class Company(models.Model):
    """单位表"""
    name = models.CharField(max_length=64, null=True, verbose_name="公司名称")
    address = models.CharField(max_length=128, null=True, verbose_name="详细地址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "单位"  # 将表名设置为中文，但是在中文表名后面有个“单位表s”表示复数，用下面就可以把复数去掉
        verbose_name_plural = "单位"


class User(models.Model):
    """用户"""
    name = models.CharField(max_length=32, unique=True, verbose_name="用户名称")
    head_url = models.CharField(max_length=128, null=True, verbose_name="头像")

    # roles = models.ManyToManyField("Role", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=32, unique=True, verbose_name="角色名称")

    # users = models.ManyToManyField("User", blank=True, null=True)

    menus = models.ManyToManyField("Menu", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"


class Menu(models.Model):
    """菜单表"""
    name = models.CharField(max_length=32, verbose_name="菜单名称")
    parent = models.ForeignKey("Menu", blank=True)
    level = models.CharField(max_length=8, blank=True, verbose_name="等级")
    code = models.CharField(max_length=64, blank=True)
    path = models.CharField(max_length=64, blank=True, verbose_name="链接地址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = "菜单"
