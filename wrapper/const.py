from collections import namedtuple
__version__ = '1.1'

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
      "all_emails",


])

build_summary = namedtuple("build_summary", [
    "vcs_url",
    "build_url",
    "build_num",
    "branch",
    "committer_name",
    "committer_email",
    "subject",
    "body",
    "why",
    "dont_build",
    "queued_at",
    "start_time",
    "stop_time",
    "build_time_millis",
    "username",
    "reponame" ,
    "lifecycle",
    "outcome",
    "status",
    "previous",
    "retry_of",


])

follow_project = namedtuple('follow_project', [
    'following',
    'first_build'
])

build_artifacts = namedtuple('build_artifacts', [
    'path',
    'pretty_path',
    'node_index',
    'url'
])



trigger_build = namedtuple('trigger_build', [
    "author_name",
    "build_url",
    "reponame",
    "failed",
    "infrastructure_fail",
    "canceled",
    "previous",
    "author_email",
    "why",
    "build_time_millis",
    "committer_email",
    "parallel",
    "retries",
    "compare",
    "dont_build",
    "committer_name",
    "usage_queued_at",
    "branch",
    "body",
    "author_date",
    "node",
    "committer_date",
    "start_time",
    "stop_time",
    "lifecycle",
    "user",
    "messages",
    "job_name",
    "retry_of",
    "previous_successful_build",
    "outcome",
    "status",
    "vcs_revision",
    "vcs_tag",
    "build_num",
    "username",
    "vcs_url",
    "timedout",
])



builds = namedtuple('builds', [
  "vcs_url",
  "build_url",
  "build_num",
  "branch",
  "vcs_revision",
  "committer_name",
  "committer_email",
  "subject",
  "body",
  "why",
  "dont_build",
  "queued_at",
  "start_time",
  "stop_time",
  "build_time_millis",
  "username",
  "reponame",
  "lifecycle",
  "outcome",
  "status",
  "retry_of",
  "previous",
  "committer_date"

])
get_projects = namedtuple('get_projects', [
    "vcs_url",
    "following",
    "username",
    "reponame",
    "branches",
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
    'CLEAR-CACHE': 'https://circleci.com/api/v1.1/project/{}/{}/{}/build-cache?circle-token={}',
    'ADD-KEY-G': 'https://circleci.com/api/v1.1/user/ssh-key?circle-token={}',
    'ADD-KEY-H': 'https://circleci.com/api/v1.1/user/heroku-key?circle-token={}'
}

