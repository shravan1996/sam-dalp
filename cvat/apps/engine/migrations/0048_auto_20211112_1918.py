# Generated by Django 3.2.8 on 2021-11-12 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0047_auto_20211110_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='resolved_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='jobcommit',
            old_name='author',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='resolver',
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='engine.issue'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='engine.job'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
