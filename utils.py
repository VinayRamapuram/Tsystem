import json
import pandas as pd


def xml_to_pandas(data):
    try:
        data = json.dumps(data)
        data_dict = json.loads(data)
        extracted_data = data_dict['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']

        df = pd.DataFrame(extracted_data) \
            .rename(columns={'generic:ObsDimension': 'TIME_PERIOD', 'generic:ObsValue': 'OBS_VALUE'})
        time_period_data = []
        obs_value_data = []
        for index, row in df.iterrows():
            time_period_data.append(row['TIME_PERIOD']['@value'])
            obs_value_data.append(row['OBS_VALUE']['@value'])

        final_df = pd.DataFrame()
        final_df['TIME_PERIOD'] = time_period_data
        final_df['OBS_VALUE'] = obs_value_data
        final_df = final_df.astype({'OBS_VALUE': 'float'})
        return final_df
    except Exception as error:
        return 'Caught this error: ' + repr(error)
