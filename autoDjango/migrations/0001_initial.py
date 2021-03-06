# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name=b'username')),
                ('qq', models.CharField(max_length=10, null=True, verbose_name=b'QQ')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name=b'Phone Number')),
                ('department', models.CharField(max_length=20, null=True, verbose_name=b'Department')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name=b'Email Address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20, verbose_name='\u5173\u952e\u5b57')),
                ('element', models.CharField(max_length=10, null=True, verbose_name='\u5143\u7d20\u8868ID')),
                ('value', models.CharField(max_length=100, verbose_name='\u8f93\u5165\u503c')),
                ('desc', models.CharField(max_length=200, verbose_name='\u6b65\u9aa4\u8bf4\u660e')),
            ],
            options={
                'db_table': 'CaseStep',
                'verbose_name': '\u7528\u4f8b\u6b65\u9aa4\u8868',
                'verbose_name_plural': '\u7528\u4f8b\u6b65\u9aa4\u8868',
            },
        ),
        migrations.CreateModel(
            name='DateBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('host', models.CharField(max_length=20, verbose_name='IP/\u57df\u540d')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('port', models.CharField(max_length=4, verbose_name='\u7aef\u53e3')),
                ('db', models.CharField(max_length=50, verbose_name='\u6570\u636e\u5e93')),
            ],
            options={
                'db_table': 'DateBase',
                'verbose_name': '\u6570\u636e\u5e93\u8868',
                'verbose_name_plural': '\u6570\u636e\u5e93\u8868',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('desc', models.CharField(max_length=200, verbose_name='\u8bf4\u660e')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'Element',
                'verbose_name': '\u5143\u7d20\u8868',
                'verbose_name_plural': '\u5143\u7d20\u8868',
            },
        ),
        migrations.CreateModel(
            name='ElementContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10, verbose_name='\u5b9a\u4f4d\u65b9\u5f0f')),
                ('content', models.CharField(max_length=100, verbose_name='\u5b9a\u4f4d\u503c')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.Element', verbose_name='\u5143\u7d20ID')),
            ],
            options={
                'db_table': 'ElementContent',
                'verbose_name': '\u5143\u7d20\u5185\u5bb9\u8868',
                'verbose_name_plural': '\u5143\u7d20\u5185\u5bb9\u8868',
            },
        ),
        migrations.CreateModel(
            name='FindMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10, verbose_name='\u5b9a\u4f4d\u65b9\u5f0f')),
                ('display', models.CharField(max_length=10, verbose_name='\u663e\u793a\u540d\u79f0')),
            ],
            options={
                'db_table': 'FindMethod',
                'verbose_name': '\u5b9a\u4f4d\u65b9\u5f0f\u8868',
                'verbose_name_plural': '\u5b9a\u4f4d\u65b9\u5f0f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5173\u952e\u5b57')),
                ('display_name', models.CharField(max_length=50, verbose_name='\u663e\u793a\u7684\u5173\u952e\u5b57')),
            ],
            options={
                'db_table': 'keyword',
                'verbose_name': '\u5173\u952e\u5b57\u8868',
                'verbose_name_plural': '\u5173\u952e\u5b57\u8868',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('address', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('desc', models.CharField(max_length=200, verbose_name='\u8bf4\u660e')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.DateBase', verbose_name='\u6570\u636e\u5e93ID')),
            ],
            options={
                'db_table': 'Project',
                'verbose_name': '\u9879\u76ee\u8868',
                'verbose_name_plural': '\u9879\u76ee\u8868',
            },
        ),
        migrations.CreateModel(
            name='ScenarioContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=5, verbose_name='\u7528\u4f8bID')),
            ],
            options={
                'db_table': 'ScenarioContent',
                'verbose_name': '\u573a\u666f\u7528\u4f8b\u8868',
                'verbose_name_plural': '\u573a\u666f\u7528\u4f8b\u8868',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7528\u4f8b\u540d\u79f0')),
                ('nature', models.CharField(max_length=50, verbose_name='\u7528\u4f8b\u6027\u8d28')),
                ('status', models.CharField(max_length=20, verbose_name='\u7528\u4f8b\u72b6\u6001')),
                ('level', models.CharField(max_length=5, null=True, verbose_name='\u7528\u4f8b\u7b49\u7ea7')),
                ('create_at', models.DateField(auto_now_add=True, null=True)),
                ('update_at', models.DateField(auto_now=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.Project', verbose_name='\u9879\u76eeID')),
            ],
            options={
                'db_table': 'TestCase',
                'verbose_name': '\u6d4b\u8bd5\u7528\u4f8b\u8868',
                'verbose_name_plural': '\u6d4b\u8bd5\u7528\u4f8b\u8868',
            },
        ),
        migrations.CreateModel(
            name='TestScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('status', models.CharField(max_length=10, verbose_name='\u72b6\u6001')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.Project', verbose_name='\u9879\u76eeID')),
            ],
            options={
                'db_table': 'TestScenario',
                'verbose_name': '\u6d4b\u8bd5\u573a\u666f\u8868',
                'verbose_name_plural': '\u6d4b\u8bd5\u573a\u666f\u8868',
            },
        ),
        migrations.AddField(
            model_name='scenariocontent',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.TestScenario', verbose_name='\u573a\u666fID'),
        ),
        migrations.AddField(
            model_name='element',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.Project', verbose_name='\u9879\u76eeID'),
        ),
        migrations.AddField(
            model_name='casestep',
            name='testcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoDjango.TestCase', verbose_name='\u7528\u4f8bID'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autoDjango.Project', verbose_name=b'Project'),
        ),
    ]
