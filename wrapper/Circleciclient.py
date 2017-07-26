from const import API_PATH, me, __version__, build_summary
from requests import get, post, delete
import webbrowser as wb
from json import loads



class CircleciClient():
    def __init__(self, token):   #Eventually add version checker
        print('CircleCI Version: {}'.format(__version__))
        self._token = token


    def me(self):
        uri = get(API_PATH['ME'].format(self._token))
        cont = uri.content.decode('utf-8')
        j = loads(cont)
        return me(
                days_left_in_trial=j['days_left_in_trial'],
                plan=j['plan'],
                trial_end=j['trial_end'],
                basic_email_prefs=j['basic_email_prefs'],
                admin=j['admin'],
                login=j['login'],
                student=j['student'],
                github_id=j['github_id'],
                pusher_id=j['pusher_id'],
                heroku_api_key=j['heroku_api_key'],
                num_projects_followed=j['num_projects_followed'],
                all_emails=j['all_emails']

            )






    def get_projects(self):
        projectsurl = get(API_PATH['PROJECTS'].format(self._token)).content.decode('utf-8')

    def follow_new_project(self, vcstype, username, project):
        followproject = post(API_PATH['FOLLOW-NEW-PROJECT'].format(vcstype, username, project, self._token))


    def build_summary(self, vcstype, username, project):
        uri = get(API_PATH['BUILD-SUMMARY'].format(vcstype, username, project, self._token))
        cont = uri.content.decode('utf-8')
        j = loads(cont)
        return build_summary(
            vcs_url=j[0]['vcs_url'],
            build_url=j[0]['build_url'],
            build_num=j[0]['build_num'],
            branch=j[0]['branch'],
            committer_name=j[0]['committer_name'],
            committer_email=j[0]['committer_email'],
            body=j[0]['body'],
            why=j[0]['why'],
            dont_build=j[0]['dont_build'],
            queued_at=j[0]['queued_at'],
            start_time=j[0]['start_time'],
            stop_time=j[0]['stop_time'],
            build_time_millis=j[0]['build_time_millis'],
            username=j[0]['username'],
            reponame=j[0]['reponame'],
            lifecycle=j[0]['lifecycle'],
            outcome=j[0]['outcome'],
            status=j[0]['status'],
            previous=j[0]['previous'],
            retry_of=j[0]['retry_of'],
            subject=j[0]['subject']




        )


    def recent_builds(self,):
        recent = get(API_PATH['RECENT-BUILDS'].format(self._token))
        #wb.open(API_PATH['RECENT-BUILDS'].format(self._token)) Open Browser
        return recent.content

    def fd_single_build(self, vcstype, username, project, buildnum):
        fdsingle = get(API_PATH['FD-SINGLE-BUILD'].format(vcstype, username, project, buildnum, self._token))
        #wb.open(API_PATH['FD-SINGLE-BUILD'].format(vcstype, username, project, buildnum, self._token))
        return fdsingle.content

    def list_build_artifacts(self, vcstype, username, project, buildnum):
        artifcats = get(API_PATH['LIST-ARTIFACTS'].format(vcstype, username, project, buildnum, self._token))
        #wb.open(API_PATH['LIST-ARTIFACTS'].format(vcstype, username, project, buildnum, self._token))
        return artifcats.content

    def retry_build(self, vcstype, username, project, buildnum):
        retry = post(API_PATH['RETRY-BUILD'].format(vcstype, username, project, buildnum, self._token))
        return retry.content

    def cancel_build(self, vcstype, username, project, buildnum):
        cancel = post(API_PATH['CANCEL-BUILD'].format(vcstype, username, project, buildnum, self._token))
        return cancel.content

    def add_user(self, vcstype, username, project, buildnum):
        adduser = post(API_PATH['ADD-USER'].format(vcstype, username, project, buildnum, self._token))
        wb.open(API_PATH['ADD-USER'].format(vcstype, username, project, buildnum, self._token))
        return adduser.content

    def trigger_new_build(self, vcstype, username, project, branch):
        triggerbuild = get(API_PATH['TRIGGER-NEW-BUILD'].format(vcstype, username, project, branch, self._token))
        return triggerbuild.content

    def create_new_ssh(self, vcstype, username, project):
        ssh = post(API_PATH['CREATE-SSH'].format(vcstype, username, project, self._token))
        #wb.open(API_PATH['CREATE-SSH'].format(vcstype, username, project, self._token))
        return ssh.content

    def create_checkout_key(self, vcstype, username, project):
        checkout = get(API_PATH['GET-CHECKOUT-KEY'].format(vcstype, username, project, self._token))
        return checkout.content

    def get_checkout_key(self, vcstype, username, project, fingerprint):
        getcheckout = get(API_PATH['GET-CHECKOUT-KEY'].format(vcstype, username, project, fingerprint, self._token))
        return getcheckout.content

    def delete_checkout_key(self, vcstype, username, project, fingerprint):
        deletecheckout = delete(API_PATH['DELETE-CHECKOUT-KEY'].format(vcstype, username, project, fingerprint, self._token))
        return deletecheckout.content

    def clear_cache(self, vcstype, username, project):
        clearche = delete(API_PATH['CLEAR-CACHE'].format(vcstype, username, project, self._token))
        return clearche.content

    def add_cci_key(self):
        cikey = post(API_PATH['ADD-KEY-G'].format(self._token))
        return cikey.content

    def add_heroku_key(self):
        herokukey = post(API_PATH['ADD-KEY-H'].format(self._token))
        return herokukey.content




