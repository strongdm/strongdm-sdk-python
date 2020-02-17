import collections


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []

    def __init__(self, ):
        pass

    def __repr__(self):
        return '<sdm.CreateResponseMetadata ' + \
            '>'


# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []

    def __init__(self, ):
        pass

    def __repr__(self):
        return '<sdm.GetResponseMetadata ' + \
            '>'


# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []

    def __init__(self, ):
        pass

    def __repr__(self):
        return '<sdm.UpdateResponseMetadata ' + \
            '>'


# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []

    def __init__(self, ):
        pass

    def __repr__(self):
        return '<sdm.DeleteResponseMetadata ' + \
            '>'


# RateLimitMetadata contains information about remaining requests avaialable
# to the user over some timeframe.
# limit: How many total requests the user/token is authorized to make before being
# rate limited.
# remaining: How many remaining requests out of the limit are still avaialable.
# reset_at: The time when remaining will be reset to limit.
# bucket: The bucket this user/token is associated with, which may be shared between
# multiple users/tokens.
class RateLimitMetadata:
    __slots__ = [
        'limit',
        'remaining',
        'reset_at',
        'bucket',
    ]

    def __init__(
        self,
        limit=None,
        remaining=None,
        reset_at=None,
        bucket=None,
    ):
        self.limit = limit
        self.remaining = remaining
        self.reset_at = reset_at
        self.bucket = bucket

    def __repr__(self):
        return '<sdm.RateLimitMetadata ' + \
            'limit: ' + repr(self.limit) + ' ' +\
            'remaining: ' + repr(self.remaining) + ' ' +\
            'reset_at: ' + repr(self.reset_at) + ' ' +\
            'bucket: ' + repr(self.bucket) + ' ' +\
            '>'


# AccountAttachmentCreateOptions specifies extra options for creating an
# AccountAttachment.
# overwrite: Overwrite clears all account grants before the attachment.
class AccountAttachmentCreateOptions:
    __slots__ = [
        'overwrite',
    ]

    def __init__(
        self,
        overwrite=None,
    ):
        self.overwrite = overwrite

    def __repr__(self):
        return '<sdm.AccountAttachmentCreateOptions ' + \
            'overwrite: ' + repr(self.overwrite) + ' ' +\
            '>'


# AccountAttachmentCreateResponse reports how the AccountAttachments were created in the system.
# meta: Reserved for future use.
# account_attachment: The created AccountAttachment.
# rate_limit: Rate limit information.
class AccountAttachmentCreateResponse:
    __slots__ = [
        'meta',
        'account_attachment',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account_attachment=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account_attachment = account_attachment
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountAttachmentCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account_attachment: ' + repr(self.account_attachment) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountAttachmentGetResponse returns a requested AccountAttachment.
# meta: Reserved for future use.
# account_attachment: The requested AccountAttachment.
# rate_limit: Rate limit information.
class AccountAttachmentGetResponse:
    __slots__ = [
        'meta',
        'account_attachment',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account_attachment=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account_attachment = account_attachment
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountAttachmentGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account_attachment: ' + repr(self.account_attachment) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountAttachmentDeleteResponse returns information about a AccountAttachment that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class AccountAttachmentDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountAttachmentDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A AccountAttachment connects a composite role to another role, granting members
# of the composite role the permissions granted to the attached role.
# id: Unique identifier of the AccountAttachment.
# account_id: The id of the account of this AccountAttachment.
# role_id: The id of the attached role of this AccountAttachment.
class AccountAttachment:
    __slots__ = [
        'id',
        'account_id',
        'role_id',
    ]

    def __init__(
        self,
        id=None,
        account_id=None,
        role_id=None,
    ):
        self.id = id
        self.account_id = account_id
        self.role_id = role_id

    def __repr__(self):
        return '<sdm.AccountAttachment ' + \
            'id: ' + repr(self.id) + ' ' +\
            'account_id: ' + repr(self.account_id) + ' ' +\
            'role_id: ' + repr(self.role_id) + ' ' +\
            '>'


# AccountGrantCreateResponse reports how the AccountGrants were created in the system.
# meta: Reserved for future use.
# account_grant: The created AccountGrant.
# rate_limit: Rate limit information.
class AccountGrantCreateResponse:
    __slots__ = [
        'meta',
        'account_grant',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account_grant=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account_grant = account_grant
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountGrantCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account_grant: ' + repr(self.account_grant) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountGrantGetResponse returns a requested AccountGrant.
# meta: Reserved for future use.
# account_grant: The requested AccountGrant.
# rate_limit: Rate limit information.
class AccountGrantGetResponse:
    __slots__ = [
        'meta',
        'account_grant',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account_grant=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account_grant = account_grant
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountGrantGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account_grant: ' + repr(self.account_grant) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountGrantDeleteResponse returns information about a AccountGrant that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class AccountGrantDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountGrantDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A AccountGrant connects a composite role to another role, granting members
# of the composite role the permissions granted to the attached role.
# id: Unique identifier of the AccountGrant.
# resource_id: The id of the composite role of this AccountGrant.
# account_id: The id of the attached role of this AccountGrant.
# start_from: The timestamp when the resource will be granted. Optional. Both start_at
# and end_at must be defined together, or not defined at all.
# valid_until: The timestamp when the resource grant will expire. Optional. Both
# start_at and end_at must be defined together, or not defined at all.
class AccountGrant:
    __slots__ = [
        'id',
        'resource_id',
        'account_id',
        'start_from',
        'valid_until',
    ]

    def __init__(
        self,
        id=None,
        resource_id=None,
        account_id=None,
        start_from=None,
        valid_until=None,
    ):
        self.id = id
        self.resource_id = resource_id
        self.account_id = account_id
        self.start_from = start_from
        self.valid_until = valid_until

    def __repr__(self):
        return '<sdm.AccountGrant ' + \
            'id: ' + repr(self.id) + ' ' +\
            'resource_id: ' + repr(self.resource_id) + ' ' +\
            'account_id: ' + repr(self.account_id) + ' ' +\
            'start_from: ' + repr(self.start_from) + ' ' +\
            'valid_until: ' + repr(self.valid_until) + ' ' +\
            '>'


# AccountCreateResponse reports how the Accounts were created in the system.
# meta: Reserved for future use.
# account: The created Account.
# token: The auth token generated for the Account. The Account will use this token to
# authenticate with the strongDM API.
# rate_limit: Rate limit information.
class AccountCreateResponse:
    __slots__ = [
        'meta',
        'account',
        'token',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account=None,
        token=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account = account
        self.token = token
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account: ' + repr(self.account) + ' ' +\
            'token: ' + repr(self.token) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountGetResponse returns a requested Account.
# meta: Reserved for future use.
# account: The requested Account.
# rate_limit: Rate limit information.
class AccountGetResponse:
    __slots__ = [
        'meta',
        'account',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account = account
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account: ' + repr(self.account) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountUpdateResponse returns the fields of a Account after it has been updated by
# a AccountUpdateRequest.
# meta: Reserved for future use.
# account: The updated Account.
# rate_limit: Rate limit information.
class AccountUpdateResponse:
    __slots__ = [
        'meta',
        'account',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        account=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.account = account
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountUpdateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'account: ' + repr(self.account) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# AccountDeleteResponse returns information about a Account that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class AccountDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.AccountDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A User can connect to resources they are granted directly, or granted
# via roles.
# id: Unique identifier of the User.
# email: The User's email address. Must be unique.
# first_name: The User's first name.
# last_name: The User's last name.
class User:
    __slots__ = [
        'id',
        'email',
        'first_name',
        'last_name',
    ]

    def __init__(
        self,
        id=None,
        email=None,
        first_name=None,
        last_name=None,
    ):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<sdm.User ' + \
            'id: ' + repr(self.id) + ' ' +\
            'email: ' + repr(self.email) + ' ' +\
            'first_name: ' + repr(self.first_name) + ' ' +\
            'last_name: ' + repr(self.last_name) + ' ' +\
            '>'


# A Service is a service account that can connect to resources they are granted
# directly, or granted via roles. Services are typically automated jobs.
# id: Unique identifier of the Service.
# name: Unique human-readable name of the Service.
class Service:
    __slots__ = [
        'id',
        'name',
    ]

    def __init__(
        self,
        id=None,
        name=None,
    ):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<sdm.Service ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# access_key:
# secret_access_key:
# output:
# port_override:
# region:
class Athena:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'access_key',
        'secret_access_key',
        'output',
        'port_override',
        'region',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        access_key=None,
        secret_access_key=None,
        output=None,
        port_override=None,
        region=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.access_key = access_key
        self.secret_access_key = secret_access_key
        self.output = output
        self.port_override = port_override
        self.region = region

    def __repr__(self):
        return '<sdm.Athena ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'access_key: ' + repr(self.access_key) + ' ' +\
            'secret_access_key: ' + repr(self.secret_access_key) + ' ' +\
            'output: ' + repr(self.output) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'region: ' + repr(self.region) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# private_key:
# project:
# port_override:
# endpoint:
# username:
class BigQuery:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'private_key',
        'project',
        'port_override',
        'endpoint',
        'username',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        private_key=None,
        project=None,
        port_override=None,
        endpoint=None,
        username=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.private_key = private_key
        self.project = project
        self.port_override = port_override
        self.endpoint = endpoint
        self.username = username

    def __repr__(self):
        return '<sdm.BigQuery ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'private_key: ' + repr(self.private_key) + ' ' +\
            'project: ' + repr(self.project) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'endpoint: ' + repr(self.endpoint) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# port_override:
# port:
# tls_required:
class Cassandra:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'port_override',
        'port',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        port_override=None,
        port=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port_override = port_override
        self.port = port
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.Cassandra ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# username:
# password:
# port:
class Druid:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port_override',
        'username',
        'password',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port_override=None,
        username=None,
        password=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port_override = port_override
        self.username = username
        self.password = password
        self.port = port

    def __repr__(self):
        return '<sdm.Druid ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# access_key:
# secret_access_key:
# region:
# endpoint:
# port_override:
class DynamoDB:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'access_key',
        'secret_access_key',
        'region',
        'endpoint',
        'port_override',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        access_key=None,
        secret_access_key=None,
        region=None,
        endpoint=None,
        port_override=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.access_key = access_key
        self.secret_access_key = secret_access_key
        self.region = region
        self.endpoint = endpoint
        self.port_override = port_override

    def __repr__(self):
        return '<sdm.DynamoDB ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'access_key: ' + repr(self.access_key) + ' ' +\
            'secret_access_key: ' + repr(self.secret_access_key) + ' ' +\
            'region: ' + repr(self.region) + ' ' +\
            'endpoint: ' + repr(self.endpoint) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# region:
# secret_access_key:
# endpoint:
# access_key:
# port_override:
class AmazonES:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'region',
        'secret_access_key',
        'endpoint',
        'access_key',
        'port_override',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        region=None,
        secret_access_key=None,
        endpoint=None,
        access_key=None,
        port_override=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.region = region
        self.secret_access_key = secret_access_key
        self.endpoint = endpoint
        self.access_key = access_key
        self.port_override = port_override

    def __repr__(self):
        return '<sdm.AmazonES ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'region: ' + repr(self.region) + ' ' +\
            'secret_access_key: ' + repr(self.secret_access_key) + ' ' +\
            'endpoint: ' + repr(self.endpoint) + ' ' +\
            'access_key: ' + repr(self.access_key) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# port_override:
# port:
# tls_required:
class Elastic:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'port_override',
        'port',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        port_override=None,
        port=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port_override = port_override
        self.port = port
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.Elastic ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# username:
# password:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPBasicAuth:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'url',
        'healthcheck_path',
        'username',
        'password',
        'headers_blacklist',
        'default_path',
        'subdomain',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        url=None,
        healthcheck_path=None,
        username=None,
        password=None,
        headers_blacklist=None,
        default_path=None,
        subdomain=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.url = url
        self.healthcheck_path = healthcheck_path
        self.username = username
        self.password = password
        self.headers_blacklist = headers_blacklist
        self.default_path = default_path
        self.subdomain = subdomain

    def __repr__(self):
        return '<sdm.HTTPBasicAuth ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'url: ' + repr(self.url) + ' ' +\
            'healthcheck_path: ' + repr(self.healthcheck_path) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'headers_blacklist: ' + repr(self.headers_blacklist) + ' ' +\
            'default_path: ' + repr(self.default_path) + ' ' +\
            'subdomain: ' + repr(self.subdomain) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPNoAuth:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'url',
        'healthcheck_path',
        'headers_blacklist',
        'default_path',
        'subdomain',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        url=None,
        healthcheck_path=None,
        headers_blacklist=None,
        default_path=None,
        subdomain=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.url = url
        self.healthcheck_path = healthcheck_path
        self.headers_blacklist = headers_blacklist
        self.default_path = default_path
        self.subdomain = subdomain

    def __repr__(self):
        return '<sdm.HTTPNoAuth ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'url: ' + repr(self.url) + ' ' +\
            'healthcheck_path: ' + repr(self.healthcheck_path) + ' ' +\
            'headers_blacklist: ' + repr(self.headers_blacklist) + ' ' +\
            'default_path: ' + repr(self.default_path) + ' ' +\
            'subdomain: ' + repr(self.subdomain) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# url:
# healthcheck_path:
# auth_header:
# headers_blacklist:
# default_path:
# subdomain:
class HTTPAuth:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'url',
        'healthcheck_path',
        'auth_header',
        'headers_blacklist',
        'default_path',
        'subdomain',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        url=None,
        healthcheck_path=None,
        auth_header=None,
        headers_blacklist=None,
        default_path=None,
        subdomain=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.url = url
        self.healthcheck_path = healthcheck_path
        self.auth_header = auth_header
        self.headers_blacklist = headers_blacklist
        self.default_path = default_path
        self.subdomain = subdomain

    def __repr__(self):
        return '<sdm.HTTPAuth ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'url: ' + repr(self.url) + ' ' +\
            'healthcheck_path: ' + repr(self.healthcheck_path) + ' ' +\
            'auth_header: ' + repr(self.auth_header) + ' ' +\
            'headers_blacklist: ' + repr(self.headers_blacklist) + ' ' +\
            'default_path: ' + repr(self.default_path) + ' ' +\
            'subdomain: ' + repr(self.subdomain) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port:
# certificate_authority:
# certificate_authority_filename:
# client_certificate:
# client_certificate_filename:
# client_key:
# client_key_filename:
class Kubernetes:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port',
        'certificate_authority',
        'certificate_authority_filename',
        'client_certificate',
        'client_certificate_filename',
        'client_key',
        'client_key_filename',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port=None,
        certificate_authority=None,
        certificate_authority_filename=None,
        client_certificate=None,
        client_certificate_filename=None,
        client_key=None,
        client_key_filename=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port = port
        self.certificate_authority = certificate_authority
        self.certificate_authority_filename = certificate_authority_filename
        self.client_certificate = client_certificate
        self.client_certificate_filename = client_certificate_filename
        self.client_key = client_key
        self.client_key_filename = client_key_filename

    def __repr__(self):
        return '<sdm.Kubernetes ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'certificate_authority: ' + repr(self.certificate_authority) + ' ' +\
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + ' ' +\
            'client_certificate: ' + repr(self.client_certificate) + ' ' +\
            'client_certificate_filename: ' + repr(self.client_certificate_filename) + ' ' +\
            'client_key: ' + repr(self.client_key) + ' ' +\
            'client_key_filename: ' + repr(self.client_key_filename) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port:
# username:
# password:
class KubernetesBasicAuth:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port',
        'username',
        'password',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port=None,
        username=None,
        password=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def __repr__(self):
        return '<sdm.KubernetesBasicAuth ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# access_key:
# secret_access_key:
# certificate_authority:
# certificate_authority_filename:
# region:
# cluster_name:
class AmazonEKS:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'endpoint',
        'access_key',
        'secret_access_key',
        'certificate_authority',
        'certificate_authority_filename',
        'region',
        'cluster_name',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        endpoint=None,
        access_key=None,
        secret_access_key=None,
        certificate_authority=None,
        certificate_authority_filename=None,
        region=None,
        cluster_name=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_access_key = secret_access_key
        self.certificate_authority = certificate_authority
        self.certificate_authority_filename = certificate_authority_filename
        self.region = region
        self.cluster_name = cluster_name

    def __repr__(self):
        return '<sdm.AmazonEKS ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'endpoint: ' + repr(self.endpoint) + ' ' +\
            'access_key: ' + repr(self.access_key) + ' ' +\
            'secret_access_key: ' + repr(self.secret_access_key) + ' ' +\
            'certificate_authority: ' + repr(self.certificate_authority) + ' ' +\
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + ' ' +\
            'region: ' + repr(self.region) + ' ' +\
            'cluster_name: ' + repr(self.cluster_name) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# certificate_authority:
# certificate_authority_filename:
# service_account_key:
# service_account_key_filename:
class GoogleGKE:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'endpoint',
        'certificate_authority',
        'certificate_authority_filename',
        'service_account_key',
        'service_account_key_filename',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        endpoint=None,
        certificate_authority=None,
        certificate_authority_filename=None,
        service_account_key=None,
        service_account_key_filename=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.endpoint = endpoint
        self.certificate_authority = certificate_authority
        self.certificate_authority_filename = certificate_authority_filename
        self.service_account_key = service_account_key
        self.service_account_key_filename = service_account_key_filename

    def __repr__(self):
        return '<sdm.GoogleGKE ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'endpoint: ' + repr(self.endpoint) + ' ' +\
            'certificate_authority: ' + repr(self.certificate_authority) + ' ' +\
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + ' ' +\
            'service_account_key: ' + repr(self.service_account_key) + ' ' +\
            'service_account_key_filename: ' + repr(self.service_account_key_filename) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port:
# token:
class KubernetesServiceAccount:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port',
        'token',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port=None,
        token=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port = port
        self.token = token

    def __repr__(self):
        return '<sdm.KubernetesServiceAccount ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'token: ' + repr(self.token) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# port:
class Memcached:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Memcached ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# auth_database:
# port_override:
# username:
# password:
# port:
# replica_set:
# tls_required:
class MongoLegacyHost:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'auth_database',
        'port_override',
        'username',
        'password',
        'port',
        'replica_set',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        auth_database=None,
        port_override=None,
        username=None,
        password=None,
        port=None,
        replica_set=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.auth_database = auth_database
        self.port_override = port_override
        self.username = username
        self.password = password
        self.port = port
        self.replica_set = replica_set
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.MongoLegacyHost ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'auth_database: ' + repr(self.auth_database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'replica_set: ' + repr(self.replica_set) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# auth_database:
# port_override:
# username:
# password:
# port:
# replica_set:
# connect_to_replica:
# tls_required:
class MongoLegacyReplicaset:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'auth_database',
        'port_override',
        'username',
        'password',
        'port',
        'replica_set',
        'connect_to_replica',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        auth_database=None,
        port_override=None,
        username=None,
        password=None,
        port=None,
        replica_set=None,
        connect_to_replica=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.auth_database = auth_database
        self.port_override = port_override
        self.username = username
        self.password = password
        self.port = port
        self.replica_set = replica_set
        self.connect_to_replica = connect_to_replica
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.MongoLegacyReplicaset ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'auth_database: ' + repr(self.auth_database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'replica_set: ' + repr(self.replica_set) + ' ' +\
            'connect_to_replica: ' + repr(self.connect_to_replica) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# auth_database:
# port_override:
# username:
# password:
# port:
# tls_required:
class MongoHost:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'auth_database',
        'port_override',
        'username',
        'password',
        'port',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        auth_database=None,
        port_override=None,
        username=None,
        password=None,
        port=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.auth_database = auth_database
        self.port_override = port_override
        self.username = username
        self.password = password
        self.port = port
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.MongoHost ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'auth_database: ' + repr(self.auth_database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# auth_database:
# port_override:
# username:
# password:
# port:
# replica_set:
# connect_to_replica:
# tls_required:
class MongoReplicaSet:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'auth_database',
        'port_override',
        'username',
        'password',
        'port',
        'replica_set',
        'connect_to_replica',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        auth_database=None,
        port_override=None,
        username=None,
        password=None,
        port=None,
        replica_set=None,
        connect_to_replica=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.auth_database = auth_database
        self.port_override = port_override
        self.username = username
        self.password = password
        self.port = port
        self.replica_set = replica_set
        self.connect_to_replica = connect_to_replica
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.MongoReplicaSet ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'auth_database: ' + repr(self.auth_database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'replica_set: ' + repr(self.replica_set) + ' ' +\
            'connect_to_replica: ' + repr(self.connect_to_replica) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
class Mysql:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Mysql ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
class AuroraMysql:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.AuroraMysql ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
class Clustrix:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Clustrix ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
class Maria:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Maria ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
class Memsql:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Memsql ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port:
# port_override:
# tls_required:
class Oracle:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port',
        'port_override',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port=None,
        port_override=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.port_override = port_override
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.Oracle ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
# override_database:
class Postgres:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.Postgres ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
# override_database:
class AuroraPostgres:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.AuroraPostgres ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
# override_database:
class Greenplum:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.Greenplum ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
# override_database:
class Cockroach:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.Cockroach ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# port:
# override_database:
class Redshift:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.Redshift ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# password:
# database:
# port_override:
# port:
# username:
# tls_required:
class Presto:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'password',
        'database',
        'port_override',
        'port',
        'username',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        password=None,
        database=None,
        port_override=None,
        port=None,
        username=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.password = password
        self.database = database
        self.port_override = port_override
        self.port = port
        self.username = username
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.Presto ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# port_override:
# port:
class RDP:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.RDP ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# password:
# port:
class Redis:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port_override',
        'password',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port_override=None,
        password=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port_override = port_override
        self.password = password
        self.port = port

    def __repr__(self):
        return '<sdm.Redis ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# password:
# port:
# tls_required:
class ElasticacheRedis:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'port_override',
        'password',
        'port',
        'tls_required',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        port_override=None,
        password=None,
        port=None,
        tls_required=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.port_override = port_override
        self.password = password
        self.port = port
        self.tls_required = tls_required

    def __repr__(self):
        return '<sdm.ElasticacheRedis ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'tls_required: ' + repr(self.tls_required) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# schema:
# port_override:
class Snowflake:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'schema',
        'port_override',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        schema=None,
        port_override=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.schema = schema
        self.port_override = port_override

    def __repr__(self):
        return '<sdm.Snowflake ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'schema: ' + repr(self.schema) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# database:
# port_override:
# schema:
# port:
# override_database:
class SQLServer:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'database',
        'port_override',
        'schema',
        'port',
        'override_database',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        database=None,
        port_override=None,
        schema=None,
        port=None,
        override_database=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.port_override = port_override
        self.schema = schema
        self.port = port
        self.override_database = override_database

    def __repr__(self):
        return '<sdm.SQLServer ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'database: ' + repr(self.database) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'schema: ' + repr(self.schema) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'override_database: ' + repr(self.override_database) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# port:
# public_key:
class SSH:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'port',
        'public_key',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        port=None,
        public_key=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.port = port
        self.public_key = public_key

    def __repr__(self):
        return '<sdm.SSH ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'public_key: ' + repr(self.public_key) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# port_override:
# port:
# password:
class Sybase:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'port_override',
        'port',
        'password',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        port_override=None,
        port=None,
        password=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.port_override = port_override
        self.port = port
        self.password = password

    def __repr__(self):
        return '<sdm.Sybase ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# port_override:
# port:
# password:
class SybaseIQ:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'port_override',
        'port',
        'password',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        port_override=None,
        port=None,
        password=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.port_override = port_override
        self.port = port
        self.password = password

    def __repr__(self):
        return '<sdm.SybaseIQ ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# password:
# port_override:
# port:
class Teradata:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'hostname',
        'username',
        'password',
        'port_override',
        'port',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        healthy=None,
        hostname=None,
        username=None,
        password=None,
        port_override=None,
        port=None,
    ):
        self.id = id
        self.name = name
        self.healthy = healthy
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port_override = port_override
        self.port = port

    def __repr__(self):
        return '<sdm.Teradata ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'healthy: ' + repr(self.healthy) + ' ' +\
            'hostname: ' + repr(self.hostname) + ' ' +\
            'username: ' + repr(self.username) + ' ' +\
            'password: ' + repr(self.password) + ' ' +\
            'port_override: ' + repr(self.port_override) + ' ' +\
            'port: ' + repr(self.port) + ' ' +\
            '>'


# NodeCreateResponse reports how the Nodes were created in the system.
# meta: Reserved for future use.
# node: The created Node.
# token: The auth token generated for the Node. The Node will use this token to
# authenticate with the strongDM API.
# rate_limit: Rate limit information.
class NodeCreateResponse:
    __slots__ = [
        'meta',
        'node',
        'token',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        node=None,
        token=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.node = node
        self.token = token
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.NodeCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'node: ' + repr(self.node) + ' ' +\
            'token: ' + repr(self.token) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# NodeGetResponse returns a requested Node.
# meta: Reserved for future use.
# node: The requested Node.
# rate_limit: Rate limit information.
class NodeGetResponse:
    __slots__ = [
        'meta',
        'node',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        node=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.node = node
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.NodeGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'node: ' + repr(self.node) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# NodeUpdateResponse returns the fields of a Node after it has been updated by
# a NodeUpdateRequest.
# meta: Reserved for future use.
# node: The updated Node.
# rate_limit: Rate limit information.
class NodeUpdateResponse:
    __slots__ = [
        'meta',
        'node',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        node=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.node = node
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.NodeUpdateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'node: ' + repr(self.node) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class NodeDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.NodeDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# Relay represents a StrongDM CLI installation running in relay mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the relay. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
class Relay:
    __slots__ = [
        'id',
        'name',
        'state',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        state=None,
    ):
        self.id = id
        self.name = name
        self.state = state

    def __repr__(self):
        return '<sdm.Relay ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'state: ' + repr(self.state) + ' ' +\
            '>'


# Gateway represents a StrongDM CLI installation running in gateway mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the gateway. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
# listen_address: The public hostname/port tuple at which the gateway will be accessible to clients.
# bind_address: The hostname/port tuple which the gateway daemon will bind to.
class Gateway:
    __slots__ = [
        'id',
        'name',
        'state',
        'listen_address',
        'bind_address',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        state=None,
        listen_address=None,
        bind_address=None,
    ):
        self.id = id
        self.name = name
        self.state = state
        self.listen_address = listen_address
        self.bind_address = bind_address

    def __repr__(self):
        return '<sdm.Gateway ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'state: ' + repr(self.state) + ' ' +\
            'listen_address: ' + repr(self.listen_address) + ' ' +\
            'bind_address: ' + repr(self.bind_address) + ' ' +\
            '>'


# ResourceCreateResponse reports how the Resources were created in the system.
# meta: Reserved for future use.
# resource: The created Resource.
# rate_limit: Rate limit information.
class ResourceCreateResponse:
    __slots__ = [
        'meta',
        'resource',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        resource=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.resource = resource
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.ResourceCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'resource: ' + repr(self.resource) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# ResourceGetResponse returns a requested Resource.
# meta: Reserved for future use.
# resource: The requested Resource.
# rate_limit: Rate limit information.
class ResourceGetResponse:
    __slots__ = [
        'meta',
        'resource',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        resource=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.resource = resource
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.ResourceGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'resource: ' + repr(self.resource) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# ResourceUpdateResponse returns the fields of a Resource after it has been updated by
# a ResourceUpdateRequest.
# meta: Reserved for future use.
# resource: The updated Resource.
# rate_limit: Rate limit information.
class ResourceUpdateResponse:
    __slots__ = [
        'meta',
        'resource',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        resource=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.resource = resource
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.ResourceUpdateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'resource: ' + repr(self.resource) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# ResourceDeleteResponse returns information about a Resource that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class ResourceDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.ResourceDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleAttachmentCreateResponse reports how the RoleAttachments were created in the system.
# meta: Reserved for future use.
# role_attachment: The created RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentCreateResponse:
    __slots__ = [
        'meta',
        'role_attachment',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role_attachment=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role_attachment = role_attachment
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleAttachmentCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role_attachment: ' + repr(self.role_attachment) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleAttachmentGetResponse returns a requested RoleAttachment.
# meta: Reserved for future use.
# role_attachment: The requested RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentGetResponse:
    __slots__ = [
        'meta',
        'role_attachment',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role_attachment=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role_attachment = role_attachment
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleAttachmentGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role_attachment: ' + repr(self.role_attachment) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleAttachmentDeleteResponse returns information about a RoleAttachment that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleAttachmentDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleAttachmentDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A RoleAttachment connects a composite role to another role, granting members
# of the composite role the permissions granted to the attached role.
# id: Unique identifier of the RoleAttachment.
# composite_role_id: The id of the composite role of this RoleAttachment.
# attached_role_id: The id of the attached role of this RoleAttachment.
class RoleAttachment:
    __slots__ = [
        'id',
        'composite_role_id',
        'attached_role_id',
    ]

    def __init__(
        self,
        id=None,
        composite_role_id=None,
        attached_role_id=None,
    ):
        self.id = id
        self.composite_role_id = composite_role_id
        self.attached_role_id = attached_role_id

    def __repr__(self):
        return '<sdm.RoleAttachment ' + \
            'id: ' + repr(self.id) + ' ' +\
            'composite_role_id: ' + repr(self.composite_role_id) + ' ' +\
            'attached_role_id: ' + repr(self.attached_role_id) + ' ' +\
            '>'


# RoleGrantCreateResponse reports how the RoleGrants were created in the system.
# meta: Reserved for future use.
# role_grant: The created RoleGrant.
# rate_limit: Rate limit information.
class RoleGrantCreateResponse:
    __slots__ = [
        'meta',
        'role_grant',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role_grant=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role_grant = role_grant
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleGrantCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role_grant: ' + repr(self.role_grant) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleGrantGetResponse returns a requested RoleGrant.
# meta: Reserved for future use.
# role_grant: The requested RoleGrant.
# rate_limit: Rate limit information.
class RoleGrantGetResponse:
    __slots__ = [
        'meta',
        'role_grant',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role_grant=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role_grant = role_grant
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleGrantGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role_grant: ' + repr(self.role_grant) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleGrantDeleteResponse returns information about a RoleGrant that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleGrantDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleGrantDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A RoleGrant connects a resource to a role, granting members of the role
# access to it.
# id: Unique identifier of the RoleGrant.
# resource_id: The id of the resource of this RoleGrant.
# role_id: The id of the attached role of this RoleGrant.
class RoleGrant:
    __slots__ = [
        'id',
        'resource_id',
        'role_id',
    ]

    def __init__(
        self,
        id=None,
        resource_id=None,
        role_id=None,
    ):
        self.id = id
        self.resource_id = resource_id
        self.role_id = role_id

    def __repr__(self):
        return '<sdm.RoleGrant ' + \
            'id: ' + repr(self.id) + ' ' +\
            'resource_id: ' + repr(self.resource_id) + ' ' +\
            'role_id: ' + repr(self.role_id) + ' ' +\
            '>'


# RoleCreateResponse reports how the Roles were created in the system. It can
# communicate partial successes or failures.
# meta: Reserved for future use.
# role: The created Role.
# rate_limit: Rate limit information.
class RoleCreateResponse:
    __slots__ = [
        'meta',
        'role',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role = role
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleCreateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role: ' + repr(self.role) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleGetResponse returns a requested Role.
# meta: Reserved for future use.
# role: The requested Role.
# rate_limit: Rate limit information.
class RoleGetResponse:
    __slots__ = [
        'meta',
        'role',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role = role
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleGetResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role: ' + repr(self.role) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleUpdateResponse returns the fields of a Role after it has been updated by
# a RoleUpdateRequest.
# meta: Reserved for future use.
# role: The updated Role.
# rate_limit: Rate limit information.
class RoleUpdateResponse:
    __slots__ = [
        'meta',
        'role',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        role=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.role = role
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleUpdateResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'role: ' + repr(self.role) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(
        self,
        meta=None,
        rate_limit=None,
    ):
        self.meta = meta
        self.rate_limit = rate_limit

    def __repr__(self):
        return '<sdm.RoleDeleteResponse ' + \
            'meta: ' + repr(self.meta) + ' ' +\
            'rate_limit: ' + repr(self.rate_limit) + ' ' +\
            '>'


# A Role grants users access to a set of resources. Composite roles have no
# resource associations of their own, but instead grant access to the combined
# resources of their child roles.
# id: Unique identifier of the Role.
# name: Unique human-readable name of the Role.
# composite: True if the Role is a composite role.
class Role:
    __slots__ = [
        'id',
        'name',
        'composite',
    ]

    def __init__(
        self,
        id=None,
        name=None,
        composite=None,
    ):
        self.id = id
        self.name = name
        self.composite = composite

    def __repr__(self):
        return '<sdm.Role ' + \
            'id: ' + repr(self.id) + ' ' +\
            'name: ' + repr(self.name) + ' ' +\
            'composite: ' + repr(self.composite) + ' ' +\
            '>'
