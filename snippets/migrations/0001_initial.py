# Generated by Django 5.1.3 on 2024-11-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('abap', 'abap'), ('algol', 'algol'), ('algol_nu', 'algol_nu'), ('arduino', 'arduino'), ('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('coffee', 'coffee'), ('colorful', 'colorful'), ('default', 'default'), ('dracula', 'dracula'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('friendly_grayscale', 'friendly_grayscale'), ('fruity', 'fruity'), ('github-dark', 'github-dark'), ('gruvbox-dark', 'gruvbox-dark'), ('gruvbox-light', 'gruvbox-light'), ('igor', 'igor'), ('inkpot', 'inkpot'), ('lightbulb', 'lightbulb'), ('lilypond', 'lilypond'), ('lovelace', 'lovelace'), ('manni', 'manni'), ('material', 'material'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('nord', 'nord'), ('nord-darker', 'nord-darker'), ('one-dark', 'one-dark'), ('paraiso-dark', 'paraiso-dark'), ('paraiso-light', 'paraiso-light'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rainbow_dash', 'rainbow_dash'), ('rrt', 'rrt'), ('sas', 'sas'), ('solarized-dark', 'solarized-dark'), ('solarized-light', 'solarized-light'), ('staroffice', 'staroffice'), ('stata-dark', 'stata-dark'), ('stata-light', 'stata-light'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs'), ('xcode', 'xcode'), ('zenburn', 'zenburn')], default='friendly', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
