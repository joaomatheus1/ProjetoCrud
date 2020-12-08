# Generated by Django 3.1.2 on 2020-11-19 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('wom_code', models.CharField(max_length=3)),
                ('descricao', models.TextField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='woman_register.position')),
            ],
        ),
    ]