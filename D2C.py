import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Facebook API Auto Sharer')
parser.add_argument('--last_team_id',  type=str, help='Last Team ID visible on the Mastersheet')
parser.add_argument('--csv_folder', default='registrations.csv', type=str, help='Folder path to D2C csv file')

args = parser.parse_args()

def find_row(df, team_id): #Finds the row with a particular Team ID
    flag = 0
    for index, row in df.iterrows():
        if row['Team Id'] == team_id:
            return index
    return None

def find_next_row(df, latest_team_id): #FInds the index of the next unique Team ID after a particular Team ID
    flag = 0
    for index, row in df.iterrows():
        if row['Team Id'] == latest_team_id:
            flag=1
        if flag:
            if row['Team Id'] != latest_team_id:
                return index
    return None

def new_team_entry(empty_df, df, index): #Enters a new team entry into the DataFrame
    count = 0
    team_id = df.iloc[index]['Team Id']
    list1 = [df.iloc[index]['Registration Time'], df.iloc[index]['Team Name']]

    while(df.iloc[index+count]['Team Id'] == team_id):
        member_info = [df.iloc[index+count]["Player's Name"], df.iloc[index+count]["Player's Email"], df.iloc[index+count]["Player's Mobile"], df.iloc[index+count]["Player's Organisation"]]
        list1.extend(member_info)
        count+=1
        if(index+count>=len(df)):
            break
            
    while(count<5):
        empty_list = ['']*4
        list1.extend(empty_list)
        count+=1

    list1.append('D2C - '+team_id)

    empty_df.loc[len(empty_df.index)] = list1

def create_df(df, latest_team_id): #Creates a new empty DataFrame and fills it with new team entries
    empty_df = pd.DataFrame(columns=['Timestamp','Team Name','Member - 1 Name','Email id','Phone Number','College Name','Member - 2 Name','Email id','Phone Number','College Name','Member - 3 Name','Email id','Phone Number',	'College Name'	,'Member - 4 Name'	,'Email id'	,'Phone Number'	,'College Name'	,'Member - 5 Name','Email id','Phone Number','College Name','How did you come to know about us?'])
    short_df = df.iloc[find_next_row(df, latest_team_id):, :]

    for team_id in short_df['Team Id'].unique():
        index = find_row(short_df, team_id)
        new_team_entry(empty_df, df, index)

    return empty_df

if __name__ == '__main__':
    df = pd.read_csv(args.csv_folder)
    new_df = create_df(df, args.last_team_id)
    new_df.to_csv('New_D2C_Registrations.csv')


