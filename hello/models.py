from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Event(models.Model):
    address = models.CharField(max_length=200)        
    start_time = models.DateTimeField(auto_now=True)   
    create_time = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.address



class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)     # 手机号
    email = models.EmailField()                 # 邮箱
    sign = models.BooleanField()                # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ('phone', 'event')
        ordering = ['-id']

    def __str__(self):
        return self.realname
