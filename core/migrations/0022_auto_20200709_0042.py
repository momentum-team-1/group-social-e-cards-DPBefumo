# Generated by Django 3.0.7 on 2020-07-09 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_auto_20200707_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL),
        ),
    ]