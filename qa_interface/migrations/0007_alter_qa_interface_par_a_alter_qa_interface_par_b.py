# Generated by Django 4.1.2 on 2022-11-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa_interface", "0006_qa_interface_source_id_alter_qa_interface_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qa_interface",
            name="par_A",
            field=models.TextField(default="nroberts"),
        ),
        migrations.AlterField(
            model_name="qa_interface",
            name="par_B",
            field=models.TextField(default="nroberts"),
        ),
    ]
