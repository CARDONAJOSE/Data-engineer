import pandas as pd
import numpy as np 
#import install as xlrd
datos=r'''C:\Users\Jose Fabian Cardona\Desktop\olivie\DA2020.xlsx'''

data_keybio= pd.read_excel(datos)
data_keybio.describe 

data_keybio.isna()