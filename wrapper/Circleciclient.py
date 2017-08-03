from const import API_PATH, me, __version__, build_summary, follow_project, builds, get_projects, build_artifacts, trigger_build
from requests import get, post, delete, head
from json import loads, dumps
from sys import exit


class circleciClient():
    def __init__(self, token):   #Eventually add version checker
        print('CircleCI Version: {}'.format(__version__))
        self._token = token


    def me(self):
        uri = get(API_PATH['ME'].format(self._token))
        decoded = uri.content.decode('utf-8')
        json = loads(decoded)
        return me(
                days_left_in_trial=json['days_left_in_trial'],
                plan=json['plan'],
                trial_end=json['trial_end'],
                basic_email_prefs=json['basic_email_prefs'],
                admin=json['admin'],
                login=json['login'],
                student=json['student'],
                github_id=json['github_id'],
                pusher_id=json['pusher_id'],
                heroku_api_key=json['heroku_api_key'],
                num_projects_followed=json['num_projects_followed'],
                all_emails=json['all_emails']

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
        followproject = post(API_PATH['FOLLOW-NEW-PROJECT'].format(vcstype, username, project, self._token))
        decoded = followproject.content.decode('utf-8')
        json = loads(decoded)

        return follow_project(
            following = json['following'],
            first_build = json['first_build']
        )
    def build_summary(self, vcstype, username, project, buildnum):
        uri = get(API_PATH['BUILD-SUMMARY'].format(vcstype, username, project, self._token))
        decoded = uri.content.decode('utf-8')
        json = loads(decoded)

        if buildnum not in range(len(json)):
            exit("Bad build Number")

        return build_summary(
            vcs_url=json[buildnum]['vcs_url'],
            build_url=json[buildnum]['build_url'],
            build_num=json[buildnum]['build_num'],
            branch=json[buildnum]['branch'],
            committer_name=json[buildnum]['committer_name'],
            committer_email=json[buildnum]['committer_email'],
            body=json[buildnum]['body'],
            why=json[buildnum]['why'],
            dont_build=json[buildnum]['dont_build'],
            queued_at=json[buildnum]['queued_at'],
            start_time=json[buildnum]['start_time'],
            stop_time=json[buildnum]['stop_time'],
            build_time_millis=json[buildnum]['build_time_millis'],
            username=json[buildnum]['username'],
            reponame=json[buildnum]['reponame'],
            lifecycle=json[buildnum]['lifecycle'],
            outcome=json[buildnum]['outcome'],
            status=json[buildnum]['status'],
            previous=json[buildnum]['previous'],
            retry_of=json[buildnum]['retry_of'],

        )
    def recent_builds(self, buildnum):
        recent = get(API_PATH['RECENT-BUILDS'].format(self._token))
        decoded = recent.content.decode('utf-8')
        json = loads(decoded)

        return builds(
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
        fdsingle = get(API_PATH['FD-SINGLE-BUILD'].format(vcstype, username, project, buildnum, self._token))
        decoded = fdsingle.content.decode('utf-8')
        json = loads(fdsingle)

        return builds(
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
        decoded = artifcats.content.decode('utf-8')
        json = loads(decoded)
        return build_artifacts(
            path = json['path'],
            pretty_path = json['pretty_path'],
            node_index = json['node_index'],
            url = json['url']
        )
    def retry_build(self, vcstype, username, project, buildnum):
        retry = post(API_PATH['RETRY-BUILD'].format(vcstype, username, project, buildnum, self._token))
        decoded = retry.content.decode('utf-8')
        json = loads(decoded)

        return builds(
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
    def cancel_build(self, vcstype, username, project, buildnum):
        cancel = post(API_PATH['CANCEL-BUILD'].format(vcstype, username, project, buildnum, self._token))
        decoded = cancel.content.decode('utf-8')
        json = loads(decoded)

        return builds(
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
    def add_user(self, vcstype, username, project, buildnum):
        adduser = post(API_PATH['ADD-USER'].format(vcstype, username, project, buildnum, self._token))
        decoded = adduser.content.decode('utf-8')
        json = loads(decoded)

        return builds(
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
    def trigger_new_build(self, vcstype, username, project, branch, ):
        triggerbuild = post(API_PATH['TRIGGER-NEW-BUILD'].format(vcstype, username, project, branch, self._token))
        decoded = triggerbuild.content.decode('utf-8')
        json = loads(decoded)

        return trigger_build(
            author_name=json["vcs_url"],
            build_url=json["build_url"],
            reponame=json["reponame"],
            failed=json["failed"],
            infrastructure_fail=json["infrastructure_fail"],
            canceled=json["canceled"],
            previous=json["previous"],
            author_email=json["author_email"],
            why=json["why"],
            build_time_millis=json["build_time_millis"],
            committer_email=json["committer_email"],
            parallel=json["parallel"],
            retries=json["retries"],
            compare=json["compare"],
            dont_build=json["dont_build"],
            committer_name=json["committer_name"],
            usage_queued_at=json["usage_queued_at"],
            branch=json["branch"],
            body=json["body"],
            author_date=json["author_date"],
            node=json["node"],
            committer_date=json["committer_date"],
            start_time=json["start_time"],
            stop_time=json["stop_time"],
            lifecycle=json['lifecycle'],
            user=json["user"],
            messages=json["messages"],
            job_name=json["job_name"],
            retry_of=json['retry_of'],
            previous_successful_build=json["previous_successful_build"],
            outcome=json["outcome"],
            status=json["status"],
            vcs_revision=json["vcs_revision"],
            vcs_tag=json["vcs_tag"],
            build_num=json["build_num"],
            username=json["username"],
            vcs_url=json["vcs_url"],
            timedout=json["timedout"]


        )
    def clear_cache(self, vcstype, username, project):
        clearche = delete(API_PATH['CLEAR-CACHE'].format(vcstype, username, project, self._token))
        decoded = clearche.content.decode('utf-8')
        json = loads(decoded)

        return json['status']
'''
    def create_new_ssh(self, vcstype, username, project):
        ssh = post(API_PATH['CREATE-SSH'].format(vcstype, username, project, self._token))
        json = loads(ssh)
        return ssh.content

       



    def create_checkout_key(self, vcstype, username, project):
        header ={'Content-Type': 'application/json'}
        data = {'type': 'github-user-key'}
        checkout = post(API_PATH['CREATE-CHECKOUT-KEY'].format(vcstype, username, project, self._token), data=dumps(data), headers=header)
        decoded = checkout.content.decode('utf-8')
        json = loads(decoded)
        return decoded

    def get_checkout_key(self, vcstype, username, project, fingerprint):
        getcheckout = get(API_PATH['GET-CHECKOUT-KEY'].format(vcstype, username, project, fingerprint, self._token))
        return getcheckout.content

    def delete_checkout_key(self, vcstype, username, project, fingerprint):
        deletecheckout = delete(API_PATH['DELETE-CHECKOUT-KEY'].format(vcstype, username, project, fingerprint, self._token))
        return deletecheckout.content

    def add_cci_key(self):
        cikey = post(API_PATH['ADD-KEY-G'].format(self._token))
        return cikey.content

    def add_heroku_key(self):
        herokukey = post(API_PATH['ADD-KEY-H'].format(self._token))
        return herokukey.content
'''



