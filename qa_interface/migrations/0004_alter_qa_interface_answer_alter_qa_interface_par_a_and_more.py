# Generated by Django 4.1.2 on 2022-10-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa_interface", "0003_alter_qa_interface_answer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qa_interface",
            name="answer",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="qa_interface", name="par_A", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="qa_interface", name="par_B", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="qa_interface",
            name="question",
            field=models.CharField(max_length=100),
        ),
    ]
