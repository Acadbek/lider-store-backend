# Generated by Django 4.2.16 on 2024-12-02 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_washingmachine_control_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirConditioner',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('power_index_btu', models.IntegerField(default=12, verbose_name='Indeks quvvati (BTU)')),
                ('recommended_area', models.CharField(choices=[('up_to_40', '40 m² gacha'), ('up_to_60', '60 m² gacha'), ('up_to_100', '100 m² gacha')], default='up_to_40', max_length=20, verbose_name='Tavsiya etilgan maydon (m²)')),
                ('compressor', models.CharField(default='invertor', max_length=50, verbose_name='Kompressor turi')),
                ('refrigerant', models.CharField(choices=[('r32', 'R32'), ('r410a', 'R410A'), ('r22', 'R22')], default='r32', max_length=10, verbose_name='Xladogent turi')),
                ('sku', models.CharField(default='8704', max_length=50, verbose_name='SKU')),
                ('installation_type', models.CharField(choices=[('wall_split', 'Devorga o‘rnatiladigan split tizimi'), ('floor_ceiling', 'Yerde yoki shiftga o‘rnatiladigan')], default='wall_split', max_length=50, verbose_name='O‘rnatish turi')),
                ('color', models.CharField(default='oq', max_length=50, verbose_name='Rang')),
                ('external_unit_weight', models.FloatField(default=12, verbose_name="Tashqi blok og'irligi (kg)")),
                ('internal_unit_weight', models.FloatField(default=9.5, verbose_name="Ichki blok og'irligi (kg)")),
                ('power_consumption_cooling', models.IntegerField(default=575, verbose_name="Sovutish rejimida iste'mol qilinadigan quvvat (W)")),
            ],
            bases=('product.product',),
        ),
    ]