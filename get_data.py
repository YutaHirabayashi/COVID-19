import os
import pandas as pd
import datetime as dt

def get_codiv_19_data():
    csv_list = os.listdir("./data")
    df_list = [create_df_from_csv(csv) for csv in csv_list]
    df = pd.concat(df_list)
    df = df.astype(float)
    df = df.sort_index()
    return df

def create_df_from_csv(csv_file_name):
    week_number = int(csv_file_name[5:7])
    date = dt.datetime(2020,2,9) + dt.timedelta(weeks = (week_number - 6))
    df = pd.read_csv(os.path.join("./data", csv_file_name),encoding="SHIFT-JIS", skiprows=2)
    covid_19_name = get_codiv_19_name(["新型コロナウイルス", "新型コロナウイルス感染症"], df.columns)
    column_number = list(df.columns).index(covid_19_name) + 1
    df = df.iloc[:, column_number:column_number+1]
    df = df.iloc[2::, :]
    df = df.rename(columns = {df.columns[0]:date})
    df = df.T
    df.index = df.index.strftime("%m/%d")
    return df

def get_codiv_19_name(name_list, column_list):
    for name in name_list:
        if name in column_list:
            return name    
    return None
