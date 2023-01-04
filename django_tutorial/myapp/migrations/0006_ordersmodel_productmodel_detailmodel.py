# Generated by Django 4.1.2 on 2022-12-26 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_product_product_price_alter_product_product_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrdersModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subtotal", models.IntegerField(default=0)),
                ("shipping", models.IntegerField(default=0)),
                ("grandtotal", models.IntegerField(default=0)),
                ("customname", models.CharField(default="", max_length=100)),
                ("customemail", models.CharField(default="", max_length=100)),
                ("customaddress", models.CharField(default="", max_length=100)),
                ("customphone", models.CharField(default="", max_length=100)),
                ("paytype", models.CharField(default="", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pname", models.CharField(default="", max_length=100)),
                ("pprice", models.IntegerField(default=0)),
                ("pimages", models.CharField(default="", max_length=100)),
                ("pdescription", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.CreateModel(
            name="DetailModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pname", models.CharField(default="", max_length=100)),
                ("unitprice", models.IntegerField(default=0)),
                ("quantity", models.IntegerField(default=0)),
                ("dtotal", models.IntegerField(default=0)),
                (
                    "dorder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.ordersmodel",
                    ),
                ),
            ],
        ),
    ]
