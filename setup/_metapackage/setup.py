import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-l10n-italy",
    description="Meta package for oca-l10n-italy Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_invoice_report_ddt_group',
        'odoo12-addon-account_vat_period_end_statement',
        'odoo12-addon-assets_management',
        'odoo12-addon-currency_rate_update_boi',
        'odoo12-addon-fiscal_epos_print',
        'odoo12-addon-fiscal_epos_print_fiscalcode',
        'odoo12-addon-fiscal_epos_print_meal_voucher',
        'odoo12-addon-l10n_it_abicab',
        'odoo12-addon-l10n_it_accompanying_invoice',
        'odoo12-addon-l10n_it_account',
        'odoo12-addon-l10n_it_account_balance_report',
        'odoo12-addon-l10n_it_account_stamp',
        'odoo12-addon-l10n_it_account_stamp_ddt',
        'odoo12-addon-l10n_it_account_stamp_sale',
        'odoo12-addon-l10n_it_account_tax_kind',
        'odoo12-addon-l10n_it_ateco',
        'odoo12-addon-l10n_it_causali_pagamento',
        'odoo12-addon-l10n_it_central_journal',
        'odoo12-addon-l10n_it_codici_carica',
        'odoo12-addon-l10n_it_corrispettivi',
        'odoo12-addon-l10n_it_corrispettivi_fatturapa_out',
        'odoo12-addon-l10n_it_corrispettivi_sale',
        'odoo12-addon-l10n_it_ddt',
        'odoo12-addon-l10n_it_delivery_note',
        'odoo12-addon-l10n_it_delivery_note_base',
        'odoo12-addon-l10n_it_delivery_note_batch',
        'odoo12-addon-l10n_it_delivery_note_order_link',
        'odoo12-addon-l10n_it_dichiarazione_intento',
        'odoo12-addon-l10n_it_esigibilita_iva',
        'odoo12-addon-l10n_it_fatturapa',
        'odoo12-addon-l10n_it_fatturapa_export_zip',
        'odoo12-addon-l10n_it_fatturapa_in',
        'odoo12-addon-l10n_it_fatturapa_in_purchase',
        'odoo12-addon-l10n_it_fatturapa_in_rc',
        'odoo12-addon-l10n_it_fatturapa_out',
        'odoo12-addon-l10n_it_fatturapa_out_ddt',
        'odoo12-addon-l10n_it_fatturapa_out_rc',
        'odoo12-addon-l10n_it_fatturapa_out_stamp',
        'odoo12-addon-l10n_it_fatturapa_out_triple_discount',
        'odoo12-addon-l10n_it_fatturapa_out_wt',
        'odoo12-addon-l10n_it_fatturapa_pec',
        'odoo12-addon-l10n_it_fatturapa_sale',
        'odoo12-addon-l10n_it_fiscal_document_type',
        'odoo12-addon-l10n_it_fiscal_payment_term',
        'odoo12-addon-l10n_it_fiscalcode',
        'odoo12-addon-l10n_it_fiscalcode_crm',
        'odoo12-addon-l10n_it_fiscalcode_sale',
        'odoo12-addon-l10n_it_intrastat',
        'odoo12-addon-l10n_it_intrastat_statement',
        'odoo12-addon-l10n_it_invoices_data_communication',
        'odoo12-addon-l10n_it_invoices_data_communication_fatturapa',
        'odoo12-addon-l10n_it_ipa',
        'odoo12-addon-l10n_it_location_nuts',
        'odoo12-addon-l10n_it_mis_reports_pl_bs',
        'odoo12-addon-l10n_it_pec',
        'odoo12-addon-l10n_it_pos_fatturapa',
        'odoo12-addon-l10n_it_pos_fiscalcode',
        'odoo12-addon-l10n_it_rea',
        'odoo12-addon-l10n_it_reverse_charge',
        'odoo12-addon-l10n_it_ricevute_bancarie',
        'odoo12-addon-l10n_it_sdi_channel',
        'odoo12-addon-l10n_it_split_payment',
        'odoo12-addon-l10n_it_vat_registries',
        'odoo12-addon-l10n_it_vat_registries_split_payment',
        'odoo12-addon-l10n_it_vat_statement_communication',
        'odoo12-addon-l10n_it_vat_statement_split_payment',
        'odoo12-addon-l10n_it_website_portal_fatturapa',
        'odoo12-addon-l10n_it_website_portal_fatturapa_sale',
        'odoo12-addon-l10n_it_website_portal_fiscalcode',
        'odoo12-addon-l10n_it_website_portal_ipa',
        'odoo12-addon-l10n_it_website_sale_corrispettivi',
        'odoo12-addon-l10n_it_website_sale_fatturapa',
        'odoo12-addon-l10n_it_website_sale_fiscalcode',
        'odoo12-addon-l10n_it_withholding_tax',
        'odoo12-addon-l10n_it_withholding_tax_causali',
        'odoo12-addon-l10n_it_withholding_tax_payment',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
