# Generated by Django 4.1 on 2024-11-18 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(max_length=250, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('offer', models.BooleanField(default=False, null=True)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo_list.category')),
            ],
        ),
    ]
