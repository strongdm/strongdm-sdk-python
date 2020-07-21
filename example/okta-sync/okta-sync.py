# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2020 StrongDM Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import yaml
import json
import os
import argparse
import datetime
import strongdm
from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.user.User import User
from okta.models.usergroup.UserGroup import UserGroup


def load_matchers():
    f = open('matchers.yml')
    data = yaml.load(f, Loader=yaml.Loader)
    return data


class OktaUser:
    def __init__(self, login, first_name, last_name, groups):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.groups = groups

    def __repr__(self):
        return "%s %s" % (self.login, self.groups)

    def to_dict(self):
        return {
            'login': self.login,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'groups': self.groups,
        }


def load_okta_users():
    ret = []
    apiClient = ApiClient(pathname='/api/v1/users',
                          base_url=os.getenv('OKTA_CLIENT_ORGURL'),
                          api_token=os.getenv('OKTA_CLIENT_TOKEN'))
    params = {
        'search':
        "profile.department eq \"Engineering\" and (status eq \"ACTIVE\")"
    }
    response = ApiClient.get_path(apiClient, '/', params=params)
    users = Utils.deserialize(response.text, User)
    for u in users:
        response = ApiClient.get_path(apiClient, '/{}/groups'.format(u.id))
        userGroups = Utils.deserialize(response.text, UserGroup)
        groups = []
        for ug in userGroups:
            groups.append(ug.profile.name)
        oktaUser = OktaUser(u.profile.login, u.profile.firstName,
                            u.profile.lastName, groups)
        ret.append(oktaUser)
    return ret


def main():
    parser = argparse.ArgumentParser(
        description='Update StrongDM permissions according to Okta groups')
    parser.add_argument('-p',
                        '--plan',
                        action='store_const',
                        const=True,
                        help='calculate changes but do not apply them')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_const',
                        const=True,
                        help='print detailed report')
    args = parser.parse_args()
    okta_sync(args.plan, args.verbose)


def okta_sync(plan, verbose):
    SDM_API_ACCESS_KEY = os.getenv('SDM_API_ACCESS_KEY')
    SDM_API_SECRET_KEY = os.getenv('SDM_API_SECRET_KEY')
    OKTA_CLIENT_TOKEN = os.getenv('OKTA_CLIENT_TOKEN')
    OKTA_CLIENT_ORGURL = os.getenv('OKTA_CLIENT_ORGURL')

    if SDM_API_ACCESS_KEY is None or SDM_API_SECRET_KEY is None \
        or OKTA_CLIENT_TOKEN is None or OKTA_CLIENT_ORGURL is None:
        print(
            "SDM_API_ACCESS_KEY, SDM_API_SECRET_KEY, OKTA_CLIENT_TOKEN, and OKTA_CLIENT_ORGURL must be set"
        )
        return

    report = {
        'start': str(datetime.datetime.now()),
        'oktaUsersCount': 0,
        'oktaUsers': [],
        'sdmUsersCount': 0,
        'sdmUsers': [],
        'bothUsersCount': 0,
        'sdmResourcesCount': 0,
        'sdmResources': {},
        'permissionsGranted': 0,
        'permissionsRevoked': 0,
        'grants': [],
        'revocations': [],
        'matchers': {},
    }

    matchers = load_matchers()
    okta_users = load_okta_users()

    report['matchers'] = matchers
    report['oktaUsers'] = [x.to_dict() for x in okta_users]
    report['oktaUsersCount'] = len(okta_users)

    client = strongdm.Client(SDM_API_ACCESS_KEY, SDM_API_SECRET_KEY)

    accounts = {o.email: o for o in client.accounts.list('type:user')}
    permissions = [v for v in client.account_grants.list('')]

    report['sdmUsers'] = {k: v.to_dict() for (k, v) in accounts.items()}
    report['sdmUsersCount'] = len(accounts)

    # define current state
    current = {}
    for p in permissions:
        if p.account_id not in current:
            current[p.account_id] = set()
        current[p.account_id].add((p.resource_id, p.id))

    # define desired state
    desired = {}
    overlapping = 0
    for group in matchers["groups"]:
        for resourceQuery in group["resources"]:
            for res in client.resources.list(resourceQuery):
                report['sdmResources'] = res
                for u in okta_users:
                    if group["name"] in u.groups:
                        if u.login not in accounts:
                            continue
                        overlapping += 1
                        aid = accounts[u.login].id
                        if aid not in desired:
                            desired[aid] = set()
                        desired[aid].add(res.id)

    report['bothUsersCount'] = overlapping
    report['sdmResourcesCount'] = len(report['sdmResources'])

    # revoke things
    revocations = 0
    for aid, curRes in current.items():
        desRes = desired.get(aid, set())
        for rid in curRes:
            if rid[0] not in desRes:
                if plan:
                    print('Plan: revoke {} from user {}'.format(rid[1], aid))
                else:
                    client.account_grants.delete(rid[1])
                report['revocations'].append(rid[1])
                revocations += 1
    report['permissionsRevoked'] = revocations

    # grant things
    grants = 0
    for aid, desRes in desired.items():
        curRes = current.get(aid, set())
        for rid in desRes:
            for cr in curRes:
                if rid != cr[0]:
                    ag = strongdm.AccountGrant(resource_id=rid, account_id=aid)
                    if plan:
                        print('Plan: grant {} to user {}'.format(rid, aid))
                    else:
                        ag = client.account_grants.create(ag)
                    report['grants'].append(ag)
                    grants += 1
    report['permissionsGranted'] = grants
    report['complete'] = str(datetime.datetime.now())

    if verbose:
        print(json.dumps(report, indent=4, sort_keys=True))
    else:
        print("{} Okta users, {} strongDM users, {} overlapping users, {} grants, {} revocations".format(\
            len(okta_users),len(accounts), overlapping, grants, revocations))


if __name__ == '__main__':
    main()
