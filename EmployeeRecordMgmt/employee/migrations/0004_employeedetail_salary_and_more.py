# Generated by Django 5.2 on 2025-04-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employeecurrentworkdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='EmployeeCurrentWorkDetail',
        ),
    ]
