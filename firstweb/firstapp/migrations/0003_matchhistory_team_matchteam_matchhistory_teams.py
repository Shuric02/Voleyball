# Generated by Django 4.2.14 on 2024-08-31 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_сoefficientsofcharacteristics_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('players', models.ManyToManyField(to='firstapp.players')),
            ],
        ),
        migrations.CreateModel(
            name='MatchTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.matchhistory')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.team')),
            ],
        ),
        migrations.AddField(
            model_name='matchhistory',
            name='teams',
            field=models.ManyToManyField(through='firstapp.MatchTeam', to='firstapp.team'),
        ),
    ]
