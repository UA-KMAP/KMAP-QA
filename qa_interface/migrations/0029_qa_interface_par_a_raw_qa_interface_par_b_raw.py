# Generated by Django 4.1.2 on 2023-03-05 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0028_alter_qa_interface_par_a_alter_qa_interface_par_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa_interface',
            name='par_A_Raw',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qa_interface',
            name='par_B_Raw',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
