# Generated by Django 3.0 on 2020-10-12 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competency', '0002_auto_20201012_1603'),
        ('environment', '0002_auto_20190520_0649'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('course_code', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(null=True)),
                ('overview', models.TextField(null=True)),
                ('target_audience', models.TextField(null=True)),
                ('objectives', models.TextField(null=True)),
                ('competencies', models.ManyToManyField(related_name='course_relations', to='competency.Competency')),
                ('environment', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='course_relation', to='environment.Environment')),
                ('groups', models.ManyToManyField(related_name='course_relations', to='group.Group')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'db_table': 'course_competency_recommendation_system_course',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('environment', 'name')},
            },
        ),
    ]