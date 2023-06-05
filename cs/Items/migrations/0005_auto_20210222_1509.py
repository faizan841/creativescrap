# Generated by Django 3.1.4 on 2021-02-22 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Items', '0004_auto_20210220_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_scrapitems',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='seller_id', to='Authentication.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_scrapitems',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_username', to='Authentication.user'),
            preserve_default=False,
        ),
    ]
