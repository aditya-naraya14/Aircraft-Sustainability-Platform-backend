# Generated by Django 4.2.1 on 2023-05-13 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aircraft", "0008_partdetails_life_cycle_assesment_score_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="part",
            name="part_detail_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="part_details",
                to="aircraft.partdetails",
            ),
        ),
    ]
