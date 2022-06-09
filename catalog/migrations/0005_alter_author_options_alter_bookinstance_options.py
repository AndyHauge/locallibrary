# Generated by Django 4.0.4 on 2022-05-11 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
