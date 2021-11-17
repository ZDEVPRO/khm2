# Generated by Django 3.2.9 on 2021-11-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('telegram', models.CharField(blank=True, max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Biz haqimizda (Footer)',
                'verbose_name_plural': 'Biz haqimizda (Footer)',
            },
        ),
        migrations.CreateModel(
            name='AboutIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Biz haqimizda (Asosiy menyu)',
                'verbose_name_plural': 'Biz haqimizda (Asosiy menyu)',
            },
        ),
        migrations.CreateModel(
            name='ContactAboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=400)),
            ],
            options={
                'verbose_name': 'Aloqa malumotlari',
                'verbose_name_plural': 'Aloqa malumotlari',
            },
        ),
        migrations.CreateModel(
            name='ContactFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': "Pastki Bog'lanish",
                'verbose_name_plural': "Pastki Bog'lanish",
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Ismi')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Telefon raqami')),
                ('subject', models.CharField(blank=True, max_length=50, verbose_name='Mavzu')),
                ('message', models.TextField(blank=True, max_length=255, verbose_name='Xabar')),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('creat_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': "Bog'lanish bo'limi",
                'verbose_name_plural': "Bog'lanish bo'limi",
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logo',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=351, verbose_name='Sarlavhasi')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=2000, verbose_name='Tavsifi')),
                ('obshi_description', models.TextField(blank=True, max_length=3001, verbose_name='Hamma Tekst')),
                ('past_description', models.TextField(blank=True, max_length=1000, verbose_name='Pastki Tavsif:')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasmi')),
                ('create_on_date', models.DateField(auto_now=True)),
                ('create_on_time', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavha')),
                ('link', models.CharField(blank=True, max_length=100, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Pastki Sahifalar',
                'verbose_name_plural': 'Pastki Sahifalar',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ism Familya')),
                ('category', models.CharField(max_length=300, verbose_name='Kasb')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasim')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefon raqami')),
                ('whatsapp', models.CharField(blank=True, max_length=100)),
                ('telegram', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': "O'qituvchilar",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_students', models.CharField(max_length=10, verbose_name="O'quvchilar soni")),
                ('num_teachers', models.CharField(max_length=10, verbose_name="O'qituvchilar soni")),
                ('num_groups', models.CharField(max_length=10, verbose_name='Guruxlar soni')),
                ('num_room', models.CharField(max_length=10, verbose_name='Xonalar soni')),
            ],
            options={
                'verbose_name': 'Hisob',
                'verbose_name_plural': 'Hisob',
            },
        ),
    ]
