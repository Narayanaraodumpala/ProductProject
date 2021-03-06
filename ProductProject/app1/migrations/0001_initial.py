# Generated by Django 3.0 on 2020-09-16 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('product', models.ManyToManyField(to='app1.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('statte', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User')),
            ],
        ),
    ]
