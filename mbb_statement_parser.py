# MBB Current/Savings Account Statement Parser
# (based on TNG Statement in CSV by Rexpert https://github.com/Rexpert/TNG_Statement_in_CSV)

import argparse
import pandas as pd
import numpy as np
import camelot
import PyPDF2

parser = argparse.ArgumentParser(
                          description='Converts MBB\'s monthly current/savings account statement to CSV',
                          epilog='Not extensively tested. Not affliated with MBB.'
                        )
parser.add_argument('filename', default='statement.pdf', nargs='?', help='PDF file of MBB Statement')
parser.add_argument('-pw', '--password', help='Password for MBB Statement')
args = parser.parse_args()

reader = PyPDF2.PdfFileReader(args.filename)

password = args.password

if reader.is_encrypted:
    if not password:
        password = input('PDF encrypted! Please enter password: ')

# Read PDF Statement into a table collection, the areas/regions and columns separators is self-defined
try:
    tables = camelot.read_pdf(args.filename, pages='all', flavor='stream', password=password,
                            table_regions=['30,600,480,100'], table_areas=['30,600,480,100'],
                            columns=['80,310,400'],
                            split_text=True, strip_text='\n')
except:
    (
        print('Error opening file:', args.filename),
        print('Some possible resolutions:'),
        print(' - Ensure filename is correct'),
        print(' - Ensure PyCryptodome is installed to decrypt password'),
        print(' - Wrong password, maybe?'),
        exit()
    )

df = (
    pd
    .concat([tbl.df for tbl in tables._tables], ignore_index=True)
    .set_axis(['Date', 'Description', 'Amount (RM)', 'Balance (RM)'], axis=1)
    .query('Date.str.contains(r"^\d|^$", na=True) & ~Description.str.contains(r"^$") & ~Description.str.startswith(r"ENDING BALANCE :") & ~Description.str.startswith(r"TOTAL CREDIT :") & ~Description.str.startswith(r"TOTAL DEBIT :")', engine='python')
    .assign(idx=lambda x: (~x.Date.str.contains('^$')).cumsum())
    .groupby('idx')
    .apply(lambda x: x.apply(lambda y: ' '.join(y.fillna('').astype(str))).str.strip())
    .reset_index(drop=True)
    .drop(['idx'], axis=1)
    .replace(r'^\s*$', np.nan, regex=True)
    .assign(
        Date=lambda x: pd.to_datetime(x.Date, format=r'%d/%m/%y'),
        **{
            'Amount (RM)': lambda x: np.where(
                x['Amount (RM)'].str.endswith('-'),
                -x['Amount (RM)'].str.removesuffix('-').str.replace(r'[^0-9\.]', '', regex=True).astype(float),
                x['Amount (RM)'].str.removesuffix('+').str.replace(r'[^0-9\.]', '', regex=True).astype(float)
            ),
            'Balance (RM)': lambda x: x['Balance (RM)'].str.replace(r'[^0-9.]', '', regex=True).astype(float)
        }
    )
)

# Debug to print out dataframe
print(df)

# Output to CSV
(
    df.to_csv(args.filename.replace('pdf', 'csv'), index=False, encoding='utf-8'),
    print("\nAll done"),
    print('File saved to:', args.filename.replace('pdf', 'csv'))
)
