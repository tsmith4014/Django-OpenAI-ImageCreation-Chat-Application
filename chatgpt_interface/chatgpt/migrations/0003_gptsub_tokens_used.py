# Generated by Django 4.1.5 on 2023-05-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatgpt", "0002_remove_gptsub_num_tokens_alter_gptsub_response"),
    ]

    operations = [
        migrations.AddField(
            model_name="gptsub",
            name="tokens_used",
            field=models.IntegerField(null=True),
        ),
    ]
