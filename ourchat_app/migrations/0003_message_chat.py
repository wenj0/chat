# Generated by Django 3.1.1 on 2020-10-03 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourchat_app', '0002_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ourchat_app.chat'),
        ),
    ]
