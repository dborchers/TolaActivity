# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0006_formguidance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formenabled',
            name='agreement',
        ),
        migrations.RemoveField(
            model_name='formenabled',
            name='country',
        ),
        migrations.RemoveField(
            model_name='formenabled',
            name='form',
        ),
        migrations.AlterModelOptions(
            name='documentationapp',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='projectagreement',
            options={'ordering': ('project_name',), 'permissions': (('can_approve', 'Can approve initiation'),), 'verbose_name_plural': 'Project Initiation'},
        ),
        migrations.AlterModelOptions(
            name='projectcomplete',
            options={'ordering': ('project_name',), 'verbose_name_plural': 'Project Tracking'},
        ),
        migrations.AlterField(
            model_name='benchmarks',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.AlterField(
            model_name='historicalprojectcomplete',
            name='activity_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Code'),
        ),
        migrations.AlterField(
            model_name='historicalprojectcomplete',
            name='actual_start_date',
            field=models.DateTimeField(blank=True, help_text='Imported from Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectcomplete',
            name='expected_duration',
            field=models.CharField(blank=True, help_text='Imported from Project Initiation', max_length=255, null=True, verbose_name='Expected Duration'),
        ),
        migrations.AlterField(
            model_name='historicalprojectcomplete',
            name='expected_end_date',
            field=models.DateTimeField(blank=True, help_text='Imported Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectcomplete',
            name='expected_start_date',
            field=models.DateTimeField(blank=True, help_text='Imported from Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='activity_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Code'),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='actual_start_date',
            field=models.DateTimeField(blank=True, help_text='Imported from Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='expected_duration',
            field=models.CharField(blank=True, help_text='Imported from Project Initiation', max_length=255, null=True, verbose_name='Expected Duration'),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='expected_end_date',
            field=models.DateTimeField(blank=True, help_text='Imported Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='expected_start_date',
            field=models.DateTimeField(blank=True, help_text='Imported from Project Initiation', null=True),
        ),
        migrations.AlterField(
            model_name='projectcomplete',
            name='project_agreement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.AlterField(
            model_name='trainingattendance',
            name='project_agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation'),
        ),
        migrations.DeleteModel(
            name='FormEnabled',
        ),
        migrations.DeleteModel(
            name='FormLibrary',
        ),
    ]