# Generated by Django 4.0.3 on 2023-07-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0003_alter_salesperson_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesperson',
            name='employee_id',
            field=models.CharField(max_length=150),
        ),
    ]