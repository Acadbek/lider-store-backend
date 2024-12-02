from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mahsulot nomi")
    image = models.ImageField(upload_to='products/', verbose_name="Mahsulot rasmi")
    description = models.TextField(verbose_name="Mahsulot haqida batafsil")
    brand = models.CharField(max_length=100, verbose_name="Brand")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Narx")
    stock = models.PositiveIntegerField(verbose_name="Aksiya", null=True, blank=True)

    def __str__(self):
        return self.name


class Refrigerator(Product):
    noise_level = models.IntegerField(
        verbose_name="Shovqin darajasi, dB",
        default=41
    )
    total_volume = models.IntegerField(
        verbose_name="Umumiy hajm, l",
        default=225
    )
    fridge_volume = models.IntegerField(
        verbose_name="Sovutgich kamerasi hajmi, l",
        default=175
    )
    freezer_volume = models.IntegerField(
        verbose_name="Muzlatkich kamerasi hajmi, l",
        default=50
    )
    lighting = models.CharField(
        max_length=50,
        verbose_name="Sovutgich kamerasi yoritilishi",
        default="LED lampha"
    )
    door_shelves = models.IntegerField(
        verbose_name="Eshik tokchalar soni",
        default=4
    )
    doors_count = models.IntegerField(
        verbose_name="Eshiklar soni",
        default=2
    )
    energy_class = models.CharField(
        max_length=10,
        verbose_name="Energiya samaradorligi sinfi",
        default="A+"
    )
    freezer_defrost = models.CharField(
        max_length=50,
        verbose_name="Muzlatkichni eritish turi",
        default="kapel'na"
    )
    refrigerant = models.CharField(
        max_length=50,
        verbose_name="Sovutuvchi moddasi",
        default="R600a"
    )
    color = models.CharField(
        max_length=20,
        verbose_name="Rangi",
        default="oq"
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        verbose_name="Og‘irligi, kg",
        default=47
    )
    dimensions = models.CharField(
        max_length=50,
        verbose_name="O‘lchamlari (E x G x B)",
        default="550x575x1441"
    )

    def __str__(self):
        return self.name


class TV(Product):
    os_version = models.CharField(
        max_length=50,
        verbose_name="Operatsion tizim versiyasi",
        default="Android 10"
    )
    control_type = models.CharField(
        max_length=50,
        verbose_name="Boshqarish turi",
        default="Ovozli boshqaruv"
    )
    smart_tv_support = models.BooleanField(
        verbose_name="Smart TV qo‘llab-quvvatlash",
        default=True
    )
    screen_size = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name="Ekran diagonali, dyuym",
        default=43
    )
    screen_resolution = models.CharField(
        max_length=20,
        verbose_name="Ekran ruxsati, px",
        default="Full HD, 1920x1080"
    )
    refresh_rate = models.IntegerField(
        verbose_name="Ekran yangilanish chastotasi, Gts",
        default=60
    )
    screen_format = models.CharField(
        max_length=10,
        verbose_name="Ekran formati",
        default="16:9"
    )
    sound_system = models.CharField(
        max_length=50,
        verbose_name="Ovoz tizimi",
        default="2 dinamik"
    )

    def __str__(self):
        return self.name


class Phone(Product):
    os_version = models.CharField(
        max_length=50,
        verbose_name="Operatsion tizim versiyasi",
        default="Android 14"
    )
    body_material = models.CharField(
        max_length=50,
        verbose_name="Korpus materiali",
        default="plastik"
    )
    sim_card_type = models.CharField(
        max_length=50,
        verbose_name="SIM karta turi",
        default="2 (Nano Sim)"
    )
    sim_card_count = models.IntegerField(
        verbose_name="SIM kartalar soni",
        default=2
    )
    display_technology = models.CharField(
        max_length=50,
        verbose_name="Displey texnologiyasi",
        default="Super AMOLED"
    )
    display_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="Displey o‘lchami, dyuym",
        default=6.7
    )
    screen_resolution = models.CharField(
        max_length=20,
        verbose_name="Ekran ruxsati, px",
        default="1080 x 2340"
    )
    refresh_rate = models.IntegerField(
        verbose_name="Yangilanish chastotasi, Gts",
        default=90
    )
    processor = models.CharField(
        max_length=100,
        verbose_name="Protsessor",
        default="MediaTek Helio G99"
    )
    ram = models.IntegerField(
        verbose_name="Operativ xotira (RAM), GB",
        default=8
    )
    rom = models.IntegerField(
        verbose_name="Ichki xotira (ROM), GB",
        default=256
    )
    main_camera = models.IntegerField(
        verbose_name="Asosiy kamera, MP",
        default=50
    )
    front_camera = models.IntegerField(
        verbose_name="Old kamera, MP",
        default=13
    )

    def __str__(self):
        return self.name


class Laptop(Product):
    laptop_type = models.CharField(
        max_length=50,
        verbose_name="Noutbuk turi",
        default="Ofis"
    )
    os_version = models.CharField(
        max_length=50,
        verbose_name="Operatsion tizim",
        default="Windows"
    )
    display_technology = models.CharField(
        max_length=50,
        verbose_name="Displey texnologiyasi",
        default="IPS"
    )
    display_size = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name="Displey diagonali, dyuym",
        default=15.6
    )
    screen_resolution = models.CharField(
        max_length=50,
        verbose_name="Ekran ruxsati, px",
        default="1920 x 1080 Full HD"
    )
    processor = models.CharField(
        max_length=100,
        verbose_name="Protsessor",
        default="AMD Ryzen™ 5 7520U"
    )
    cores_count = models.IntegerField(
        verbose_name="Yadro soni",
        default=4
    )
    ram = models.IntegerField(
        verbose_name="Operativ xotira (RAM), GB",
        default=8
    )
    gpu_type = models.CharField(
        max_length=50,
        verbose_name="Videokarta turi",
        default="integratsiyalashgan"
    )
    gpu = models.CharField(
        max_length=100,
        verbose_name="Videokarta",
        default="AMD Radeon Graphics"
    )
    storage_type = models.CharField(
        max_length=50,
        verbose_name="Naychali xotira turi",
        default="SDD"
    )
    ssd_size = models.IntegerField(
        verbose_name="SSD xotira hajmi, GB",
        default=512
    )
    weight = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name="Og'irligi, kg",
        default=1.59
    )

    def __str__(self):
        return self.name


class WashingMachine(Product):
    WASH_TYPE_CHOICES = [
        ('automatic', 'Avtomatik'),
        ('semi_automatic', 'Yarim avtomatik'),
        ('manual', 'Qo‘lda boshqariladigan'),
    ]

    INSTALLATION_CHOICES = [
        ('built_in', 'O‘rnatilgan'),
        ('standalone', 'Mustaqil'),
    ]

    MOTOR_TYPE_CHOICES = [
        ('inverter', 'Invertorli'),
        ('universal', 'Universal'),
        ('brush', 'Cho‘tka motori'),
    ]

    LOADING_TYPE_CHOICES = [
        ('front', 'Oldindan yuklash'),
        ('top', 'Yuqa yuklash'),
    ]

    CONTROL_TYPE_CHOICES = [
        ('electronic', 'Elektron boshqaruv'),
        ('mechanical', 'Mexanik boshqaruv'),
        ('hybrid', 'Gibrid boshqaruv'),
    ]

    STEAM_TREATMENT_CHOICES = [
        ('yes', 'Bor'),
        ('no', 'Yo‘q'),
    ]

    wash_type = models.CharField(max_length=20, choices=WASH_TYPE_CHOICES, default='automatic',
                                 verbose_name="Yuvish turi")
    installation = models.CharField(max_length=20, choices=INSTALLATION_CHOICES, default='built_in',
                                    verbose_name="O‘rnatish turi")
    voltage = models.CharField(max_length=50, verbose_name="Kuchlanish (V)", default="220 V-240 V")
    motor_type = models.CharField(max_length=20, choices=MOTOR_TYPE_CHOICES, default='inverter',
                                  verbose_name="Motor turi")
    loading_type = models.CharField(max_length=20, choices=LOADING_TYPE_CHOICES, default='front',
                                    verbose_name="Yuklash turi")
    max_load = models.IntegerField(verbose_name="Maksimal yuklash (kg)", default=7)
    control_type = models.CharField(max_length=20, choices=CONTROL_TYPE_CHOICES, default='electronic',
                                    verbose_name="Boshqaruv turi")
    display = models.BooleanField(default=True, verbose_name="Displey")
    wash_efficiency = models.CharField(max_length=5, default="A+++", verbose_name="Yuvish samaradorligi sinfi")
    max_spin_speed = models.IntegerField(default=1200, verbose_name="Maksimal aylanish tezligi (ob/min)")
    steam_treatment = models.CharField(max_length=3, choices=STEAM_TREATMENT_CHOICES, default='yes',
                                       verbose_name="Bug bilan ishlov berish")
    color = models.CharField(max_length=50, default="kulrang", verbose_name="Rang")

    def __str__(self):
        return self.name


class AirConditioner(Product):
    RECOMMENDED_AREA_CHOICES = [
        ('up_to_40', '40 m² gacha'),
        ('up_to_60', '60 m² gacha'),
        ('up_to_100', '100 m² gacha'),
        # boshqa maydonlar qo'shish mumkin
    ]

    REFRIGERANT_CHOICES = [
        ('r32', 'R32'),
        ('r410a', 'R410A'),
        ('r22', 'R22'),
        # boshqa xladogentlar qo'shish mumkin
    ]

    INSTALLATION_CHOICES = [
        ('wall_split', 'Devorga o‘rnatiladigan split tizimi'),
        ('floor_ceiling', 'Yerde yoki shiftga o‘rnatiladigan'),
        # boshqa o‘rnatish variantlari qo‘shish mumkin
    ]
    power_index_btu = models.IntegerField(default=12, verbose_name="Indeks quvvati (BTU)")
    recommended_area = models.CharField(max_length=20, choices=RECOMMENDED_AREA_CHOICES, default='up_to_40', verbose_name="Tavsiya etilgan maydon (m²)")
    compressor = models.CharField(max_length=50, default="invertor", verbose_name="Kompressor turi")
    refrigerant = models.CharField(max_length=10, choices=REFRIGERANT_CHOICES, default='r32', verbose_name="Xladogent turi")
    sku = models.CharField(max_length=50, verbose_name="SKU", default="8704")
    installation_type = models.CharField(max_length=50, choices=INSTALLATION_CHOICES, default='wall_split', verbose_name="O‘rnatish turi")
    color = models.CharField(max_length=50, default="oq", verbose_name="Rang")
    external_unit_weight = models.FloatField(default=12, verbose_name="Tashqi blok og'irligi (kg)")
    internal_unit_weight = models.FloatField(default=9.5, verbose_name="Ichki blok og'irligi (kg)")
    power_consumption_cooling = models.IntegerField(default=575, verbose_name="Sovutish rejimida iste'mol qilinadigan quvvat (W)")

    def __str__(self):
        return f"{self.brand} - {self.sku}"
