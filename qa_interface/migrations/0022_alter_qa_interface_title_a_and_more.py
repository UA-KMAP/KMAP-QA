# Generated by Django 4.1.2 on 2023-02-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0021_alter_qa_interface_title_a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='title_A',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='qa_interface',
            name='title_B',
            field=models.CharField(max_length=35),
        ),
    ]