# Generated by Django 2.0.1 on 2018-06-08 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmInformation',
            fields=[
                ('information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Information')),
                ('ref_adm', models.CharField(default='ref', max_length=50)),
                ('slug', models.SlugField(default='page-slug', max_length=150, unique=True)),
            ],
            bases=('people.information',),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('adminformation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adm.AdmInformation')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('students_number', models.IntegerField(default=0)),
                ('duration', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['name'],
            },
            bases=('adm.adminformation',),
        ),
    ]
