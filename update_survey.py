import http.client
import json
import os
import time

def main():
    pass

if __name__ == '__main__':
    main()

access_token = os.environ.get('access_token_surveymonkey') # Stored in Windows environment variables for safety

# Grab the survey structure for the given ID

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
    surveyDetails = res.read()
    json_data = json.loads(surveyDetails)
        
    if res.status >= 400: 
        raise RuntimeError(f'Request failed: {res.status}')
    
    # Write the JSON response to a file
    with open('details.json', 'w') as f:
        data = json.dump(json_data, f, indent=4, sort_keys=True)

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
    surveyDetails = res.read()
    json_data = json.loads(surveyDetails)

    if res.status >= 400: 
        raise RuntimeError(f'Request failed: {res.status}')

    # Write the JSON response to a file
    with open('data.json', 'w') as f:
        data = json.dump(json_data, f, indent=4, sort_keys=True)

def get_surveys(access_token):
    '''
    Calls the SurveyMonkey API to get the surveys related to the access token.
    access_token = API access token from SurveyMonkey
    '''
    conn = http.client.HTTPSConnection("api.surveymonkey.com")
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {access_token}"
        }

    conn.request("GET", "/v3/surveys", headers=headers)
    res = conn.getresponse()
    surveyDetails = res.read()
    json_data = json.loads(surveyDetails)

    if res.status >= 400:
        raise RuntimeError(f'Request failed: {res.status}')

    # Write the JSON response to a file
    with open('surveys.json', 'w') as f:
        data = json.dump(json_data, f, indent=4, sort_keys=True)

# get_surveys(access_token = access_token)
# update_survey_details(survey_id = id, access_token = access_token)
# update_survey_data(survey_id = id, access_token = access_token)