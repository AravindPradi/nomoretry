# Generated by Django 3.1.1 on 2020-09-21 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.branch')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.college')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.college'),
        ),
    ]