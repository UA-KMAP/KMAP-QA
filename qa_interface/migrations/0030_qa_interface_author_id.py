# Generated by Django 4.1.2 on 2023-03-05 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0029_qa_interface_par_a_raw_qa_interface_par_b_raw'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa_interface',
            name='author_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
