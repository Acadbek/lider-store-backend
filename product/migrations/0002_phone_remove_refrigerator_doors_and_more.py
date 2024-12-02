# Generated by Django 4.2.16 on 2024-12-02 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('os_version', models.CharField(default='Android 14', max_length=50, verbose_name='Operatsion tizim versiyasi')),
                ('body_material', models.CharField(default='plastik', max_length=50, verbose_name='Korpus materiali')),
                ('sim_card_type', models.CharField(default='2 (Nano Sim)', max_length=50, verbose_name='SIM karta turi')),
                ('sim_card_count', models.IntegerField(default=2, verbose_name='SIM kartalar soni')),
                ('display_technology', models.CharField(default='Super AMOLED', max_length=50, verbose_name='Displey texnologiyasi')),
                ('display_size', models.DecimalField(decimal_places=1, default=6.7, max_digits=3, verbose_name='Displey o‘lchami, dyuym')),
                ('screen_resolution', models.CharField(default='1080 x 2340', max_length=20, verbose_name='Ekran ruxsati, px')),
                ('refresh_rate', models.IntegerField(default=90, verbose_name='Yangilanish chastotasi, Gts')),
                ('processor', models.CharField(default='MediaTek Helio G99', max_length=100, verbose_name='Protsessor')),
                ('ram', models.IntegerField(default=8, verbose_name='Operativ xotira (RAM), GB')),
                ('rom', models.IntegerField(default=256, verbose_name='Ichki xotira (ROM), GB')),
                ('main_camera', models.IntegerField(default=50, verbose_name='Asosiy kamera, MP')),
                ('front_camera', models.IntegerField(default=13, verbose_name='Old kamera, MP')),
            ],
            bases=('product.product',),
        ),
        migrations.RemoveField(
            model_name='refrigerator',
            name='doors',
        ),
        migrations.RemoveField(
            model_name='refrigerator',
            name='freezer_defrosting',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='resolution',
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='doors_count',
            field=models.IntegerField(default=2, verbose_name='Eshiklar soni'),
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='freezer_defrost',
            field=models.CharField(default="kapel'na", max_length=50, verbose_name='Muzlatkichni eritish turi'),
        ),
        migrations.AddField(
            model_name='tv',
            name='screen_resolution',
            field=models.CharField(default='Full HD, 1920x1080', max_length=20, verbose_name='Ekran ruxsati, px'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='color',
            field=models.CharField(default='oq', max_length=20, verbose_name='Rangi'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='dimensions',
            field=models.CharField(default='550x575x1441', max_length=50, verbose_name='O‘lchamlari (E x G x B)'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='door_shelves',
            field=models.IntegerField(default=4, verbose_name='Eshik tokchalar soni'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='energy_class',
            field=models.CharField(default='A+', max_length=10, verbose_name='Energiya samaradorligi sinfi'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='freezer_volume',
            field=models.IntegerField(default=50, verbose_name='Muzlatkich kamerasi hajmi, l'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='fridge_volume',
            field=models.IntegerField(default=175, verbose_name='Sovutgich kamerasi hajmi, l'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='lighting',
            field=models.CharField(default='LED lampha', max_length=50, verbose_name='Sovutgich kamerasi yoritilishi'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='noise_level',
            field=models.IntegerField(default=41, verbose_name='Shovqin darajasi, dB'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='refrigerant',
            field=models.CharField(default='R600a', max_length=50, verbose_name='Sovutuvchi moddasi'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='total_volume',
            field=models.IntegerField(default=225, verbose_name='Umumiy hajm, l'),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=47, max_digits=5, verbose_name='Og‘irligi, kg'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='control_type',
            field=models.CharField(default='Ovozli boshqaruv', max_length=50, verbose_name='Boshqarish turi'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='os_version',
            field=models.CharField(default='Android 10', max_length=50, verbose_name='Operatsion tizim versiyasi'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='refresh_rate',
            field=models.IntegerField(default=60, verbose_name='Ekran yangilanish chastotasi, Gts'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='screen_format',
            field=models.CharField(default='16:9', max_length=10, verbose_name='Ekran formati'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='screen_size',
            field=models.DecimalField(decimal_places=1, default=43, max_digits=4, verbose_name='Ekran diagonali, dyuym'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='smart_tv_support',
            field=models.BooleanField(default=True, verbose_name='Smart TV qo‘llab-quvvatlash'),
        ),
        migrations.AlterField(
            model_name='tv',
            name='sound_system',
            field=models.CharField(default='2 dinamik', max_length=50, verbose_name='Ovoz tizimi'),
        ),
    ]