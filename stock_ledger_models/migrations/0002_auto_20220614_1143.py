# Generated by Django 3.2 on 2022-06-14 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_ledger_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stg_trn_data_del_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.DateField(auto_now_add=True)),
                ('PROCESS', models.CharField(max_length=30)),
                ('RECORDS_CLEANED', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'stg_trn_data_del_records',
            },
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='CURRENCY',
            new_name='CURRENCY_CODE',
        ),
        migrations.AlterField(
            model_name='item_dtl',
            name='UPDATE_DATETIME',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='stg_trn_data',
            name='PROCESS_IND',
            field=models.CharField(choices=[('N', 'Ready to pick'), ('E', 'Error'), ('P', 'Processed')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='stg_trn_data',
            name='QTY',
            field=models.DecimalField(decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='stg_trn_data',
            name='REV_TRN_NO',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterModelTable(
            name='calendar',
            table='calendar',
        ),
        migrations.AlterModelTable(
            name='class',
            table='class',
        ),
        migrations.AlterModelTable(
            name='currency',
            table='CURRENCY',
        ),
        migrations.AlterModelTable(
            name='date_range',
            table='date_range',
        ),
        migrations.AlterModelTable(
            name='dept',
            table='dept',
        ),
        migrations.AlterModelTable(
            name='err_trn_data',
            table='err_trn_data',
        ),
        migrations.AlterModelTable(
            name='gl_account',
            table='gl_account',
        ),
        migrations.AlterModelTable(
            name='item_dtl',
            table='ITEM_DTL',
        ),
        migrations.AlterModelTable(
            name='item_location',
            table='item_location',
        ),
        migrations.AlterModelTable(
            name='location',
            table='location',
        ),
        migrations.AlterModelTable(
            name='pndg_dly_rollup',
            table='pndg_dly_rollup',
        ),
        migrations.AlterModelTable(
            name='sl_control',
            table='sl_control',
        ),
        migrations.AlterModelTable(
            name='stg_fin_data',
            table='stg_fin_data',
        ),
        migrations.AlterModelTable(
            name='stg_trn_data',
            table='stg_trn_data',
        ),
        migrations.AlterModelTable(
            name='subclass',
            table='subclass',
        ),
        migrations.AlterModelTable(
            name='transaction_data_expl',
            table='transaction_data_expl',
        ),
        migrations.AlterModelTable(
            name='trn_data',
            table='trn_data',
        ),
        migrations.AlterModelTable(
            name='trn_data_history',
            table='trn_data_history',
        ),
        migrations.AlterModelTable(
            name='trn_data_rev',
            table='trn_data_rev',
        ),
    ]
