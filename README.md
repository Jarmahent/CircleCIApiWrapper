![alt text](http://i.imgur.com/Zzu6tJw.png "Logo Title Text 1")

# CirceCI API Wrapper for Python

### I have created this wrapper for educational purposes and it is not meant to be used for actual working purposes, but feel free to take it and edit it in anyway you like. Just make sure to credit this repo.
   
### Example code:
```python
import circleciclient

token = 'Your token here'

client = circleciClient(token)
me = client.me()
print(me.num_projects_followed)
```
`Output`
```bash
CircleCi Version: 1.1
4
```

# Documentation/ Code Overview

##### All functions return multiple objects

`me()`
_---Returns simple user data---_

##### Objects returned by `me`:

                days_left_in_trial
                trial_end
                basic_email_prefs
                admin
                login
                student
                github_id
                pusher_id
                heroku_api_key
                num_projects_followed
                all_emails

---

`get_project(projectnumber)`

_---Gets project data ---_

##### Objects returned by `get_project`:
            vcs_url
            following
            username
            reponame
            branches

---

`follow_new_project(vcstype, username, project)`

_---Follows a new project---_

##### Objects returned by `follow_new_project`:

            following
            first_build


---

`build_summary(vcstype, username, project, buildnumber)`

_---Returns a summary of the specified build---_

##### Objects returned by `build_summary`:
            vcs_url
            build_url
            build_num
            branch=json
            committer_name
            committer_email
            body
            why
            dont_build
            queued_at
            start_time
            stop_time
            build_time_millis
            username
            reponame
            lifecycle
            outcome
            status
            previous
            retry_of


---

`recent_builds(buildnumber)`

_---Build summary for each of the last 30 recent builds, ordered by build_num---_

##### Objects returned by `build_summary`:
            vcs_url
            build_url
            build_num
            branch=json
            committer_name
            committer_email
            body
            why
            dont_build
            queued_at
            start_time
            stop_time
            build_time_millis
            username
            reponame
            lifecycle
            outcome
            status
            previous
            committer_date

---

`detailed_single_build(vcstype, username, project, buildnumber)`

_---Detailed summary of a single build---_

##### Objects returned by `build_summary`:
            vcs_url
            build_url
            build_num
            branch=json
            committer_name
            committer_email
            body
            why
            dont_build
            queued_at
            start_time
            stop_time
            build_time_millis
            username
            reponame
            lifecycle
            outcome
            status
            previous
            committer_date