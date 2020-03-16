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
import os
sys.path += [
    os.path.normpath(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))
]
import importlib
sdm = importlib.import_module("strongdm-sdk-python")


# listUsers.py enumerates all users of an organization
# usage:
# python3 listUsers.py
def main():
    client = sdm.Client(os.getenv("SDM_API_ACCESS_KEY"),
                        os.getenv("SDM_API_SECRET_KEY"))

    users = client.accounts.list('')
    for user in users:
        print("user " + user.id + ": " + user.email)


if __name__ == "__main__":
    main()
