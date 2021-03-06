# Generated by Django 3.0 on 2020-10-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('definition', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'competency',
                'verbose_name_plural': 'competencies',
                'db_table': 'course_competency_recommendation_system_competency',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
