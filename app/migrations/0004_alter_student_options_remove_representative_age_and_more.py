# Generated by Django 4.1.7 on 2023-02-26 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_representative_user_id_student_birth_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RemoveField(
            model_name='representative',
            name='age',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='name',
        ),
        migrations.AlterModelTable(
            name='student',
            table=None,
        ),
    ]
