# Generated by Django 4.2.4 on 2023-08-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instantMessages', '0004_userdeletedconversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreatedconversation',
            name='event',
            field=models.CharField(default='userCreatedConversation', max_length=100),
        ),
    ]
