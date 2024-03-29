# Generated by Django 3.2.5 on 2021-07-26 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateField()),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone4.listing')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('town', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='milestone4.user')),
                ('purchases', models.IntegerField()),
            ],
            bases=('milestone4.user',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('sale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='milestone4.sale')),
                ('rating_date', models.DateField()),
                ('score', models.IntegerField()),
            ],
            bases=('milestone4.sale',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='milestone4.user')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sales', models.IntegerField()),
            ],
            bases=('milestone4.user',),
        ),
        migrations.AddField(
            model_name='sale',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone4.buyer'),
        ),
        migrations.AddField(
            model_name='sale',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone4.seller'),
        ),
        migrations.AddField(
            model_name='listing',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestone4.seller'),
        ),
    ]
