# Centralising Survey Activity - UPE

## :information_source: TLDR

This script uses the SurveyMonkey API to download the structure of the survey and all of the responses. The extracted data is in JSON format, and then is changed into a Pandas dataframe. 

## Contents

- Introduction
- Package Requirements
- SurveyMonkey API Usage
- Project Timeline

## Introduction

Navitas aims to create the best learning experiences for our students, and we hold the Student Experience in high regard to improvement of our business. The best way to understand the Student Experience is directly from the student themselves, with surveys proving an effective tool for collecting feedback. 

As part of our Balance Scorecard project, we track Student Satisfaction and Net Promoter Score (NPS), with the relevant surveys used to extract the data coming from surveys devolved and controlled by the college. As such, it is challenging to extract these two metrics, as well as monitor the wider aspects of student experience, due to lack of data aggregation. 

As part of the 2022-23 strategy, we aim to centralise the module survey process to UPE using Survey Monkey. Through this process, UPE would create and a control a new module survey which would be administered by the college, with the response data feeding back to a central repository. Colleges would have full access to all responses. This works similarly to the UPE Student Satisfaction Survey conducted annually. 

Much like our statistical data, qualitative and quantitative feedback in relation to Student Experience is valuable and our current approach loses out on taking advantage of this to drive forward empowering changes for our customers. By centralising activity, we can harvest the results within Evidence, whilst still providing colleges with flexibility to run the survey when and how they need to for their own practices. This project will strengthen our data capabilities and open up new opportunities for approaching Student Experience. 
## Package Requirements

Refer to ```requirements.txt``` for the packages and versions used in this script. The code was created in a virtual environment and tested with the noted versions. 

Use ```pip install -r requirements.txt``` to install packages and versions, if they are not already installed in your packages.

## SurveyMonkey API Usage

 This script uses the SurveyMonkey API to return responses from surveys. The API is REST-based, employs OAuth 2.0, and returns responses in JSON. 

 More information on the SurveyMonkey can be found in the [documentation files.](https://developer.surveymonkey.com/api/v3/#SurveyMonkey-Api)

## :calendar: Project Timeline 

| Period | Task | Status |
| --- | --- | --- |
| **Technical Provision**
| Start up | Scope project documentation | Complete :green_circle:
| Start up | Create a framework survey | Complete :green_circle:
| Start up | Implement custom variables to allow survey customisation across colleges | Complete :green_circle:
| Start up | Create automation scripts w/ Python | Complete :green_circle:
| Start up | Initial testing with dummy data (custom variables/ automation) | Complete :green_circle:
| Start up | Create a link builder tool for the colleges in Excel | Complete :green_circle:
| Start up | Transfer code to Azure DevOps for testing in Evidence | Not started :orange_circle:
| Start up | Testing with dummy data (using DevOps) | Not started :orange_circle:
| **Survey Provision**
| w/c 24 Jan | L&T to review the proposed survey and recommend changes | Not started :orange_circle:
| w/c 14 Feb | Proposals to be shared with colleges w/ proposed survey for review | Not started :orange_circle:
| w/c 14 Mar | Revised survey to be prepared following recommendations from colleges | Not started :orange_circle:
| April | Identify a trial college | Not started :orange_circle:

