# Generated by Django 4.1.7 on 2023-02-26 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('professor_ids', models.ManyToManyField(through='app.Section', to='app.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('birth', models.DateField(blank=True, null=True)),
                ('representative_ids', models.ManyToManyField(to='app.representative')),
                ('section_ids', models.ManyToManyField(through='app.Inscription', to='app.section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.section'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
