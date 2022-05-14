# Generated by Django 4.0.4 on 2022-05-14 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labattendance',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='qualification',
        ),
        migrations.AddField(
            model_name='qualification',
            name='for_who',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Staff.qualification'),
        ),
    ]
