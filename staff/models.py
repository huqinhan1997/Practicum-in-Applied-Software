from django.db import models

# Create your models here.
class Staff(models.Model):

    genders = (('男','男'),('女','女'))
    sid = models.CharField(db_column='职工号',max_length = 32,unique = True,primary_key=True)
    sname = models.CharField(db_column='姓名',max_length = 64)
    age = models.IntegerField(db_column='年龄')
    gender = models.CharField(db_column='性别',max_length = 32, choices=genders,default='男')
    c_time = models.DateTimeField(db_column='注册时间',auto_now_add=True)
    password = models.CharField(db_column='登录密码',max_length = 256)
    def __str__(self):
        return self.sname
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


class Club(models.Model):
    cid = models.CharField(db_column='编号',max_length=32,unique=True,primary_key=True)
    cname = models.CharField(db_column='名称',max_length=64)
    manager = models.CharField(db_column='负责人',max_length=32)
    location = models.CharField(db_column='活动地点',max_length=128)

    def __str__(self):
        return self.cname


class Activity(models.Model):
    aid = models.CharField(db_column='编号',max_length=32, primary_key=True)
    aname = models.CharField(db_column='名称',max_length=64)
    cname = models.CharField(max_length=64,db_column='社团')
    manager = models.CharField(db_column='负责人',max_length=64)
    location = models.CharField(db_column='活动地点',max_length=128)
    #date = models.CharField(db_column='活动时间',max_length=32)
    date = models.DateTimeField(db_column='活动时间')
    nump = models.IntegerField(db_column='人数')

    def __str__(self):
        return self.aname

class Join(models.Model):
    sid = models.ForeignKey('Staff',on_delete=models.CASCADE,db_column='职工号')
    aid = models.ForeignKey('Activity',on_delete=models.CASCADE,db_column='活动编号')
    j_time = models.DateTimeField(auto_now_add=True,db_column='报名时间')

    def __str__(self):
        return str(self.sid)+'->'+str(self.aid)


class Apply(models.Model):
    staffname = models.CharField(max_length=64,db_column='申请人')
    staffid = models.CharField(max_length=32,db_column='申请人编号')
    clubname = models.CharField(max_length=64,db_column='申请社团')
    clubid = models.CharField(max_length=32,db_column='社团编号')
    status = models.CharField(max_length=32,db_column='状态',default='待审核')
    a_time = models.DateTimeField(db_column='申请时间',auto_now_add=True)

    def __str__(self):
        return self.staffname +'-->' + self.clubname

class News(models.Model):
    aname = models.CharField(max_length=64,db_column='活动名称')
    cname = models.CharField(max_length=64,db_column='社团')
    date = models.DateTimeField(db_column='活动时间')

    def __str__(self):
        return self.aname