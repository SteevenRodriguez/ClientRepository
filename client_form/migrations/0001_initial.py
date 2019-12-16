# Generated by Django 3.0 on 2019-12-13 23:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('procedencia', models.CharField(choices=[('U', 'Urbano'), ('R', 'Rural')], max_length=1)),
                ('origen', models.CharField(max_length=20)),
                ('derivacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_form.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_form.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='tratamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_form.Product'),
        ),
    ]