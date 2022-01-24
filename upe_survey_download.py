import pandas as pd 
import http.client
import os
import json
import time
from datetime import datetime

def main():
    pass

if __name__ == '__main__':
    main()

# Variables
access_token = os.environ.get('access_token_surveymonkey')
survey_id = 315864260
start_time = time.time()

# Functions
def parse_timestamp(text):
    d = text.replace('+00:00', '')
    return datetime.strptime(d, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')

def update_survey_details(survey_id, access_token):
    '''
    Calls the SurveyMonkey API to get the details of given survey, including the questions and general structure.
    survey_id = 12345678
    access_token = API access token from SurveyMonkey
    '''
    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {access_token}"
        }

    conn.request("GET", "/v3/surveys/{}/details".format(survey_id), headers=headers)
    res = conn.getresponse()
    survey_details = res.read()
    json_details = json.loads(survey_details)
        
    if res.status >= 400: 
        raise RuntimeError(f'Request failed: {res.status}')
    
    # Write the JSON response to a file
    with open('details.json', 'w') as f:
        data = json.dump(json_details, f, indent=4, sort_keys=True)

def update_survey_data(survey_id, access_token):
    '''
    Calls the SurveyMonkey API to get all of the data of a given survey.
    survey_id = 12345678
    access_token = API access token from SurveyMonkey
    '''
    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {access_token}"
        }

    conn.request("GET", "/v3/surveys/{}/responses/bulk".format(survey_id), headers=headers)
    res = conn.getresponse()
    survey_data = res.read()
    json_data = json.loads(survey_data)

    if res.status >= 400: 
        raise RuntimeError(f'Request failed: {res.status}')

    # Write the JSON response to a file
    with open('data.json', 'w') as f:
        data = json.dump(json_data, f, indent=4, sort_keys=True)

update_survey_details(access_token=access_token, survey_id=survey_id)
update_survey_data(access_token=access_token, survey_id=survey_id)

# Open the files 
with open('data.json', 'r') as data_file:
    json_data = json.load(data_file)

with open('details.json') as details_file: 
    json_details = json.load(details_file)

# Map Question ID to Question Text
id = pd.json_normalize(json_details['pages'], ['questions'])['id']
question_text = pd.json_normalize(json_details['pages'], ['questions', 'headings'])['heading']
questions = dict(zip(id, question_text))

# Map ID to college variable
id = []
college_value = []
for i in range(len(json_data['data'])):
    id.append(json_data['data'][i]['id'])
    college_value.append(json_data['data'][i]['custom_variables']['College'])

colleges = dict(zip(id, college_value))

# Map ID to semester variable
semester_value = []
for i in range (len(json_data['data'])):
    semester_value.append(json_data['data'][i]['custom_variables']['Semester'])

semesters = dict(zip(id, semester_value))

# Map ID to program variable
program_value = []
for i in range(len(json_data['data'])):
    program_value.append(json_data['data'][i]['custom_variables']['Program'])

programs = dict(zip(id, program_value))

# Map ID to module variable
module_value = []
for i in range (len(json_data['data'])):
    module_value.append(json_data['data'][i]['custom_variables']['Module'])

modules = dict(zip(id, module_value))

# Building the dataframe
json_df = pd.json_normalize(json_data['data'], ['pages', 'questions', 'answers'], ['id', ['questions', 'answers', 'id']])
json_df['college'] = json_df['id'].map(colleges)
json_df['semester'] = json_df['id'].map(semesters)
json_df['program'] = json_df['id'].map(programs)
json_df['module'] = json_df['id'].map(modules)
json_df['question'] = json_df['questions.answers.id'].map(questions)

# Rename columns
json_df.rename(columns={
    "choice_metadata.weight" : "answer",
    "questions.answers.id" : "question_id",
    "id" : "respondent_id"
}, inplace=True)

# Fill NA in the answer column
json_df['answer'].fillna(json_df['text'], inplace=True)

# Reshaping
json_df = json_df[[
    'respondent_id',
    'college',
    'semester',
    'program',
    'module',
    'question_id',
    'question',
    'answer'
]]

# Questions as headers - values / index / column headers
df = json_df.pivot_table('answer', ['respondent_id', 'college', 'program', 'semester', 'module'], 'question', aggfunc=sum).fillna(0)
print(df.head())
print(f'Script executed in: {time.time() - start_time} seconds')