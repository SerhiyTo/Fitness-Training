# Generated by Django 5.0.4 on 2024-05-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portionfood',
            name='food_item',
        ),
        migrations.AddField(
            model_name='portionfood',
            name='food_item',
            field=models.ManyToManyField(related_name='portions', to='diet.fooditem'),
        ),
    ]
