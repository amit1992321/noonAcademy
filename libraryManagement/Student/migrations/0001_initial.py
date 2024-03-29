# Generated by Django 2.2.6 on 2019-10-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('UID', models.CharField(max_length=20)),
                ('course', models.CharField(choices=[('BCA', 'BCA'), ('MCA', 'MCA'), ('B.TECH', 'B.Tech'), ('BSC', 'bsc'), ('MBBS', 'Mbbs'), ('B.COM', 'B.Com'), ('M.COM', 'M.Com'), ('MSC', 'Msc'), ('PHD', 'Phd'), ('M.TECH', 'M.Tech'), ('MS', 'Ms')], default='BCA', max_length=25, null=True)),
                ('semester', models.CharField(choices=[('First', 'I'), ('Second', 'II'), ('Third', 'III'), ('Fourth', 'IV'), ('Five', 'V'), ('Six', 'VI'), ('Sevan', 'VII'), ('Eight', 'VIII')], default='First', max_length=20, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
