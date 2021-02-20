# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:58:37 2021

@author: TranchinaKe
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import seaborn as sns
import pandas as pd

#necessario avere un foglio delle credenziali.json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
## The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
#SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1a6NVcFzkHUSf4fG0woy4xhjcmQ0FL4fGEsrMRuzt_W0'
numeroVisualizzazione = 'Risposte del modulo 1!B2:F'

def main(numeroVisualizzazione):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=numeroVisualizzazione).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    main()



def returnMatrixResult(numeroVisualizzazione):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=numeroVisualizzazione).execute()
    values = result.get('values', [])
    
    #[['6', '6', '5', '4', '4'],
    # ['4', '5', '4', '5', '6'],
    # ['5', '6', '2', '2', '2'],
    # ['2', '1', '1', '1', '1'],
    # ['1', '2', '2', '4', '3'],
    # ['2', '2', '3', '4', '3']]

#
    flat_list = [item for sublist in values for item in sublist]
    
    #['6', '6', '5', '4', '4', '4', '5', '4', '5', '6', '5', '6',
    # '2', '2', '2', '2', '1', '1', '1', '1', '1', '2', '2', '4',
    # '3', '2', '2', '3', '4', '3']
    
    for i in range(0, len(flat_list)): 
        flat_list[i] = int(flat_list[i]) 
    
        #From list of string to list of int 
        #
        #[6, 6, 5, 4, 4, 4, 5, 4, 5, 6,
        # 5, 6, 2, 2, 2, 2, 1, 1, 1, 1,
        # 1, 2, 2, 4, 3, 2, 2, 3, 4, 3]
    return flat_list

#### PRIMA VIS
numeroVisualizzazione = 'Risposte del modulo 1!B2:F'
flat_list1 = returnMatrixResult(numeroVisualizzazione)

#### Seconda VIS
numeroVisualizzazione = 'Risposte del modulo 1!G2:K'
flat_list2 = returnMatrixResult(numeroVisualizzazione)

#### Terza VIS
numeroVisualizzazione = 'Risposte del modulo 1!L2:P'
flat_list3 = returnMatrixResult(numeroVisualizzazione)

f = pd.DataFrame(flat_list1,columns =['Prima Vis'])
f['Seconda Vis'] = pd.Series(flat_list2)
f['Terza Vis'] = pd.Series(flat_list3)
f

#ax = sns.violinplot(inner="box",data=f,gridsize=1000, bw=2,width=0.2,split=True)
ax = sns.violinplot(inner="box",data=f)
ax.showmeans()
    




#grafico singolo
numeroVisualizzazione = 'Risposte del modulo 1!B2:F'
flat_list1 = returnMatrixResult(numeroVisualizzazione)

ax = sns.violinplot(x=flat_list1, inner="box")
ax.set_title("Violin Plot Valutazione PRIMA visualizzazione")
#ax.set_ylabel("Gapminder Life Expectancy")
ax.set_xlabel("Punteggio")


#### Seconda VIS
numeroVisualizzazione = 'Risposte del modulo 1!G2:K'
flat_list2 = returnMatrixResult(numeroVisualizzazione)
 
ax = sns.violinplot(x=flat_list2, inner="box")
ax.set_title("Violin Plot Valutazione SECONDA visualizzazione")
#ax.set_ylabel("Gapminder Life Expectancy")
ax.set_xlabel("Punteggio")

#### Terza VIS
numeroVisualizzazione = 'Risposte del modulo 1!L2:P'
flat_list = returnMatrixResult(numeroVisualizzazione)
 
ax = sns.violinplot(x=flat_list, inner="box")
ax.set_title("Violin Plot Valutazione TERZA visualizzazione")
#ax.set_ylabel("Gapminder Life Expectancy")
ax.set_xlabel("Punteggio")
