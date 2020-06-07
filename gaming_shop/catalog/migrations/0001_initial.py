# Generated by Django 3.0.6 on 2020-05-16 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sensor', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=50, verbose_name='DPI presets')),
                ('speed', models.CharField(max_length=50)),
                ('switch', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('brend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Brend')),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('key_switch', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('light_effects', models.CharField(max_length=200)),
                ('lifespan', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('brend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Brend')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('frequency_headphone', models.CharField(max_length=30)),
                ('impedance', models.CharField(max_length=10)),
                ('driver', models.CharField(max_length=50)),
                ('frequency_microphone', models.CharField(max_length=30)),
                ('sensitivity', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('brend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Brend')),
            ],
        ),
    ]
