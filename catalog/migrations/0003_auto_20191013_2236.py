# Generated by Django 2.2.4 on 2019-10-13 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191008_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('Set book as returned', 'can_mark_returned'),)},
        ),
    ]