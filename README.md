![alt text](http://i.imgur.com/Zzu6tJw.png "Logo Title Text 1")

# CirceCI API Wrapper for Python  `V1.1`

### I have created this wrapper for educational purposes and it is not meant to be used for actual working purposes, but feel free to take it and edit it in anyway you like. Just make sure to credit this repo.
   
### Example code:
```python
import circleciClient

token = 'Your token here'

client = circleciClient(token)
me = client.me()
print(me.num_projects_followed)
```
`Output`
```bash
CircleCi Api Version: 1.1
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

---

`list_build_artifacts(vcstype, username, project, buildnumber)`

_---List the build artifacts of a projects build---_

##### Objects returned by `list_build_artifacts`:
            path
            pretty_path
            node_index
            url

---

`retry_build(vcstype, username, project, buildnumber)`

_---Retries build---_

##### Objects returned by `retry_build`:
            vcs_url
            build_url
            build_num
            branch
            vcs_revision
            committer_name
            committer_email
            subject
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
            retry_of
            previous
            committer_date

---

`cancel_build(vcstype, username, project, buildnumber)`

_---Cancels a build---_

##### Objects returned by `cancel_build`:
            vcs_url
            build_url
            build_num
            branch
            vcs_revision
            committer_name
            committer_email
            subject
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
            retry_of
            previous
            committer_date

---

`add_user(vcstype, username, project, buildnumber)`

_---Adds a user to the build's SSH permissions---_

##### Objects returned by `add_user`:
            vcs_url
            build_url
            build_num
            branch
            vcs_revision
            committer_name
            committer_email
            subject
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
            retry_of
            previous
            committer_date

---

`trigger_new_build(vcstype, username, project, branch)`

_---Triggers a new build for project---_

##### Objects returned by `trigger_new_build`:
            author_name
            build_url
            reponame
            failed
            infrastructure_fail
            canceled
            previous
            author_email
            why
            build_time_millis
            committer_email
            parallel
            retries
            compare
            dont_build
            committer_name
            usage_queued_at
            branch
            body
            author_date
            node
            committer_date
            start_time
            stop_time
            lifecycle
            user
            messages
            job_name
            retry_of
            previous_successful_build
            outcome
            status
            vcs_revision
            vcs_tag
            build_num
            username
            vcs_url
            timedout

---

`clear_cache(vcstype, username, project)`

_---Clears cache of a project---_

##### Objects returned by `clear_cache`:
           status
