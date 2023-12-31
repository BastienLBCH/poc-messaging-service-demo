# Generated by Django 4.2.4 on 2023-08-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instantMessages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddedParticipantToConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('participant_id', models.CharField(max_length=100)),
                ('conversation_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
