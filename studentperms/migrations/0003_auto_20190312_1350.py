# Generated by Django 2.1.7 on 2019-03-12 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("studentperms", "0002_auto_20190213_1126")]

    operations = [
        migrations.AlterField(
            model_name="permission",
            name="dept_head",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"flags__slug": "instructor"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="permissions_granted_as_head",
                to="people.Person",
                verbose_name="Department head or designate",
            ),
        ),
        migrations.AlterField(
            model_name="permission",
            name="dept_head_signed",
            field=models.DateField(
                blank=True, null=True, verbose_name="Department head signed on"
            ),
        ),
        migrations.AlterField(
            model_name="permission",
            name="instructor_signed",
            field=models.DateField(
                blank=True, null=True, verbose_name="Instructor signed on"
            ),
        ),
    ]
