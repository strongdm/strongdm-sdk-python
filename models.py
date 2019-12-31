import collections


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# password:
# port:
class Redis:
    __slots__ = [
        'id', 'name', 'healthy', 'hostname', 'port_override', 'password',
        'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.password = None
        self.port = None

    def __repr__(self):
        return '<sdm.Redis id: {0} name: {1} healthy: {2} hostname: {3} port_override: {4} password: {5} port: {6}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.port_override), repr(self.password),
            repr(self.port))


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
        'id', 'name', 'healthy', 'hostname', 'port_override', 'password',
        'port', 'tls_required'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.password = None
        self.port = None
        self.tls_required = None

    def __repr__(self):
        return '<sdm.ElasticacheRedis id: {0} name: {1} healthy: {2} hostname: {3} port_override: {4} password: {5} port: {6} tls_required: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.port_override), repr(self.password),
            repr(self.port), repr(self.tls_required))


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
        'id', 'name', 'healthy', 'hostname', 'port', 'certificate_authority',
        'certificate_authority_filename', 'client_certificate',
        'client_certificate_filename', 'client_key', 'client_key_filename'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port = None
        self.certificate_authority = None
        self.certificate_authority_filename = None
        self.client_certificate = None
        self.client_certificate_filename = None
        self.client_key = None
        self.client_key_filename = None

    def __repr__(self):
        return '<sdm.Kubernetes id: {0} name: {1} healthy: {2} hostname: {3} port: {4} certificate_authority: {5} certificate_authority_filename: {6} client_certificate: {7} client_certificate_filename: {8} client_key: {9} client_key_filename: {10}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.port),
            repr(self.certificate_authority),
            repr(self.certificate_authority_filename),
            repr(self.client_certificate),
            repr(self.client_certificate_filename), repr(self.client_key),
            repr(self.client_key_filename))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port:
# username:
# password:
# certificate_authority:
# certificate_authority_filename:
# client_certificate:
# client_certificate_filename:
# client_key:
# client_key_filename:
class KubernetesBasicAuth:
    __slots__ = [
        'id', 'name', 'healthy', 'hostname', 'port', 'username', 'password',
        'certificate_authority', 'certificate_authority_filename',
        'client_certificate', 'client_certificate_filename', 'client_key',
        'client_key_filename'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port = None
        self.username = None
        self.password = None
        self.certificate_authority = None
        self.certificate_authority_filename = None
        self.client_certificate = None
        self.client_certificate_filename = None
        self.client_key = None
        self.client_key_filename = None

    def __repr__(self):
        return '<sdm.KubernetesBasicAuth id: {0} name: {1} healthy: {2} hostname: {3} port: {4} username: {5} password: {6} certificate_authority: {7} certificate_authority_filename: {8} client_certificate: {9} client_certificate_filename: {10} client_key: {11} client_key_filename: {12}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.port), repr(self.username),
            repr(self.password), repr(self.certificate_authority),
            repr(self.certificate_authority_filename),
            repr(self.client_certificate),
            repr(self.client_certificate_filename), repr(self.client_key),
            repr(self.client_key_filename))


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
        'id', 'name', 'healthy', 'endpoint', 'access_key', 'secret_access_key',
        'certificate_authority', 'certificate_authority_filename', 'region',
        'cluster_name'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.endpoint = None
        self.access_key = None
        self.secret_access_key = None
        self.certificate_authority = None
        self.certificate_authority_filename = None
        self.region = None
        self.cluster_name = None

    def __repr__(self):
        return '<sdm.AmazonEKS id: {0} name: {1} healthy: {2} endpoint: {3} access_key: {4} secret_access_key: {5} certificate_authority: {6} certificate_authority_filename: {7} region: {8} cluster_name: {9}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.endpoint), repr(self.access_key),
            repr(self.secret_access_key), repr(self.certificate_authority),
            repr(self.certificate_authority_filename), repr(self.region),
            repr(self.cluster_name))


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
        'id', 'name', 'healthy', 'endpoint', 'certificate_authority',
        'certificate_authority_filename', 'service_account_key',
        'service_account_key_filename'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.endpoint = None
        self.certificate_authority = None
        self.certificate_authority_filename = None
        self.service_account_key = None
        self.service_account_key_filename = None

    def __repr__(self):
        return '<sdm.GoogleGKE id: {0} name: {1} healthy: {2} endpoint: {3} certificate_authority: {4} certificate_authority_filename: {5} service_account_key: {6} service_account_key_filename: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.endpoint), repr(self.certificate_authority),
            repr(self.certificate_authority_filename),
            repr(self.service_account_key),
            repr(self.service_account_key_filename))


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# username:
# port:
# public_key:
class SSH:
    __slots__ = [
        'id', 'name', 'healthy', 'hostname', 'username', 'port', 'public_key'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.port = None
        self.public_key = None

    def __repr__(self):
        return '<sdm.SSH id: {0} name: {1} healthy: {2} hostname: {3} username: {4} port: {5} public_key: {6}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.port),
            repr(self.public_key))


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
        'id', 'name', 'healthy', 'url', 'healthcheck_path', 'username',
        'password', 'headers_blacklist', 'default_path', 'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.username = None
        self.password = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPBasicAuth id: {0} name: {1} healthy: {2} url: {3} healthcheck_path: {4} username: {5} password: {6} headers_blacklist: {7} default_path: {8} subdomain: {9}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy), repr(self.url),
            repr(self.healthcheck_path), repr(self.username),
            repr(self.password), repr(self.headers_blacklist),
            repr(self.default_path), repr(self.subdomain))


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
        'id', 'name', 'healthy', 'url', 'healthcheck_path',
        'headers_blacklist', 'default_path', 'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPNoAuth id: {0} name: {1} healthy: {2} url: {3} healthcheck_path: {4} headers_blacklist: {5} default_path: {6} subdomain: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy), repr(self.url),
            repr(self.healthcheck_path), repr(self.headers_blacklist),
            repr(self.default_path), repr(self.subdomain))


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
        'id', 'name', 'healthy', 'url', 'healthcheck_path', 'auth_header',
        'headers_blacklist', 'default_path', 'subdomain'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.url = None
        self.healthcheck_path = None
        self.auth_header = None
        self.headers_blacklist = None
        self.default_path = None
        self.subdomain = None

    def __repr__(self):
        return '<sdm.HTTPAuth id: {0} name: {1} healthy: {2} url: {3} healthcheck_path: {4} auth_header: {5} headers_blacklist: {6} default_path: {7} subdomain: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy), repr(self.url),
            repr(self.healthcheck_path), repr(self.auth_header),
            repr(self.headers_blacklist), repr(self.default_path),
            repr(self.subdomain))


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
        'id', 'name', 'healthy', 'hostname', 'username', 'password',
        'database', 'port_override', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Mysql id: {0} name: {1} healthy: {2} hostname: {3} username: {4} password: {5} database: {6} port_override: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.password),
            repr(self.database), repr(self.port_override), repr(self.port))


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
        'id', 'name', 'healthy', 'hostname', 'username', 'password',
        'database', 'port_override', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.AuroraMysql id: {0} name: {1} healthy: {2} hostname: {3} username: {4} password: {5} database: {6} port_override: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.password),
            repr(self.database), repr(self.port_override), repr(self.port))


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
        'id', 'name', 'healthy', 'hostname', 'username', 'password',
        'database', 'port_override', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Clustrix id: {0} name: {1} healthy: {2} hostname: {3} username: {4} password: {5} database: {6} port_override: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.password),
            repr(self.database), repr(self.port_override), repr(self.port))


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
        'id', 'name', 'healthy', 'hostname', 'username', 'password',
        'database', 'port_override', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Maria id: {0} name: {1} healthy: {2} hostname: {3} username: {4} password: {5} database: {6} port_override: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.password),
            repr(self.database), repr(self.port_override), repr(self.port))


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
        'id', 'name', 'healthy', 'hostname', 'username', 'password',
        'database', 'port_override', 'port'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Memsql id: {0} name: {1} healthy: {2} hostname: {3} username: {4} password: {5} database: {6} port_override: {7} port: {8}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.hostname), repr(self.username), repr(self.password),
            repr(self.database), repr(self.port_override), repr(self.port))


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
        'id', 'name', 'healthy', 'access_key', 'secret_access_key', 'output',
        'port_override', 'region'
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.access_key = None
        self.secret_access_key = None
        self.output = None
        self.port_override = None
        self.region = None

    def __repr__(self):
        return '<sdm.Athena id: {0} name: {1} healthy: {2} access_key: {3} secret_access_key: {4} output: {5} port_override: {6} region: {7}>'.format(
            repr(self.id), repr(self.name), repr(self.healthy),
            repr(self.access_key), repr(self.secret_access_key),
            repr(self.output), repr(self.port_override), repr(self.region))


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.CreateResponseMetadata>'.format()


# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.GetResponseMetadata>'.format()


# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.UpdateResponseMetadata>'.format()


# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.DeleteResponseMetadata>'.format()


# RateLimitMetadata contains information about remaining requests avaialable
# to the user over some timeframe.
# limit: How many total requests the user/token is authorized to make before being
# rate limited.
# remaining: How many remaining requests out of the limit are still avaialable.
# reset_at: The time when remaining will be reset to limit.
# bucket: The bucket this user/token is associated with, which may be shared between
# multiple users/tokens.
class RateLimitMetadata:
    __slots__ = ['limit', 'remaining', 'reset_at', 'bucket']

    def __init__(self):
        self.limit = None
        self.remaining = None
        self.reset_at = None
        self.bucket = None

    def __repr__(self):
        return '<sdm.RateLimitMetadata limit: {0} remaining: {1} reset_at: {2} bucket: {3}>'.format(
            repr(self.limit), repr(self.remaining), repr(self.reset_at),
            repr(self.bucket))


# NodeCreateResponse reports how the Nodes were created in the system.
# meta: Reserved for future use.
# node: The created Node.
# token: The auth token generated for the Node. The Node will use this token to
# authenticate with the strongDM API.
# rate_limit: Rate limit information.
class NodeCreateResponse:
    __slots__ = ['meta', 'node', 'token', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.token = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeCreateResponse meta: {0} node: {1} token: {2} rate_limit: {3}>'.format(
            repr(self.meta), repr(self.node), repr(self.token),
            repr(self.rate_limit))


# NodeGetResponse returns a requested Node.
# meta: Reserved for future use.
# node: The requested Node.
# rate_limit: Rate limit information.
class NodeGetResponse:
    __slots__ = ['meta', 'node', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeGetResponse meta: {0} node: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.node), repr(self.rate_limit))


# NodeUpdateResponse returns the fields of a Node after it has been updated by
# a NodeUpdateRequest.
# meta: Reserved for future use.
# node: The updated Node.
# rate_limit: Rate limit information.
class NodeUpdateResponse:
    __slots__ = ['meta', 'node', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeUpdateResponse meta: {0} node: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.node), repr(self.rate_limit))


# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class NodeDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# Relay represents a StrongDM CLI installation running in relay mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the relay. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
class Relay:
    __slots__ = ['id', 'name', 'state']

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None

    def __repr__(self):
        return '<sdm.Relay id: {0} name: {1} state: {2}>'.format(
            repr(self.id), repr(self.name), repr(self.state))


# Gateway represents a StrongDM CLI installation running in gateway mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the gateway. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
# listen_address: The public hostname/port tuple at which the gateway will be accessible to clients.
# bind_address: The hostname/port tuple which the gateway daemon will bind to.
class Gateway:
    __slots__ = ['id', 'name', 'state', 'listen_address', 'bind_address']

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
        self.listen_address = None
        self.bind_address = None

    def __repr__(self):
        return '<sdm.Gateway id: {0} name: {1} state: {2} listen_address: {3} bind_address: {4}>'.format(
            repr(self.id), repr(self.name), repr(self.state),
            repr(self.listen_address), repr(self.bind_address))


# ResourceCreateResponse reports how the Resources were created in the system.
# meta: Reserved for future use.
# resource: The created Resource.
# rate_limit: Rate limit information.
class ResourceCreateResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceCreateResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceGetResponse returns a requested Resource.
# meta: Reserved for future use.
# resource: The requested Resource.
# rate_limit: Rate limit information.
class ResourceGetResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceGetResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceUpdateResponse returns the fields of a Resource after it has been updated by
# a ResourceUpdateRequest.
# meta: Reserved for future use.
# resource: The updated Resource.
# rate_limit: Rate limit information.
class ResourceUpdateResponse:
    __slots__ = ['meta', 'resource', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceUpdateResponse meta: {0} resource: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.resource), repr(self.rate_limit))


# ResourceDeleteResponse returns information about a Resource that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class ResourceDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# RoleAttachmentCreateResponse reports how the RoleAttachments were created in the system.
# meta: Reserved for future use.
# role_attachment: The created RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentCreateResponse:
    __slots__ = ['meta', 'role_attachment', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentCreateResponse meta: {0} role_attachment: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role_attachment), repr(self.rate_limit))


# RoleAttachmentGetResponse returns a requested RoleAttachment.
# meta: Reserved for future use.
# role_attachment: The requested RoleAttachment.
# rate_limit: Rate limit information.
class RoleAttachmentGetResponse:
    __slots__ = ['meta', 'role_attachment', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentGetResponse meta: {0} role_attachment: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role_attachment), repr(self.rate_limit))


# RoleAttachmentDeleteResponse returns information about a RoleAttachment that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleAttachmentDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# A RoleAttachment connects a composite role to another role, granting members
# of the composite role the permissions granted to the attached role.
# id: Unique identifier of the RoleAttachment.
# composite_role_id: The id of the composite role of this RoleAttachment.
# attached_role_id: The id of the attached role of this RoleAttachment.
class RoleAttachment:
    __slots__ = ['id', 'composite_role_id', 'attached_role_id']

    def __init__(self):
        self.id = None
        self.composite_role_id = None
        self.attached_role_id = None

    def __repr__(self):
        return '<sdm.RoleAttachment id: {0} composite_role_id: {1} attached_role_id: {2}>'.format(
            repr(self.id), repr(self.composite_role_id),
            repr(self.attached_role_id))


# RoleCreateResponse reports how the Roles were created in the system. It can
# communicate partial successes or failures.
# meta: Reserved for future use.
# role: The created Role.
# rate_limit: Rate limit information.
class RoleCreateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleCreateResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleGetResponse returns a requested Role.
# meta: Reserved for future use.
# role: The requested Role.
# rate_limit: Rate limit information.
class RoleGetResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleGetResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleUpdateResponse returns the fields of a Role after it has been updated by
# a RoleUpdateRequest.
# meta: Reserved for future use.
# role: The updated Role.
# rate_limit: Rate limit information.
class RoleUpdateResponse:
    __slots__ = ['meta', 'role', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleUpdateResponse meta: {0} role: {1} rate_limit: {2}>'.format(
            repr(self.meta), repr(self.role), repr(self.rate_limit))


# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleDeleteResponse:
    __slots__ = ['meta', 'rate_limit']

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleDeleteResponse meta: {0} rate_limit: {1}>'.format(
            repr(self.meta), repr(self.rate_limit))


# A Role grants users access to a set of resources. Composite roles have no
# resource associations of their own, but instead grant access to the combined
# resources of their child roles.
# id: Unique identifier of the Role.
# name: Unique human-readable name of the Role.
# composite: True if the Role is a composite role.
class Role:
    __slots__ = ['id', 'name', 'composite']

    def __init__(self):
        self.id = None
        self.name = None
        self.composite = None

    def __repr__(self):
        return '<sdm.Role id: {0} name: {1} composite: {2}>'.format(
            repr(self.id), repr(self.name), repr(self.composite))
