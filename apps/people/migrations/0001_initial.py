# Generated by Django 2.0.1 on 2018-05-30 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(editable=False)),
                ('modification_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Information')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.IntegerField(choices=[(0, 'Gênero'), (1, 'Feminino'), (2, 'Masculino')], default=0)),
                ('civil_status', models.IntegerField(choices=[(0, 'Estado civil'), (1, 'Casado(a)'), (2, 'Divorciado(a)'), (3, 'Separado(a)'), (4, 'Solteiro(a)'), (5, 'União Estável'), (6, 'Viúvo(a)')], default=0)),
                ('mothers_name', models.CharField(max_length=60)),
                ('fathers_name', models.CharField(blank=True, max_length=60)),
                ('occupation', models.CharField(max_length=40)),
                ('rg', models.CharField(max_length=12, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=60)),
                ('home_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=16, null=True)),
                ('address', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(blank=True, max_length=80, null=True)),
                ('neighborhood', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=32)),
                ('uf', models.CharField(choices=[('UF', 'Estado'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=0, max_length=2)),
                ('cep', models.CharField(blank=True, max_length=10)),
                ('comments', models.CharField(blank=True, max_length=1024, null=True)),
                ('ref_person', models.CharField(default='ref', max_length=50)),
                ('slug', models.SlugField(default='page-slug', max_length=150, unique=True)),
            ],
            bases=('people.information',),
        ),
        migrations.AddField(
            model_name='information',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
            ],
            options={
                'verbose_name': 'Doador',
                'verbose_name_plural': 'Doadores',
                'ordering': ['name'],
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
                ('bag_helped', models.BooleanField(choices=[(0, 'Não'), (1, 'Sim')], default=0, max_length=3)),
                ('salary', models.CharField(default=0, max_length=20)),
                ('employees_type', models.CharField(choices=[(1, 'Colaborador(a)'), (2, 'Professor(a)')], max_length=11)),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['name'],
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
                ('scholarity', models.IntegerField(choices=[(0, 'Escolaridade'), (1, 'Fundamental - Incompleto'), (2, 'Fundamental - Completo'), (3, 'Médio - Incompleto'), (4, 'Médio - Completo'), (5, 'Superior - Incompleto'), (6, 'Superior - Completo'), (7, 'Pós-graduação - Incompleto'), (8, 'Pós-graduação - Completo'), (9, 'Mestrado - Incompleto'), (10, 'Mestrado - Completo'), (11, 'Doutorado - Incompleto'), (12, 'Doutorado - Completo')], default=0)),
                ('school', models.CharField(max_length=100)),
                ('time', models.IntegerField(choices=[(0, 'Período'), (1, 'Matutino'), (2, 'Diurno'), (3, 'Vespertino'), (4, 'Noturno')], default=0)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['name'],
            },
            bases=('people.person',),
        ),
    ]
