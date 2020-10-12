# Generated by Django 3.0 on 2020-10-12 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0002_auto_20190520_0649'),
        ('competency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetencyCorrelation',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('correlation', models.FloatField(null=True)),
                ('competency1', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='competencycorrelation_relation1', to='competency.Competency')),
                ('competency2', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='competencycorrelation_relation2', to='competency.Competency')),
                ('environment', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='competencycorrelation_relation', to='environment.Environment')),
            ],
            options={
                'verbose_name': 'competency correlation',
                'verbose_name_plural': 'competency correlations',
                'db_table': 'course_competency_recommendation_system_competency_correlation',
                'ordering': ['-correlation'],
                'abstract': False,
                'unique_together': {('competency1', 'competency2')},
            },
        ),
    ]
