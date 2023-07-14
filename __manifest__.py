{
    'name': 'Invoice Report Adjustment For Kosmos',
    'version': '16.0',
    'summary': 'Menambahkan dan mengedit default invoice report menyesuaikan kebutuhan tim accountant Kosmos',
    'description':
        """
            - Menambahkan Bill to: di atas data customer
            - Mengubah format invoice date
            - Menambahkan total in words
        """,
    'category': 'Productivity',
    'author': 'Muhamad Syahril Aziz',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': ['report/invoice_adjustment_kosmos.xml'],
    'installable': True,
    'auto_install': False
}