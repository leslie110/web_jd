from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')


class Chioce(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Test(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.__doc__ + ":name->" + self.name

class User(models.Model):
    user_name = models.CharField(max_length=30,
                                 primary_key=True)
    psw = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    def __str__(self):
        return self.__doc__ + ":user_name->" + self.user_name

class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    auth = models.CharField(max_length=10,verbose_name='作者')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True,verbose_name='最后更新时间')

    def __str__(self):
        return self.__doc__
    class Meta:
        verbose_name_plural= '文章列表'

class Bank(models.Model):
    '''银行信息'''
    bank_name = models.CharField(max_length=50,verbose_name='银行名称')
    city = models.CharField(max_length=30,verbose_name='城市')
    point = models.CharField(max_length=60,verbose_name='网点')

    class Meta:
        verbose_name_plural = '银行卡'
    def __str__(self):
        return self.bank_name

class CardInfo(models.Model):
    '''卡信息'''
    info = models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name='选择银行')
    card_id = models.CharField(max_length=30,verbose_name='卡号')
    card_name = models.CharField(max_length=10,verbose_name='姓名')

    class Meta:
        verbose_name_plural = '卡号信息'

    def __str__(self):
        return self.card_id

