# Generated by Django 4.1.2 on 2023-02-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0018_qa_interface_title_a_qa_interface_title_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='title_A',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='qa_interface',
            name='title_B',
            field=models.CharField(max_length=25),
        ),
    ]
