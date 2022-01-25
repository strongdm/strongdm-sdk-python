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
import os
import random
import strongdm as sdm


def create_example_resource(client):
    # create a redis
    redis = sdm.Redis(
        name="exampleRedis-%s" % random.randint(0, 100000),
        hostname="example.com",
        port_override=random.randint(3000, 20000),
        tags={"env": "staging"},
    )
    return client.resources.create(redis).resource.id


def create_example_role(client, access_rules):
    resp = client.roles.create(
        sdm.Role(
            name="exampleRole-%s" % random.randint(0, 100000),
            access_rules=access_rules,
        ))
    return resp.role.id


def create_and_update_access_rules(client):
    redis_id = create_example_resource(client)

    # create a role with initial access rule
    access_rules = [{"ids": [redis_id]}]
    role_id = client.roles.create(
        sdm.Role(
            name="exampleRole-%s" % random.randint(0, 100000),
            access_rules=access_rules,
        )).role.id

    # update access rules
    role = client.roles.get(role_id).role
    role.access_rules = [{"tags": {"env": "staging"}}, {"type": "redis"}]

    client.roles.update(role)


def create_role_grant_via_access_rules(client):
    resource1_id = create_example_resource(client)
    resource2_id = create_example_resource(client)
    role_id = create_example_role(client, [{"ids": [resource1_id]}])

    # add resource2's id to the role's access rules
    role = client.roles.get(role_id).role
    role.access_rules[0]["ids"].append(resource2_id)
    client.roles.update(role).role


def delete_role_grant_via_access_rules(client):
    resource1_id = create_example_resource(client)
    resource2_id = create_example_resource(client)
    role_id = create_example_role(client, [{
        "ids": [resource1_id, resource2_id]
    }])

    # remove the ID of the second resource
    role = client.roles.get(role_id).role
    role.access_rules[0]["ids"].remove(resource2_id)
    client.roles.update(role)


def list_role_grants_via_access_rules(client):
    resource_id = create_example_resource(client)
    role_id = create_example_role(client, [{"ids": [resource_id]}])

    # role.access_rules contains each AccessRule associated with the role
    role = client.roles.get(role_id).role
    print(role.access_rules[0]["ids"])


# accessRules.py demonstrates usage of access rules
# usage:
# python3 accessRules.py
def main():
    client = sdm.Client(os.getenv("SDM_API_ACCESS_KEY"),
                        os.getenv("SDM_API_SECRET_KEY"))

    # Each of the following functions is an example of how to do an operation using Access Rules

    create_and_update_access_rules(client)

    # The RoleGrants API has been deprecated in favor of Access Rules.
    # When using Access Rules the best practice is to grant Resources access based on Type and Tags.
    # If it is _necessary_ to grant access to specific Resources in the same way as RoleGrants did,
    # you can use Resource IDs directly in Access Rules as shown in the following examples.

    create_role_grant_via_access_rules(client)
    delete_role_grant_via_access_rules(client)
    list_role_grants_via_access_rules(client)


if __name__ == "__main__":
    main()
