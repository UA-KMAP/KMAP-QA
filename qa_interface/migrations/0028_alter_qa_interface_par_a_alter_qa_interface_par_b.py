# Generated by Django 4.1.2 on 2023-03-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0027_alter_qa_interface_par_a_alter_qa_interface_par_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='par_A',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='qa_interface',
            name='par_B',
            field=models.TextField(),
        ),
    ]