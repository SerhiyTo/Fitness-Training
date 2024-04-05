# Generated by Django 5.0.3 on 2024-04-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name": "Profile", "verbose_name_plural": "Profiles"},
        ),
        migrations.AlterField(
            model_name="coachprofile",
            name="experience",
            field=models.IntegerField(verbose_name="Coach experience"),
        ),
        migrations.AlterField(
            model_name="coachprofile",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Coach price"),
        ),
        migrations.AlterField(
            model_name="coachprofile",
            name="rating",
            field=models.FloatField(verbose_name="Coach rating"),
        ),
        migrations.AlterField(
            model_name="coachprofile",
            name="specialization",
            field=models.CharField(max_length=100, verbose_name="Coach specialization"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(null=True, verbose_name="User birthdate"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="User email"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(max_length=20, null=True, verbose_name="User phone"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="height",
            field=models.FloatField(verbose_name="User height"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="weight",
            field=models.FloatField(verbose_name="User weight"),
        ),
    ]
