# Generated by Django 2.2.9 on 2022-05-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220527_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': (['-pub_date'],), 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='posts.Group', verbose_name='Сообщество'),
        ),
    ]
