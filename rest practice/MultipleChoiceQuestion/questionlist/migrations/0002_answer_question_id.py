# Generated by Django 3.1.7 on 2021-02-21 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionlist.question'),
            preserve_default=False,
        ),
    ]