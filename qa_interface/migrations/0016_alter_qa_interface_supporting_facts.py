# Generated by Django 4.1.2 on 2023-02-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_interface', '0015_alter_qa_interface_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa_interface',
            name='supporting_facts',
            field=models.TextField(help_text='<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" title="Popover title" data-bs-content="And here is some amazing content. It is very engaging. Right?">?</button>', max_length=4),
        ),
    ]
