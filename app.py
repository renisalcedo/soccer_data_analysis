import pandas as pd
from classes.position_earning import PositionEarning
from classes.common_position import CommonPosition
from classes.normalized_earning import NormalizedEarning

if __name__ == '__main__':
    """ Initializes the Major League Soccer as default excel """
    excel_file = 'mls.xlsx'
    mls_data = pd.ExcelFile(excel_file)

    pe = PositionEarning(mls_data)
    pe.display()
    cp = CommonPosition(mls_data)
    cp.display()
    ne = NormalizedEarning(mls_data)
    ne.display()
