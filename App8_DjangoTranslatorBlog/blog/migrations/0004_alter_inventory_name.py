# Generated by Django 4.0.1 on 2022-03-09 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_inventory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.item'),
        ),
    ]
