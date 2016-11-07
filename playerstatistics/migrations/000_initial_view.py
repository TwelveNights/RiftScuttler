from django.db import migrations

from common import utils


class Migration(migrations.Migration):

    dependencies = []

    operations = []

    utils.set_operations(operations, "playerstatistics", "000_create_views")
