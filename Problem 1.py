# Make a Pandas DataFrame with two-dimensional list

import pandas as pd

def listToDataframe(twoD_list:list[[]]) -> pd.DataFrame:
    cols=[]
    for i in range(len(twoD_list[0])):
        cols.append(f'cols_{i}')
    df = pd.DataFrame(twoD_list, columns=cols)
    print(df)
    return df

listToDataframe(twoD_list=[['Semester1', 25, 77], ['Semester2', 30, 67], ['Semester3', 26, 90], ['Semester4', 22, 88]])