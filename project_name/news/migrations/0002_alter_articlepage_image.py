from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="image",
            field=wagtail.fields.StreamField(
                [("image", None)],
                blank=True,
                max_num=1,
            ),
        ),
    ]
