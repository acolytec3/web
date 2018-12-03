# Generated by Django 2.0.6 on 2018-06-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0085_tokenapproval'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='admin_mark_as_remarket_ready',
            field=models.BooleanField(default=False, help_text='Admin override to mark as remarketing ready'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='admin_override_suspend_auto_approval',
            field=models.BooleanField(default=False, help_text='Admin override to suspend work auto approvals'),
        ),
    ]