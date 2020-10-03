# Generated by Django 3.1.1 on 2020-10-03 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ourchat_app', '0003_message_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[[16, 'Создатель чата'], [1, 'Участник чата']], default=16)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourchat_app.chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
