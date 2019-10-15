# Generated by Django 2.2.6 on 2019-10-15 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LendBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_book_from', models.DateField()),
                ('lend_book_till', models.DateField()),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Book')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
    ]
