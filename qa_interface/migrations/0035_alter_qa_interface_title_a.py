# Generated by Django 4.1.2 on 2023-06-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0034_alter_qa_interface_title_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='title_A',
            field=models.CharField(max_length=35),
        ),
    ]
