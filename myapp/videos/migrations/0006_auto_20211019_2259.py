# Generated by Django 3.2.8 on 2021-10-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_movie_mv_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'verbose_name': '剧集', 'verbose_name_plural': '剧集'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': '电影', 'verbose_name_plural': '电影'},
        ),
        migrations.AlterModelOptions(
            name='tvseries',
            options={'verbose_name': '电视连续剧', 'verbose_name_plural': '电视连续剧'},
        ),
        migrations.AlterModelOptions(
            name='videoparser',
            options={'verbose_name': '视频解析器', 'verbose_name_plural': '视频解析器'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='mv_country',
            field=models.CharField(choices=[('华语', '华语'), ('香港地区', '香港地区'), ('美国', '美国'), ('欧洲', '欧洲'), ('韩国', '韩国'), ('日本', '日本'), ('泰国', '泰国'), ('印度', '印度'), ('其它', '其它')], default='华语', max_length=36, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mv_mtype',
            field=models.CharField(choices=[('喜剧', '喜剧'), ('爱情', '爱情'), ('动作', '动作'), ('枪战', '枪战'), ('犯罪', '犯罪'), ('惊悚', '惊悚'), ('恐怖', '恐怖'), ('悬疑', '悬疑'), ('动画', '动画'), ('家庭', '家庭'), ('奇幻', '奇幻'), ('魔幻', '魔幻'), ('科幻', '科幻'), ('战争', '战争'), ('青春', '青春')], default='喜剧', max_length=24, verbose_name='影片类型'),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='tv_country',
            field=models.CharField(choices=[('华语', '华语'), ('香港地区', '香港地区'), ('美国', '美国'), ('欧洲', '欧洲'), ('韩国', '韩国'), ('日本', '日本'), ('泰国', '泰国'), ('印度', '印度'), ('其它', '其它')], default='华语', max_length=36, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='tv_mtype',
            field=models.CharField(choices=[('喜剧', '喜剧'), ('爱情', '爱情'), ('动作', '动作'), ('枪战', '枪战'), ('犯罪', '犯罪'), ('惊悚', '惊悚'), ('恐怖', '恐怖'), ('悬疑', '悬疑'), ('动画', '动画'), ('家庭', '家庭'), ('奇幻', '奇幻'), ('魔幻', '魔幻'), ('科幻', '科幻'), ('战争', '战争'), ('青春', '青春')], default='喜剧', max_length=24, verbose_name='影片类型'),
        ),
        migrations.CreateModel(
            name='MovieSeries',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('create_date', models.DateField(verbose_name='创建时间')),
                ('movies', models.ManyToManyField(to='videos.Movie')),
            ],
            options={
                'verbose_name': '电影系列',
                'verbose_name_plural': '电影系列',
            },
        ),
    ]
