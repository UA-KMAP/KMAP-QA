# Generated by Django 4.1.2 on 2023-02-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0016_alter_qa_interface_supporting_facts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='supporting_facts',
            field=models.TextField(help_text=' &nbsp; <button type="button" class="btn btn-info" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="right" data-bs-content="Supporting facts indicates sentences involved while creating the multi hop question from both of the paragraphs..."> ? </button>', max_length=4),
        ),
    ]
