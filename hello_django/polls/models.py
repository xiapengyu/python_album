# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Test(models.Model):
    a = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)
    d = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    user_name = models.CharField(max_length=255, verbose_name='用户名')
    age = models.IntegerField(verbose_name='年龄')
    job = models.CharField(max_length=255, verbose_name='职业')
    phone = models.CharField(unique=True, max_length=255, verbose_name='手机号码')

    class Meta:
        managed = False
        db_table = 'user'
