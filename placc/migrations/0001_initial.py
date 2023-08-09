# Generated by Django 4.1.7 on 2023-08-09 09:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('import_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales', models.FloatField(blank=True, default=0.0, null=True)),
                ('gross', models.FloatField(blank=True, default=0.0, null=True)),
                ('nett', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='NOTES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='REPORTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tally_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PLACC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(max_length=80)),
                ('debit', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('credit', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('final', models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=20, null=True)),
                ('tally_mapping_primary', models.CharField(blank=True, max_length=50, null=True)),
                ('tally_mapping_parent', models.CharField(blank=True, max_length=50, null=True)),
                ('notes_mapping', models.CharField(blank=True, choices=[('Accrued interest on NSC', 'Accrued interest on NSC'), ('Accumalated Depreciation', 'Accumalated Depreciation'), ('Advance Income Tax', 'Advance Income Tax'), ('Advance Wealth Tax', 'Advance Wealth Tax'), ('Loan Receivables - Short Term', 'Loan Receivables - Short Term'), ('Bank Charges', 'Bank Charges'), ('Bank Current Account', 'Bank Current Account'), ('Business Promotion', 'Business Promotion'), ('Communication', 'Communication'), ('Contribution to Provident and other fund', 'Contribution to Provident and other fund'), ('Depreciation', 'Depreciation'), ('Electricity & Water Charges', 'Electricity & Water Charges'), ('Debit Balances written off', 'Debit Balances written off'), ('Exchange difference', 'Exchange difference'), ('Fixed Assets', 'Fixed Assets'), ('Fixed Deposits with Bank', 'Fixed Deposits with Bank'), ('Gifts and donations (CSR Expd)', 'Gifts and donations (CSR Expd)'), ('Good Debtors', 'Good Debtors'), ('Interest Income', 'Interest Income'), ('Legal & Professional', 'Legal & Professional'), ('Loss on sale of Fixed Assets', 'Loss on sale of Fixed Assets'), ('Membership and subscriptions', 'Membership and subscriptions'), ('Advances to suppliers', 'Advances to suppliers'), ('Petty Cash', 'Petty Cash'), ('Prepaid Expenses', 'Prepaid Expenses'), ('Printing and stationery', 'Printing and stationery'), ('Professional Exps- Inter co', 'Professional Exps- Inter co'), ('Provision for doubtful debts/advances written back', 'Provision for doubtful debts/advances written back'), ('Professional tax payable', 'Professional tax payable'), ('Provision for Gratuity', 'Provision for Gratuity'), ('Provision for income tax', 'Provision for income tax'), ('Provision for doubtful debts & advances - Exp.', 'Provision for doubtful debts & advances - Exp.'), ('Rates & Taxes', 'Rates & Taxes'), ('Rent', 'Rent'), ('Repair & Maintainance', 'Repair & Maintainance'), ('Provision for Leave salary', 'Provision for Leave salary'), ('Excess provisions written back/ Misc inc', 'Excess provisions written back/ Misc inc'), ('Sales tax receivable', 'Sales tax receivable'), ('Security Deposits', 'Security Deposits'), ('Service Tax Payables', 'Service Tax Payables'), ('Staff training and recruitment', 'Staff training and recruitment'), ('Staff Welfare Expenses', 'Staff Welfare Expenses'), ('Share Capital', 'Share Capital'), ('Tax Current Year Income Tax', 'Tax Current Year Income Tax'), ('TDS Payable', 'TDS Payable'), ('TDS Receivable', 'TDS Receivable'), ('Inter Branch', 'Inter Branch'), ('Travelling and coveyance', 'Travelling and coveyance'), ('VAT Receivables', 'VAT Receivables'), ('Vehicle Running & Maintainance', 'Vehicle Running & Maintainance'), ('Wealth Tax Payable', 'Wealth Tax Payable'), ('Insurance', 'Insurance'), ('General Expenses', 'General Expenses'), ('GST Receivable', 'GST Receivable'), ('GST Payable', 'GST Payable'), ('Payable to employees', 'Payable to employees'), ('Payable for expenses', 'Payable for expenses'), ('Reserve & Surplus', 'Reserve & Surplus'), ('Salaries & Wages', 'Salaries & Wages')], max_length=50, null=True)),
                ('report_mapping', models.CharField(blank=True, choices=[('Accrued interest on NSC', 'Accrued interest on NSC'), ('Accumalated Depreciation', 'Accumalated Depreciation'), ('Advance Income Tax', 'Advance Income Tax'), ('Advance Wealth Tax', 'Advance Wealth Tax'), ('Loan Receivables - Short Term', 'Loan Receivables - Short Term'), ('Bank Charges', 'Bank Charges'), ('Bank Current Account', 'Bank Current Account'), ('Business Promotion', 'Business Promotion'), ('Communication', 'Communication'), ('Contribution to Provident and other fund', 'Contribution to Provident and other fund'), ('Depreciation', 'Depreciation'), ('Electricity & Water Charges', 'Electricity & Water Charges'), ('Debit Balances written off', 'Debit Balances written off'), ('Exchange difference', 'Exchange difference'), ('Fixed Assets', 'Fixed Assets'), ('Fixed Deposits with Bank', 'Fixed Deposits with Bank'), ('Gifts and donations (CSR Expd)', 'Gifts and donations (CSR Expd)'), ('Good Debtors', 'Good Debtors'), ('Interest Income', 'Interest Income'), ('Legal & Professional', 'Legal & Professional'), ('Loss on sale of Fixed Assets', 'Loss on sale of Fixed Assets'), ('Membership and subscriptions', 'Membership and subscriptions'), ('Advances to suppliers', 'Advances to suppliers'), ('Petty Cash', 'Petty Cash'), ('Prepaid Expenses', 'Prepaid Expenses'), ('Printing and stationery', 'Printing and stationery'), ('Professional Exps- Inter co', 'Professional Exps- Inter co'), ('Provision for doubtful debts/advances written back', 'Provision for doubtful debts/advances written back'), ('Professional tax payable', 'Professional tax payable'), ('Provision for Gratuity', 'Provision for Gratuity'), ('Provision for income tax', 'Provision for income tax'), ('Provision for doubtful debts & advances - Exp.', 'Provision for doubtful debts & advances - Exp.'), ('Rates & Taxes', 'Rates & Taxes'), ('Rent', 'Rent'), ('Repair & Maintainance', 'Repair & Maintainance'), ('Provision for Leave salary', 'Provision for Leave salary'), ('Excess provisions written back/ Misc inc', 'Excess provisions written back/ Misc inc'), ('Sales tax receivable', 'Sales tax receivable'), ('Security Deposits', 'Security Deposits'), ('Service Tax Payables', 'Service Tax Payables'), ('Staff training and recruitment', 'Staff training and recruitment'), ('Staff Welfare Expenses', 'Staff Welfare Expenses'), ('Share Capital', 'Share Capital'), ('Tax Current Year Income Tax', 'Tax Current Year Income Tax'), ('TDS Payable', 'TDS Payable'), ('TDS Receivable', 'TDS Receivable'), ('Inter Branch', 'Inter Branch'), ('Travelling and coveyance', 'Travelling and coveyance'), ('VAT Receivables', 'VAT Receivables'), ('Vehicle Running & Maintainance', 'Vehicle Running & Maintainance'), ('Wealth Tax Payable', 'Wealth Tax Payable'), ('Insurance', 'Insurance'), ('General Expenses', 'General Expenses'), ('GST Receivable', 'GST Receivable'), ('GST Payable', 'GST Payable'), ('Payable to employees', 'Payable to employees'), ('Payable for expenses', 'Payable for expenses'), ('Reserve & Surplus', 'Reserve & Surplus'), ('Salaries & Wages', 'Salaries & Wages')], max_length=50, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('auto_update_mapping_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_mapped', models.BooleanField(blank=True, default=False, null=True)),
                ('budget', models.FloatField(blank=True, default=0.0, null=True)),
                ('new_mapping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='placc.tally_mapping')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Mapping_Company_tally_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.FloatField(blank=True, default=0.0, null=True)),
                ('Company_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placc.company')),
                ('Notes_Mapping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='placc.notes')),
                ('Tally_Mapping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='placc.tally_mapping')),
            ],
        ),
        migrations.CreateModel(
            name='Mapping_Company_notes_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.FloatField(blank=True, default=0.0, null=True)),
                ('Company_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placc.company')),
                ('Notes_Mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placc.notes')),
                ('Report_Mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placc.reports')),
            ],
        ),
        migrations.CreateModel(
            name='CreditorsAgeingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('bill_ref', models.CharField(blank=True, max_length=50, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
            options={
                'ordering': ['customer_name'],
            },
        ),
        migrations.CreateModel(
            name='AgeingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('bill_ref', models.CharField(blank=True, max_length=50, null=True)),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.company')),
            ],
            options={
                'ordering': ['customer_name'],
            },
        ),
    ]
