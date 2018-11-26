import pandas as pd
from classes.position_earning import PositionEarning

if __name__ == '__main__':
    """ Initializes the Major League Soccer as default excel """
    excel_file = 'mls.xlsx'
    mls_data = pd.ExcelFile(excel_file)

    pe = PositionEarning(mls_data)
    pe.display()