# Generated by Django 4.1.5 on 2023-01-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_cropdisease_disease_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cropdisease",
            name="disease_name",
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
