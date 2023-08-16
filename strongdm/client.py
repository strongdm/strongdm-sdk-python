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

# Code generated by protogen. DO NOT EDIT.

import base64
import copy
import datetime
import grpc
import hashlib
import hmac
import random
import time
from . import svc
from . import plumbing

# These defaults are taken from AWS. Customization of these values
# is a future step in the API.
DEFAULT_MAX_RETRIES = 3
DEFAULT_BASE_RETRY_DELAY = 0.0030  # 30 ms
DEFAULT_MAX_RETRY_DELAY = 300  # 300 seconds
API_VERSION = '2021-08-23'
USER_AGENT = 'strongdm-sdk-python/4.3.1'


class Client:
    '''Client interacts with the strongDM API.'''
    def __init__(self,
                 api_access_key,
                 api_secret,
                 host='api.strongdm.com:443',
                 insecure=False,
                 retry_rate_limit_errors=True):
        '''
        Create a new Client.

        - api_access_key: the access key to authenticate with strongDM
        - api_secret: the secret key to authenticate with strongDM
        '''
        self.api_access_key = api_access_key.strip()
        self.api_secret = base64.b64decode(api_secret.strip())
        self.max_retries = DEFAULT_MAX_RETRIES
        self.base_retry_delay = DEFAULT_BASE_RETRY_DELAY
        self.max_retry_delay = DEFAULT_MAX_RETRY_DELAY
        self.expose_rate_limit_errors = (not retry_rate_limit_errors)
        self.snapshot_datetime = None
        self._test_options = {}

        try:
            if insecure:
                channel = grpc.insecure_channel(host)
            else:
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(host, creds)
        except Exception as e:
            raise plumbing.convert_error_to_porcelain(e) from e
        self.channel = channel
        self.access_requests = svc.AccessRequests(channel, self)
        '''
         AccessRequests are requests for access to a resource that may match a Workflow.

        See `strongdm.svc.AccessRequests`.
        '''
        self.access_request_events_history = svc.AccessRequestEventsHistory(
            channel, self)
        '''
         AccessRequestEventsHistory provides records of all changes to the state of an AccessRequest.

        See `strongdm.svc.AccessRequestEventsHistory`.
        '''
        self.access_requests_history = svc.AccessRequestsHistory(channel, self)
        '''
         AccessRequestsHistory provides records of all changes to the state of an AccessRequest.

        See `strongdm.svc.AccessRequestsHistory`.
        '''
        self.account_attachments = svc.AccountAttachments(channel, self)
        '''
         AccountAttachments assign an account to a role.

        See `strongdm.svc.AccountAttachments`.
        '''
        self.account_attachments_history = svc.AccountAttachmentsHistory(
            channel, self)
        '''
         AccountAttachmentsHistory records all changes to the state of an AccountAttachment.

        See `strongdm.svc.AccountAttachmentsHistory`.
        '''
        self.account_grants = svc.AccountGrants(channel, self)
        '''
         AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.

        See `strongdm.svc.AccountGrants`.
        '''
        self.account_grants_history = svc.AccountGrantsHistory(channel, self)
        '''
         AccountGrantsHistory records all changes to the state of an AccountGrant.

        See `strongdm.svc.AccountGrantsHistory`.
        '''
        self.account_permissions = svc.AccountPermissions(channel, self)
        '''
         AccountPermissions records the granular permissions accounts have, allowing them to execute
         relevant commands via StrongDM's APIs.

        See `strongdm.svc.AccountPermissions`.
        '''
        self.account_resources = svc.AccountResources(channel, self)
        '''
         AccountResources enumerates the resources to which accounts have access.
         The AccountResources service is read-only.

        See `strongdm.svc.AccountResources`.
        '''
        self.account_resources_history = svc.AccountResourcesHistory(
            channel, self)
        '''
         AccountResourcesHistory records all changes to the state of a AccountResource.

        See `strongdm.svc.AccountResourcesHistory`.
        '''
        self.accounts = svc.Accounts(channel, self)
        '''
         Accounts are users that have access to strongDM. There are two types of accounts:
         1. **Users:** humans who are authenticated through username and password or SSO.
         2. **Service Accounts:** machines that are authenticated using a service token.

        See `strongdm.svc.Accounts`.
        '''
        self.accounts_history = svc.AccountsHistory(channel, self)
        '''
         AccountsHistory records all changes to the state of an Account.

        See `strongdm.svc.AccountsHistory`.
        '''
        self.activities = svc.Activities(channel, self)
        '''
         An Activity is a record of an action taken against a strongDM deployment, e.g.
         a user creation, resource deletion, sso configuration change, etc. The Activities
         service is read-only.

        See `strongdm.svc.Activities`.
        '''
        self.control_panel = svc.ControlPanel(channel, self)
        '''
         ControlPanel contains all administrative controls.

        See `strongdm.svc.ControlPanel`.
        '''
        self.nodes = svc.Nodes(channel, self)
        '''
         Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
         - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
         - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.

        See `strongdm.svc.Nodes`.
        '''
        self.nodes_history = svc.NodesHistory(channel, self)
        '''
         NodesHistory records all changes to the state of a Node.

        See `strongdm.svc.NodesHistory`.
        '''
        self.organization_history = svc.OrganizationHistory(channel, self)
        '''
         OrganizationHistory records all changes to the state of an Organization.

        See `strongdm.svc.OrganizationHistory`.
        '''
        self.peering_group_nodes = svc.PeeringGroupNodes(channel, self)
        '''
         PeeringGroupNodes provides the building blocks necessary to obtain attach a node to a peering group.

        See `strongdm.svc.PeeringGroupNodes`.
        '''
        self.peering_group_peers = svc.PeeringGroupPeers(channel, self)
        '''
         PeeringGroupPeers provides the building blocks necessary to link two peering groups.

        See `strongdm.svc.PeeringGroupPeers`.
        '''
        self.peering_group_resources = svc.PeeringGroupResources(channel, self)
        '''
         PeeringGroupResources provides the building blocks necessary to obtain attach a resource to a peering group.

        See `strongdm.svc.PeeringGroupResources`.
        '''
        self.peering_groups = svc.PeeringGroups(channel, self)
        '''
         PeeringGroups provides the building blocks necessary to obtain explicit network topology and routing.

        See `strongdm.svc.PeeringGroups`.
        '''
        self.queries = svc.Queries(channel, self)
        '''
         A Query is a record of a single client request to a resource, such as a SQL query.
         Long-running SSH, RDP, or Kubernetes interactive sessions also count as queries.
         The Queries service is read-only.

        See `strongdm.svc.Queries`.
        '''
        self.remote_identities = svc.RemoteIdentities(channel, self)
        '''
         RemoteIdentities assign a resource directly to an account, giving the account the permission to connect to that resource.

        See `strongdm.svc.RemoteIdentities`.
        '''
        self.remote_identities_history = svc.RemoteIdentitiesHistory(
            channel, self)
        '''
         RemoteIdentitiesHistory records all changes to the state of a RemoteIdentity.

        See `strongdm.svc.RemoteIdentitiesHistory`.
        '''
        self.remote_identity_groups = svc.RemoteIdentityGroups(channel, self)
        '''
         A RemoteIdentityGroup is a named grouping of Remote Identities for Accounts.
         An Account's relationship to a RemoteIdentityGroup is defined via RemoteIdentity objects.

        See `strongdm.svc.RemoteIdentityGroups`.
        '''
        self.remote_identity_groups_history = svc.RemoteIdentityGroupsHistory(
            channel, self)
        '''
         RemoteIdentityGroupsHistory records all changes to the state of a RemoteIdentityGroup.

        See `strongdm.svc.RemoteIdentityGroupsHistory`.
        '''
        self.replays = svc.Replays(channel, self)
        '''
         A Replay captures the data transferred over a long-running SSH, RDP, or Kubernetes interactive session
         (otherwise referred to as a query). The Replays service is read-only.

        See `strongdm.svc.Replays`.
        '''
        self.resources = svc.Resources(channel, self)
        '''
         Resources are databases, servers, clusters, websites, or clouds that strongDM
         delegates access to.

        See `strongdm.svc.Resources`.
        '''
        self.resources_history = svc.ResourcesHistory(channel, self)
        '''
         ResourcesHistory records all changes to the state of a Resource.

        See `strongdm.svc.ResourcesHistory`.
        '''
        self.role_resources = svc.RoleResources(channel, self)
        '''
         RoleResources enumerates the resources to which roles have access.
         The RoleResources service is read-only.

        See `strongdm.svc.RoleResources`.
        '''
        self.role_resources_history = svc.RoleResourcesHistory(channel, self)
        '''
         RoleResourcesHistory records all changes to the state of a RoleResource.

        See `strongdm.svc.RoleResourcesHistory`.
        '''
        self.roles = svc.Roles(channel, self)
        '''
         A Role has a list of access rules which determine which Resources the members
         of the Role have access to. An Account can be a member of multiple Roles via
         AccountAttachments.

        See `strongdm.svc.Roles`.
        '''
        self.roles_history = svc.RolesHistory(channel, self)
        '''
         RolesHistory records all changes to the state of a Role.

        See `strongdm.svc.RolesHistory`.
        '''
        self.secret_stores = svc.SecretStores(channel, self)
        '''
         SecretStores are servers where resource secrets (passwords, keys) are stored.

        See `strongdm.svc.SecretStores`.
        '''
        self.secret_stores_history = svc.SecretStoresHistory(channel, self)
        '''
         SecretStoresHistory records all changes to the state of a SecretStore.

        See `strongdm.svc.SecretStoresHistory`.
        '''
        self.workflows = svc.Workflows(channel, self)
        '''
         Workflows are the collection of rules that define the resources to which access can be requested,
         the users that can request that access, and the mechanism for approving those requests which can either
         but automatic approval or a set of users authorized to approve the requests.

        See `strongdm.svc.Workflows`.
        '''
        self.workflow_approvers_history = svc.WorkflowApproversHistory(
            channel, self)
        '''
         WorkflowApproversHistory provides records of all changes to the state of a WorkflowApprover.

        See `strongdm.svc.WorkflowApproversHistory`.
        '''
        self.workflow_assignments_history = svc.WorkflowAssignmentsHistory(
            channel, self)
        '''
         WorkflowAssignmentsHistory provides records of all changes to the state of a WorkflowAssignment.

        See `strongdm.svc.WorkflowAssignmentsHistory`.
        '''
        self.workflow_roles_history = svc.WorkflowRolesHistory(channel, self)
        '''
         WorkflowRolesHistory provides records of all changes to the state of a WorkflowRole

        See `strongdm.svc.WorkflowRolesHistory`.
        '''
        self.workflows_history = svc.WorkflowsHistory(channel, self)
        '''
         WorkflowsHistory provides records of all changes to the state of a Workflow.

        See `strongdm.svc.WorkflowsHistory`.
        '''

    def close(self):
        '''Closes this Client and releases all resources held by it.

        Closing the Client will immediately terminate all RPCs active with the
        Client and it is not valid to invoke new RPCs with the Client.

        This method is idempotent.
        '''
        self.channel.close()

    def get_metadata(self, method_name, req):
        return [
            ('x-sdm-authentication', self.api_access_key),
            ('x-sdm-signature', self.sign(method_name,
                                          req.SerializeToString())),
            ('x-sdm-api-version', API_VERSION),
            ('x-sdm-user-agent', USER_AGENT),
        ]

    def sign(self, method_name, request_bytes):
        def hmac_digest(key, msg_byte_string):
            return hmac.new(key, msg=msg_byte_string,
                            digestmod=hashlib.sha256).digest()

        current_utc_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
        signing_key = hmac_digest(self.api_secret, current_utc_date.encode())
        signing_key = hmac_digest(signing_key, b'sdm_api_v1')

        hash = hashlib.sha256()

        hash.update(method_name.encode())
        hash.update(b'\n')
        hash.update(request_bytes)

        return base64.b64encode(hmac_digest(signing_key, hash.digest()))

    def jitterSleep(self, iter):
        dur_max = self.base_retry_delay * 2**iter
        if (dur_max > self.max_retry_delay):
            dur_max = self.max_retry_delay
        # get a value between 0 and max
        dur = random.random() * dur_max
        time.sleep(dur)

    def shouldRetry(self, iter, err):
        if (iter >= self.max_retries - 1):
            return False
        if not isinstance(err, grpc.RpcError):
            return True
        if (not self.expose_rate_limit_errors
            ) and err.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
            porcelain_err = plumbing.convert_error_to_porcelain(err)
            wait_until = porcelain_err.rate_limit.reset_at
            now = datetime.datetime.now(datetime.timezone.utc)
            sleep_for = (wait_until - now).total_seconds()
            # If timezones or clock drift causes this calculation to fail,
            # wait at most one minute.
            if sleep_for < 0 or sleep_for > 60:
                sleep_for = 60
            time.sleep(sleep_for)
            return True
        return err.code() == grpc.StatusCode.INTERNAL or err.code(
        ) == grpc.StatusCode.UNAVAILABLE

    def snapshot_at(self, snapshot_datetime):
        '''
        Constructs a read-only client that will provide historical data from the provided timestamp.

        See `SnapshotClient`.
        '''
        client = copy.copy(self)
        client.snapshot_datetime = snapshot_datetime
        client.access_requests = svc.AccessRequests(client.channel, client)
        client.account_attachments = svc.AccountAttachments(
            client.channel, client)
        client.account_grants = svc.AccountGrants(client.channel, client)
        client.account_permissions = svc.AccountPermissions(
            client.channel, client)
        client.account_resources = svc.AccountResources(client.channel, client)
        client.accounts = svc.Accounts(client.channel, client)
        client.nodes = svc.Nodes(client.channel, client)
        client.peering_group_nodes = svc.PeeringGroupNodes(
            client.channel, client)
        client.peering_group_peers = svc.PeeringGroupPeers(
            client.channel, client)
        client.peering_group_resources = svc.PeeringGroupResources(
            client.channel, client)
        client.peering_groups = svc.PeeringGroups(client.channel, client)
        client.remote_identities = svc.RemoteIdentities(client.channel, client)
        client.remote_identity_groups = svc.RemoteIdentityGroups(
            client.channel, client)
        client.resources = svc.Resources(client.channel, client)
        client.role_resources = svc.RoleResources(client.channel, client)
        client.roles = svc.Roles(client.channel, client)
        client.secret_stores = svc.SecretStores(client.channel, client)
        client.workflows = svc.Workflows(client.channel, client)
        return SnapshotClient(client)


class SnapshotClient:
    '''SnapshotClient exposes methods to query historical records at a provided timestamp.'''
    def __init__(self, client):
        self.access_requests = svc.SnapshotAccessRequests(
            client.access_requests)
        '''
         AccessRequests are requests for access to a resource that may match a Workflow.

        See `strongdm.svc.SnapshotAccessRequests`.
        '''
        self.account_attachments = svc.SnapshotAccountAttachments(
            client.account_attachments)
        '''
         AccountAttachments assign an account to a role.

        See `strongdm.svc.SnapshotAccountAttachments`.
        '''
        self.account_grants = svc.SnapshotAccountGrants(client.account_grants)
        '''
         AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.

        See `strongdm.svc.SnapshotAccountGrants`.
        '''
        self.account_permissions = svc.SnapshotAccountPermissions(
            client.account_permissions)
        '''
         AccountPermissions records the granular permissions accounts have, allowing them to execute
         relevant commands via StrongDM's APIs.

        See `strongdm.svc.SnapshotAccountPermissions`.
        '''
        self.account_resources = svc.SnapshotAccountResources(
            client.account_resources)
        '''
         AccountResources enumerates the resources to which accounts have access.
         The AccountResources service is read-only.

        See `strongdm.svc.SnapshotAccountResources`.
        '''
        self.accounts = svc.SnapshotAccounts(client.accounts)
        '''
         Accounts are users that have access to strongDM. There are two types of accounts:
         1. **Users:** humans who are authenticated through username and password or SSO.
         2. **Service Accounts:** machines that are authenticated using a service token.

        See `strongdm.svc.SnapshotAccounts`.
        '''
        self.nodes = svc.SnapshotNodes(client.nodes)
        '''
         Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
         - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
         - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.

        See `strongdm.svc.SnapshotNodes`.
        '''
        self.peering_group_nodes = svc.SnapshotPeeringGroupNodes(
            client.peering_group_nodes)
        '''
         PeeringGroupNodes provides the building blocks necessary to obtain attach a node to a peering group.

        See `strongdm.svc.SnapshotPeeringGroupNodes`.
        '''
        self.peering_group_peers = svc.SnapshotPeeringGroupPeers(
            client.peering_group_peers)
        '''
         PeeringGroupPeers provides the building blocks necessary to link two peering groups.

        See `strongdm.svc.SnapshotPeeringGroupPeers`.
        '''
        self.peering_group_resources = svc.SnapshotPeeringGroupResources(
            client.peering_group_resources)
        '''
         PeeringGroupResources provides the building blocks necessary to obtain attach a resource to a peering group.

        See `strongdm.svc.SnapshotPeeringGroupResources`.
        '''
        self.peering_groups = svc.SnapshotPeeringGroups(client.peering_groups)
        '''
         PeeringGroups provides the building blocks necessary to obtain explicit network topology and routing.

        See `strongdm.svc.SnapshotPeeringGroups`.
        '''
        self.remote_identities = svc.SnapshotRemoteIdentities(
            client.remote_identities)
        '''
         RemoteIdentities assign a resource directly to an account, giving the account the permission to connect to that resource.

        See `strongdm.svc.SnapshotRemoteIdentities`.
        '''
        self.remote_identity_groups = svc.SnapshotRemoteIdentityGroups(
            client.remote_identity_groups)
        '''
         A RemoteIdentityGroup is a named grouping of Remote Identities for Accounts.
         An Account's relationship to a RemoteIdentityGroup is defined via RemoteIdentity objects.

        See `strongdm.svc.SnapshotRemoteIdentityGroups`.
        '''
        self.resources = svc.SnapshotResources(client.resources)
        '''
         Resources are databases, servers, clusters, websites, or clouds that strongDM
         delegates access to.

        See `strongdm.svc.SnapshotResources`.
        '''
        self.role_resources = svc.SnapshotRoleResources(client.role_resources)
        '''
         RoleResources enumerates the resources to which roles have access.
         The RoleResources service is read-only.

        See `strongdm.svc.SnapshotRoleResources`.
        '''
        self.roles = svc.SnapshotRoles(client.roles)
        '''
         A Role has a list of access rules which determine which Resources the members
         of the Role have access to. An Account can be a member of multiple Roles via
         AccountAttachments.

        See `strongdm.svc.SnapshotRoles`.
        '''
        self.secret_stores = svc.SnapshotSecretStores(client.secret_stores)
        '''
         SecretStores are servers where resource secrets (passwords, keys) are stored.

        See `strongdm.svc.SnapshotSecretStores`.
        '''
        self.workflows = svc.SnapshotWorkflows(client.workflows)
        '''
         Workflows are the collection of rules that define the resources to which access can be requested,
         the users that can request that access, and the mechanism for approving those requests which can either
         but automatic approval or a set of users authorized to approve the requests.

        See `strongdm.svc.SnapshotWorkflows`.
        '''
