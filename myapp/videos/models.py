from django.db import models

class CountryCode(models.TextChoices):
    '''区域代码'''
    ZH = '华语','华语'
    HK = '香港地区','香港地区'
    US = '美国','美国'
    EU = '欧洲','欧洲'
    KO = '韩国','韩国'
    JP = '日本','日本'
    TAI = '泰国','泰国'
    IND = '印度','印度'
    OTH = '其它','其它'

class VideoType(models.TextChoices):
    '''影片类型'''
    COMEDY = '喜剧','喜剧'
    ROMATIC = '爱情','爱情'
    ACTION = '动作','动作'
    GUN = '枪战','枪战'
    CRIME = '犯罪','犯罪'
    THRILLER = '惊悚','惊悚'
    HORRIBLE = '恐怖','恐怖'
    DETECT = '悬疑','悬疑'
    CARTOON = '动画','动画'
    HOMELY = '家庭','家庭'
    FANTASTIC = '奇幻','奇幻'
    GHOST = '魔幻','魔幻'
    FANTACY = '科幻','科幻'
    WAR = '战争','战争'
    YOUTH = '青春','青春'

class TVSeries(models.Model):
    '''电视连续剧'''
    id = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    tv_name = models.CharField(max_length=128,verbose_name='名称')
    tv_country = models.CharField(max_length=36,choices=CountryCode.choices,default=CountryCode.ZH,verbose_name='区域')
    tv_mtype = models.CharField(max_length=24,choices=VideoType.choices,default=VideoType.COMEDY,verbose_name='影片类型') #影片类型
    tv_description = models.TextField(verbose_name='简介')

    def __str__(self) -> str:
        return self.tv_name

    def description(self):
        if len(self.tv_description) > 48:
            return '{}....'.format(self.tv_description[0:44])
        else:
            return self.tv_description

    class Meta:
        verbose_name = '电视连续剧'
        verbose_name_plural = '电视连续剧'


class Episode(models.Model):
    '''剧集'''
    id = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    tv_id = models.ForeignKey(TVSeries,on_delete=models.CASCADE,to_field='id',verbose_name='电视剧')
    e_title = models.CharField(max_length=256,verbose_name='名称')
    e_url = models.CharField(max_length=256,verbose_name='播放链接')

    def __str__(self) -> str:
        return self.e_title

    class Meta:
        verbose_name = '剧集'
        verbose_name_plural = '剧集'

class Movie(models.Model):
    '''电影'''
    id = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    mv_name = models.CharField(max_length=128,verbose_name='名称')
    mv_country = models.CharField(max_length=36,choices=CountryCode.choices,default=CountryCode.ZH,verbose_name='区域')
    mv_mtype = models.CharField(max_length=24,choices=VideoType.choices,default=VideoType.COMEDY,verbose_name='影片类型') #影片类型
    mv_url = models.CharField(max_length=256,default='',verbose_name='播放链接')
    mv_description = models.TextField(verbose_name='简介')

    def __str__(self) -> str:
        return self.mv_name

    def description(self):
        if len(self.mv_description) > 48:
            return '{}....'.format(self.mv_description[0:44])
        else:
            return self.mv_description

    description.allow_tags = True

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'

class VideoParser(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    name = models.CharField(max_length=36,verbose_name='名称')
    p_url = models.CharField(max_length=128,verbose_name='链接地址')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = '视频解析器'
        verbose_name_plural = '视频解析器'

class MovieSeries(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True,editable=False)
    name = models.CharField(max_length=64,verbose_name='名称')
    create_date = models.DateField(verbose_name='创建时间')
    movies = models.ManyToManyField(Movie,verbose_name='电影集')

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = '电影系列'
        verbose_name_plural = '电影系列'

