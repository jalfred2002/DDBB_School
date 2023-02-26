# Generated by Django 4.1.7 on 2023-02-26 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_representative_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.RemoveField(
            model_name='student',
            name='representative',
        ),
        migrations.AddField(
            model_name='student',
            name='representative',
            field=models.ManyToManyField(to='app.representative'),
        ),
    ]