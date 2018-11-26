import pandas as pd

if __name__ == '__main__':
    """ Initializes the Major League Soccer as default excel """
    excel_file = 'mls.xlsx'
    mls_data = pd.read_excel(excel_file)