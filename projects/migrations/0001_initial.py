# Generated by Django 2.0.1 on 2018-07-30 09:57

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('creator', models.CharField(max_length=300)),
                ('year', models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018, verbose_name='År')),
                ('semester', models.CharField(choices=[('H', 'Høst'), ('V', 'Vår')], default='H', max_length=2)),
                ('course', models.CharField(max_length=150)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='projects/')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=60)),
            ],
            options={
                'verbose_name': 'Prosjekt',
                'verbose_name_plural': 'Prosjekter',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='styremedlem/')),
            ],
        ),
    ]
