# Generated by Django 3.1.2 on 2020-10-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201014_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.programme'),
        ),
    ]