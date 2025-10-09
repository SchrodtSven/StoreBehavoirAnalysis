# Sanitizer 
# Disclaimer:  Kommentare und Naming Conventions sind und bleiben EN
# AUTHOR Sven Schrodt 
# SINCE 2025-10-06

import pandas as pd

class Sanitizer:
    """ Class sanitizing data
        - fill time series
        - adjust data types
    """

    def __init__(self):
        pass
    
    @staticmethod
    def get_time_df(nm:str, frm:str, utl:str, freq:str='D', format:str='YYYY-mm-dd') -> pd.DataFrame:
        """_summary_

        Args:
            nm (str): name of date column
            frm (str): from date
            utl (str): until date
            freq (str, optional): Frequency; defaults to 'D'.
            format (str, optional): Optional datee format string Defaults to 'YYYY-mm-dd'.

        Returns:
            pd.DataFrame: _description_
        """
        period = pd.date_range(start=frm, end=utl, freq=freq)
        return  pd.DataFrame({nm: period})
    
    
if __name__ == "__main__":
 
    print(Sanitizer.get_time_df('Datum', '2025-08-01', '2025-08-23'))