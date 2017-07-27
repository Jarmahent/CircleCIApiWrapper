from const import API_PATH, me, __version__, build_summary, follow_project, recent_builds, get_projects
from requests import get, post, delete
import webbrowser as wb
from json import loads
from sys import exit


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






    def get_projects(self, projectnum):
        projectsurl = get(API_PATH['PROJECTS'].format(self._token)).content.decode('utf-8')
        json = loads(projectsurl)
        return get_projects(
            vcs_url = json[projectnum]['vcs_url'],
            following=json[projectnum]['following'],
            username=json[projectnum]['username'],
            reponame=json[projectnum]['reponame'],
            branches=json[projectnum]['branches'],
        )
    def follow_new_project(self, vcstype, username, project):
        followproject = post(API_PATH['FOLLOW-NEW-PROJECT'].format(vcstype, username, project, self._token)).content.decode('utf-8')
        f = loads(followproject)

        return follow_project(
            following = f['following'],
            first_build = f['first_build']
        )


    def build_summary(self, vcstype, username, project, buildnum):
        uri = get(API_PATH['BUILD-SUMMARY'].format(vcstype, username, project, self._token))
        cont = uri.content.decode('utf-8')
        j = loads(cont)
        if buildnum not in range(len(j)):
            exit("Bad build Number")


        return build_summary(
            vcs_url=j[buildnum]['vcs_url'],
            build_url=j[buildnum]['build_url'],
            build_num=j[buildnum]['build_num'],
            branch=j[buildnum]['branch'],
            committer_name=j[buildnum]['committer_name'],
            committer_email=j[buildnum]['committer_email'],
            body=j[buildnum]['body'],
            why=j[buildnum]['why'],
            dont_build=j[buildnum]['dont_build'],
            queued_at=j[buildnum]['queued_at'],
            start_time=j[buildnum]['start_time'],
            stop_time=j[buildnum]['stop_time'],
            build_time_millis=j[buildnum]['build_time_millis'],
            username=j[buildnum]['username'],
            reponame=j[buildnum]['reponame'],
            lifecycle=j[buildnum]['lifecycle'],
            outcome=j[buildnum]['outcome'],
            status=j[buildnum]['status'],
            previous=j[buildnum]['previous'],
            retry_of=j[buildnum]['retry_of'],
            subject=j[buildnum]['subject']
        )







    def recent_builds(self, buildnum):
        recent = get(API_PATH['RECENT-BUILDS'].format(self._token)).content.decode('utf-8')
        json = loads(recent)
        return recent_builds(
            vcs_url=json[buildnum]["vcs_url"],
            build_url=json[buildnum]["build_url"],
            build_num=json[buildnum]["build_num"],
            branch=json[buildnum]["branch"],
            vcs_revision=json[buildnum]["vcs_revision"],
            committer_name=json[buildnum]["committer_name"],
            committer_email=json[buildnum]["committer_email"],
            subject=json[buildnum]["subject"],
            body=json[buildnum]["body"],
            why=json[buildnum]["why"],
            dont_build=json[buildnum]["dont_build"],
            queued_at=json[buildnum]["queued_at"],
            start_time=json[buildnum]["start_time"],
            stop_time=json[buildnum]["stop_time"],
            build_time_millis=json[buildnum]["build_time_millis"],
            username=json[buildnum]["username"],
            reponame=json[buildnum]["reponame"],
            lifecycle=json[buildnum]["lifecycle"],
            outcome=json[buildnum]["outcome"],
            status=json[buildnum]["status"],
            retry_of=json[buildnum]["retry_of"],
            previous=json[buildnum]["previous"],
            committer_date = json[buildnum]['committer_date']
        )

    def detailed_single_build(self, vcstype, username, project, buildnum):
        fdsingle = get(API_PATH['FD-SINGLE-BUILD'].format(vcstype, username, project, buildnum, self._token)).content.decode('utf-8')
        json = loads(fdsingle)
        return recent_builds(
            vcs_url=json["vcs_url"],
            build_url=json["build_url"],
            build_num=json["build_num"],
            branch=json["branch"],
            vcs_revision=json["vcs_revision"],
            committer_name=json["committer_name"],
            committer_email=json["committer_email"],
            subject=json["subject"],
            body=json["body"],
            why=json["why"],
            dont_build=json["dont_build"],
            queued_at=json["queued_at"],
            start_time=json["start_time"],
            stop_time=json["stop_time"],
            build_time_millis=json["build_time_millis"],
            username=json["username"],
            reponame=json["reponame"],
            lifecycle=json["lifecycle"],
            outcome=json["outcome"],
            status=json["status"],
            retry_of=json["retry_of"],
            previous=json["previous"],
            committer_date=json['committer_date']
        )

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




