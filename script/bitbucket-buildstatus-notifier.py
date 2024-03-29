#!/usr/bin/env python
import os
import requests

repo_owner = os.getenv('CF_REPO_OWNER')
repo_slug = os.getenv('CF_REPO_NAME')

repo_auth_user = os.getenv('BB_BSN_REPO_AUTH_USER')
repo_auth_password = os.getenv('BB_BSN_REPO_AUTH_PASSWORD')

if repo_auth_user is None:
    print("Authentication User Environment Variable [BB_BSN_REPO_AUTH_USER] is not defined.")
    exit(2)
    
if repo_auth_password is None:
    print("Authentication Password Environment Variable [BB_BSN_REPO_AUTH_PASSWORD] is not defined.")
    exit(2)

bb_url = os.getenv('BB_BSN_URL', 'https://api.bitbucket.org')

cf_build_id = os.getenv('CF_BUILD_ID')
cf_status = os.getenv('CF_BUILD_STATUS', 'STOPPED') # 'SUCCESSFUL', 'FAILED', 'INPROGRESS', 'STOPPED'
cf_revision = os.getenv('CF_REVISION')
cf_build_url = os.getenv('CF_BUILD_URL')

print('Will Attempt to update build status of commit [{}] to [{}] '.format(cf_revision, cf_status))

data = {
    'key': cf_revision,
    'state': cf_status,
    'name': 'Build [{}]'.format(cf_build_id),
    'url': cf_build_url,
    'description': 'Build [{}] {}'.format(cf_build_id, cf_status)
}

# Construct URL
api_url = ('%(url)s/2.0/repositories/'
           '%(owner)s/%(repo_slug)s/commit/%(revision)s/statuses/build'
           % {'url': bb_url,
              'owner': repo_owner,
              'repo_slug': repo_slug,
              'revision': cf_revision})

print('Sending request to:')
print(api_url)
print('with body')
print(data)

# Post build status to Bitbucket
response = requests.post(api_url, auth=(repo_auth_user, repo_auth_password), json=data)

print('Response:')
print(response)
print(response.text)

if response:
    exit(0)
else:
    exit(1)