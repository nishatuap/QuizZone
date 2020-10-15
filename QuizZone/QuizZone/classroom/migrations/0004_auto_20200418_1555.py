from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20191008_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Question'),
        ),
    ]
