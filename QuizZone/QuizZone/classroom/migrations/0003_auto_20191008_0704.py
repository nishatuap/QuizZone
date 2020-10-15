from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='takenquiz',
            name='percentage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='takenquiz',
            name='score',
            field=models.IntegerField(),
        ),
    ]
