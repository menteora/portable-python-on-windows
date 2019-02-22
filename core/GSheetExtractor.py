from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper

class GSheetExtractor(DataExtractor):

    def connect(self):
        scopes = self.config_json['authentication']['scopes']
        token = PathHelper.getConfigPath(self.config_json['authentication']['token'])
        credentials = PathHelper.getConfigPath(self.config_json['authentication']['credentials'])

        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        store = file.Storage(token)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(credentials, scopes)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

    def execute(self, spreadsheet_id, range_name):
        self.result = self.service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

    def toDataframe(self):
        """ Converts Google sheet data to a Pandas DataFrame.
        Note: This script assumes that your data contains a header file on the first row!

        Also note that the Google API returns 'none' from empty cells - in order for the code
        below to work, you'll need to make sure your sheet doesn't contain empty cells,
        or update the code to account for such instances.

        """
        header = self.result.get('values', [])[0]   # Assumes first line is header!
        values = self.result.get('values', [])[1:]  # Everything else is data.

        if not values:
            print('No data found.')
        else:
            all_data = []
            for col_id, col_name in enumerate(header):
                print(col_id)
                print(col_name)
                column_data = []
                for row in values:
                    try:
                        column_data.append(row[col_id])
                    except IndexError:
                        column_data.append('')
                        print(column_data)
                    # print(column_data)
                ds = pd.Series(data=column_data, name=col_name)
                all_data.append(ds)
            self.df = pd.concat(all_data, axis=1)
            return self.df
