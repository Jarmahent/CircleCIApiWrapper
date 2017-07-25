from collections import namedtuple
__version__ = '1.1 \n'

me = namedtuple("me", [
      "days_left_in_trial",
      "plan",
      "trial_end",
      "basic_email_prefs",
      "admin",
      "login",
      "student",
      "github_id",
      "pusher_id",
      "heroku_api_key",
      "num_projects_followed",
      "all_emails"

])

API_PATH = {
    'ME': 'https://circleci.com/api/v1.1/me?circle-token={}',
    'PROJECTS': 'https://circleci.com/api/v1.1/projects?circle-token={}',
    'FOLLOW-NEW-PROJECT': 'https://circleci.com/api/v1.1/project/{}/{}/{}/follow?circle-token={}',
    'BUILD-SUMMARY': 'https://circleci.com/api/v1.1/project/{}/{}/{}?circle-token={}',
    'RECENT-BUILDS': 'https://circleci.com/api/v1.1/recent-builds?circle-token={}',
    'FD-SINGLE-BUILD': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}?circle-token={}',
    'LIST-ARTIFACTS': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}/artifacts?circle-token={}',
    'RETRY-BUILD': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}/retry?circle-token={}',
    'CANCEL-BUILD': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}/cancel?circle-token={}',
    'ADD-USER': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}/ssh-users?circle-token={}',
    'TRIGGER-NEW-BUILD': 'https://circleci.com/api/v1.1/project/{}/{}/{}/tree/{}?circle-token={}',
    'CREATE-SSH': 'https://circleci.com/api/v1.1/project/{}/{}/{}/ssh-key?circle-token={}',
    'LIST-CHECKOUT-KEY': 'https://circleci.com/api/v1.1/project/{}/{}/{}/checkout-key?circle-token={}',  #GET
    'CREATE-CHECKOUT-KEY': 'https://circleci.com/api/v1.1/project/{}/{}/{}/checkout-key?circle-token={}', #POST
    'GET-CHECKOUT-KEY': 'https://circleci.com/api/v1.1/project/{}/{}/{}/checkout-key/{}?circle-token={}', #GET
    'DELETE-CHECKOUT-KEY': 'https://circleci.com/api/v1.1/project/{}/{}/{}/checkout-key/{}?circle-token={}',   #DELETE
    'CLEAR-CACHE': 'https://circleci.com/api/v1.1/project/{}/{}/{}/{}/build-cache?circle-token={}',
    'ADD-KEY-G': 'https://circleci.com/api/v1.1/user/ssh-key?circle-token={}',
    'ADD-KEY-H': 'https://circleci.com/api/v1.1/user/heroku-key?circle-token={}'
}

