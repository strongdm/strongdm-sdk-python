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
import sys
import os.path
import pprint
import time
import json
import os
import strongdm


# panicButton.py suspends all users except for one admin,
# in the fake use case of a critical break in or something
# usage:
# python3 panicButton.py adminuser@email.com
# to revert back to pre-panic state:
# python3 panicButton.py revert
def main():
    access_key = os.getenv("SDM_API_ACCESS_KEY")
    secret_key = os.getenv("SDM_API_SECRET_KEY")
    if access_key is None or secret_key is None:
        print("SDM_API_ACCESS_KEY and SDM_API_SECRET_KEY must be provided")
        return 1

    client = strongdm.Client(access_key, secret_key)

    if len(sys.argv) == 2 and sys.argv[1] == "revert":
        with open('state.json', 'r') as infile:
            state = json.load(infile)

            reinstated_count = 0

            users = client.accounts.list('')
            for user in users:
                if not user.suspended:
                    continue
                reinstated_count += 1
                user.suspended = False
                client.accounts.update(user)
            for attachment in state['attachments']:
                try:
                    client.account_attachments.create(
                        strongdm.AccountAttachment(
                            account_id=attachment["account_id"],
                            role_id=attachment["role_id"]))
                except strongdm.errors.AlreadyExistsError:
                    pass
                except Exception as ex:
                    print("skipping creation of attachment due to error: ",
                          str(ex))
            for grant in state['grants']:
                try:
                    client.account_grants.create(
                        strongdm.AccountGrant(
                            account_id=grant["account_id"],
                            resource_id=grant["resource_id"]))
                except strongdm.errors.AlreadyExistsError:
                    pass
                except Exception as ex:
                    print("skipping creation of grant due to error: ", str(ex))
            print("reinstated " + str(reinstated_count) + " users")
            print("recreated " + str(len(state['attachments'])) +
                  " account attachments")
            print("recreated " + str(len(state['grants'])) + " account grants")
        return

    admin_email = ""
    if len(sys.argv) == 2:
        admin_email = sys.argv[1]
    else:
        print("please provide an admin email to preserve")
        return 1

    admin_user_id = ""
    users = client.accounts.list('email:?', admin_email)
    for user in users:
        admin_user_id = user.id

    account_attachments = client.account_attachments.list('')
    account_grants = client.account_grants.list('')

    state = {
        'attachments': [{
            "account_id": x.account_id,
            "role_id": x.role_id
        } for x in account_attachments if x.account_id != admin_user_id],
        'grants': [{
            "account_id": x.account_id,
            "resource_id": x.resource_id
        } for x in account_grants
                   if x.account_id != admin_user_id and x.valid_until is None],
    }

    print("storing " + str(len(state['attachments'])) +
          " account attachments in state")
    print("storing " + str(len(state['grants'])) + " account grants in state")

    with open('state.json', 'w') as outfile:
        json.dump(state, outfile)

    suspended_count = 0
    users = client.accounts.list('')
    for user in users:
        if isinstance(user, strongdm.User) and user.email == admin_email:
            continue
        user.suspended = True
        try:
            client.accounts.update(user)
            suspended_count += 1
        except Exception as ex:
            print("skipping user " + user.id + " on account of error: " +
                  str(ex))

    print("suspended " + str(suspended_count) + " users ")


if __name__ == "__main__":
    main()
