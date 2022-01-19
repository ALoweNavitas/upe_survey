import pandas as pd 
import os
import json
from datetime import date, datetime
import update_survey

access_token = os.environ.get('access_token_surveymonkey')
survey_id = 315864260

# update_survey.update_survey_data(survey_id=survey_id, access_token=access_token)
# update_survey.update_survey_details(survey_id=survey_id, access_token=access_token)

with open('data.json', 'r') as data_file:
    json_data = json.load(data_file)

with open('details.json') as details_file: 
    json_details = json.load(details_file)

def parse_timestamp(text):
    d = text.replace('+00:00', '')
    return datetime.strptime(d, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')

for i in range(len(json_data['data'])):
    print(json_data['data'][i]['custom_variables']['College'])
    print(json_data['data'][i]['id'])
    # print(json_data['data'][i]['custom_variables']['College'])

json_df = pd.json_normalize(data=json_data['data'],
                        record_path=['pages', 'questions', 'answers'], # Whatever paths are here dictates what fields need to be collected in the meta code below. Can be str or list-like
                        meta=['id', ['pages', 'questions', 'id'], ['answers', 'id']])

print(json_df)