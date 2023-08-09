# Generated by Django 4.1.7 on 2023-08-09 11:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tally', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_version', models.CharField(max_length=10)),
                ('blocked_versions', models.CharField(max_length=150)),
                ('latest_software_path', models.CharField(max_length=50)),
                ('download_link', models.URLField(max_length=90)),
                ('total_downloads_till_date', models.IntegerField(default=0)),
                ('total_downloads_current_version', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, unique=True)),
                ('company_number', models.IntegerField(blank=True, null=True)),
                ('starting_from', models.CharField(blank=True, max_length=10, null=True)),
                ('ending_at', models.CharField(blank=True, max_length=10, null=True)),
                ('guid', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=90, null=True)),
                ('sync_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sync_from_user', models.CharField(max_length=50)),
                ('company_url', models.URLField(blank=True, null=True)),
                ('company_email', models.CharField(blank=True, default='vikas.pandey9323@gmail.com', max_length=150, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigurationBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=90)),
                ('user_mobile', models.CharField(max_length=10, unique=True)),
                ('user_password', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=10)),
                ('tally_path', models.CharField(max_length=150)),
                ('schedule_time_mins', models.CharField(max_length=5)),
                ('schedule_time_hrs', models.CharField(max_length=5)),
                ('port_number', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modules_assigned', models.CharField(max_length=20)),
                ('is_premium', models.BooleanField(default=False)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
                ('grand_parent', models.CharField(blank=True, max_length=50, null=True)),
                ('parent', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_applicable', models.BooleanField(default=False)),
                ('tds_applicable', models.BooleanField(default=False)),
                ('billwise_on', models.BooleanField(default=False)),
                ('is_cost_center_on', models.BooleanField(default=False)),
                ('is_sub_ledger', models.BooleanField(default=False)),
                ('is_revenue', models.BooleanField(default=False)),
                ('affets_gross_profit', models.BooleanField(default=False)),
                ('is_deemed_positive', models.BooleanField(default=False)),
                ('affects_stock', models.BooleanField(default=False)),
                ('alter_id', models.IntegerField(blank=True, null=True)),
                ('primary_group', models.CharField(max_length=60)),
                ('group_opening_balance', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('group_closing_balance', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('credit_total', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('debit_total', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('overdue_bills', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('cashin', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('cashout', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('has_cost_centers', models.BooleanField(default=False)),
                ('this_yr_bal', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('prv_yr_bal', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('this_qtr_bal', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('prv_qtr_bal', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='GSTR1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_no', models.CharField(blank=True, max_length=90, null=True)),
                ('customer_billing_name', models.CharField(blank=True, max_length=90, null=True)),
                ('report1', models.BooleanField(default=False)),
                ('report2', models.BooleanField(default=False)),
                ('report3', models.BooleanField(default=False)),
                ('report4', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='GSTR2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_no', models.CharField(blank=True, max_length=90, null=True)),
                ('customer_billing_name', models.CharField(blank=True, max_length=90, null=True)),
                ('report1', models.BooleanField(default=False)),
                ('report2', models.BooleanField(default=False)),
                ('report3', models.BooleanField(default=False)),
                ('report4', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Ledgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=90, null=True)),
                ('primary_group_str', models.CharField(blank=True, max_length=90, null=True)),
                ('parent_str', models.CharField(blank=True, max_length=90, null=True)),
                ('creation_date', models.CharField(blank=True, max_length=10, null=True)),
                ('alteration_date', models.CharField(blank=True, max_length=10, null=True)),
                ('altered_by', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=90, null=True)),
                ('email', models.CharField(blank=True, max_length=95, null=True)),
                ('is_cost_center_on', models.BooleanField(default=False)),
                ('mailing_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gst', models.CharField(blank=True, max_length=15, null=True)),
                ('opening_balance', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('closing_balance', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('budget', models.BigIntegerField(blank=True, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='ParentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imag', models.FileField(blank=True, null=True, upload_to='pi_history_file/')),
            ],
        ),
        migrations.CreateModel(
            name='TrialBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular', models.CharField(max_length=90)),
                ('dr_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('cr_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('balance_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
            options={
                'unique_together': {('company_id', 'particular', 'dr_amt', 'cr_amt')},
            },
        ),
        migrations.CreateModel(
            name='voucher_type_parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vouchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=90)),
                ('voucher_type_internal', models.CharField(max_length=90)),
                ('v_number', models.CharField(blank=True, max_length=30, null=True)),
                ('v_date', models.CharField(blank=True, max_length=10, null=True)),
                ('v_refrence', models.CharField(blank=True, max_length=20, null=True)),
                ('v_refrence_date', models.CharField(blank=True, max_length=10, null=True)),
                ('gst', models.CharField(blank=True, max_length=90, null=True)),
                ('basic_order_ref', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('narration', models.CharField(blank=True, max_length=200, null=True)),
                ('invoice_date_time', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('alteration_date', models.DateField(blank=True, null=True)),
                ('voucher_date', models.DateField(blank=True, null=True)),
                ('instrument_number', models.CharField(blank=True, max_length=30, null=True)),
                ('instrument_date', models.CharField(blank=True, max_length=15, null=True)),
                ('bank_date', models.CharField(blank=True, max_length=15, null=True)),
                ('is_reconciled', models.BooleanField(blank=True, default=False, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
                ('party_ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.ledgers')),
            ],
            options={
                'ordering': ['-voucher_date'],
            },
        ),
        migrations.CreateModel(
            name='VoucherItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name_temp', models.CharField(blank=True, max_length=100, null=True)),
                ('amt', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('type', models.CharField(choices=[('CR', 'CR'), ('DR', 'DR')], max_length=5)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.ledgers')),
                ('voucher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.vouchers')),
            ],
            options={
                'ordering': ['-auto_timedate'],
                'unique_together': {('ledger_name_temp', 'amt', 'type', 'voucher_id')},
            },
        ),
        migrations.CreateModel(
            name='VoucherBillAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('amt', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('type', models.CharField(blank=True, max_length=15, null=True)),
                ('voucher_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.voucheritem')),
            ],
        ),
        migrations.CreateModel(
            name='TrialBalanceMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_group_for_tbm', to='import_app.group')),
                ('custom_parent_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_parent_group_for_tbm', to='import_app.parentgroup')),
                ('groups', models.ManyToManyField(blank=True, related_name='group_for_tbm', to='import_app.group')),
                ('parent_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_group_for_tbm', to='import_app.parentgroup')),
                ('trial_balance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.trialbalance')),
            ],
        ),
        migrations.CreateModel(
            name='SyncHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('sync_from_user', models.CharField(max_length=50)),
                ('is_auto_sync', models.BooleanField(default=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=90)),
                ('units', models.CharField(max_length=50)),
                ('gst_appicable', models.BooleanField(default=False)),
                ('opening_quantity', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('opening_value', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('rate_per', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
                ('under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.vouchers')),
            ],
        ),
        migrations.CreateModel(
            name='ProfitLoss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_name', models.CharField(max_length=80)),
                ('total_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('type', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], max_length=20)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
            options={
                'unique_together': {('company_id', 'head_name', 'total_amt', 'type')},
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.customers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ledgers',
            name='primary_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.parentgroup'),
        ),
        migrations.AddField(
            model_name='ledgers',
            name='trial_balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.trialbalance'),
        ),
        migrations.AddField(
            model_name='ledgers',
            name='under',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally.group'),
        ),
        migrations.AddField(
            model_name='ledgers',
            name='under_custom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally.customgroup'),
        ),
        migrations.CreateModel(
            name='GSTSalesValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_billing_name', models.CharField(blank=True, max_length=90, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=90, null=True)),
                ('inv_no', models.CharField(blank=True, max_length=20, null=True)),
                ('inv_date', models.DateField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('inv_typ', models.CharField(blank=True, max_length=3, null=True)),
                ('txval', models.FloatField(blank=True, null=True)),
                ('camt', models.FloatField(blank=True, null=True)),
                ('samt', models.FloatField(blank=True, null=True)),
                ('iamt', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('report5', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='GSTR2_invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(blank=True, max_length=20, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('inv_typ', models.CharField(blank=True, max_length=3, null=True)),
                ('gstr2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.gstr2')),
            ],
            options={
                'unique_together': {('invoice_no', 'invoice_date', 'total_value', 'inv_typ')},
            },
        ),
        migrations.CreateModel(
            name='GSTR1_invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(blank=True, max_length=20, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('inv_typ', models.CharField(blank=True, max_length=3, null=True)),
                ('gstr1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.gstr1')),
            ],
            options={
                'unique_together': {('invoice_no', 'invoice_date', 'total_value', 'inv_typ')},
            },
        ),
        migrations.CreateModel(
            name='GSTPurchaseValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_billing_name', models.CharField(blank=True, max_length=90, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=90, null=True)),
                ('inv_no', models.CharField(blank=True, max_length=20, null=True)),
                ('inv_date', models.DateField(blank=True, null=True)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('inv_typ', models.CharField(blank=True, max_length=3, null=True)),
                ('txval', models.FloatField(blank=True, null=True)),
                ('camt', models.FloatField(blank=True, null=True)),
                ('samt', models.FloatField(blank=True, null=True)),
                ('iamt', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('report5', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='primary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.parentgroup'),
        ),
        migrations.AddField(
            model_name='group',
            name='trial_balance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.trialbalance'),
        ),
        migrations.CreateModel(
            name='DateWiseLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_date', models.DateField()),
                ('closing_balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True)),
                ('ledger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.ledgers')),
            ],
        ),
        migrations.CreateModel(
            name='CrucialNumbersBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=90, null=True)),
                ('cr_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('dr_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 9, 16, 32, 41, 668737), null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='CrucialNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todays_sale', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('monthly_cumulative', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('yearly_cumulative', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 9, 11, 2, 41, 668737, tzinfo=datetime.timezone.utc), null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('person', 'company')},
            },
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(blank=True, max_length=50, null=True)),
                ('company_id', models.ManyToManyField(to='import_app.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='persons',
            field=models.ManyToManyField(through='import_app.CompanyPerson', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_name', models.CharField(max_length=80)),
                ('total_amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('type', models.CharField(choices=[('Asset', 'Asset'), ('Liabilities', 'Liabilities')], max_length=20)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
            options={
                'unique_together': {('company_id', 'head_name', 'total_amt', 'type')},
            },
        ),
        migrations.CreateModel(
            name='voucher_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('is_head', models.BooleanField(default=False)),
                ('total_entry', models.IntegerField(default=0)),
                ('alter_id', models.CharField(max_length=10)),
                ('guid', models.CharField(max_length=55)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_app.voucher_type_parent')),
            ],
            options={
                'unique_together': {('company_id', 'name', 'type')},
            },
        ),
        migrations.CreateModel(
            name='ScheduleMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mis_name', models.CharField(blank=True, max_length=40, null=True)),
                ('days', models.CharField(blank=True, max_length=50, null=True)),
                ('is_daily', models.BooleanField(default=False)),
                ('from_email', models.CharField(max_length=90)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
                ('schedule_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('company_id', 'mis_name', 'days')},
            },
        ),
        migrations.CreateModel(
            name='PLItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('pl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.profitloss')),
            ],
            options={
                'unique_together': {('pl', 'name', 'amt')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='ledgers',
            unique_together={('company_id', 'name', 'primary_group_str')},
        ),
        migrations.CreateModel(
            name='GSTR2_gst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txval', models.FloatField(blank=True, null=True)),
                ('camt', models.FloatField(blank=True, null=True)),
                ('samt', models.FloatField(blank=True, null=True)),
                ('iamt', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('gstr2_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.gstr2_invoice')),
            ],
            options={
                'unique_together': {('gstr2_invoice', 'txval', 'camt', 'samt', 'iamt', 'rate')},
            },
        ),
        migrations.CreateModel(
            name='GSTR1_gst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txval', models.FloatField(blank=True, null=True)),
                ('camt', models.FloatField(blank=True, null=True)),
                ('samt', models.FloatField(blank=True, null=True)),
                ('iamt', models.FloatField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('gstr1_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.gstr1_invoice')),
            ],
            options={
                'unique_together': {('gstr1_invoice', 'txval', 'camt', 'samt', 'iamt', 'rate')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('primary', 'company_id', 'name', 'grand_parent')},
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('company_name', 'company_number', 'starting_from', 'ending_at')},
        ),
        migrations.CreateModel(
            name='BSItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('amt', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('bs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.balancesheet')),
            ],
            options={
                'unique_together': {('bs', 'name', 'amt')},
            },
        ),
    ]