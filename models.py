import collections


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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.port_override = None
        self.port = None
        self.password = None

    def __repr__(self):
        return '<sdm.Sybase ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'password: ' + repr(self.password) + \
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
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
        'port_override',
        'port',
        'username',
        'tls_required',
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.port = None
        self.username = None
        self.tls_required = None

    def __repr__(self):
        return '<sdm.Presto ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'username: ' + repr(self.username) + \
            'tls_required: ' + repr(self.tls_required) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Teradata ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# access_key:
# secret_access_key:
# region:
# port_override:
class AmazonES:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'endpoint',
        'access_key',
        'secret_access_key',
        'region',
        'port_override',
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.endpoint = None
        self.access_key = None
        self.secret_access_key = None
        self.region = None
        self.port_override = None

    def __repr__(self):
        return '<sdm.AmazonES ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'endpoint: ' + repr(self.endpoint) + \
            'access_key: ' + repr(self.access_key) + \
            'secret_access_key: ' + repr(self.secret_access_key) + \
            'region: ' + repr(self.region) + \
            'port_override: ' + repr(self.port_override) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.port_override = None
        self.port = None
        self.tls_required = None

    def __repr__(self):
        return '<sdm.Elastic ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'tls_required: ' + repr(self.tls_required) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.password = None
        self.port = None

    def __repr__(self):
        return '<sdm.Redis ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port_override: ' + repr(self.port_override) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
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
        return '<sdm.ElasticacheRedis ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port_override: ' + repr(self.port_override) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
            'tls_required: ' + repr(self.tls_required) + \
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
        return '<sdm.Kubernetes ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port: ' + repr(self.port) + \
            'certificate_authority: ' + repr(self.certificate_authority) + \
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + \
            'client_certificate: ' + repr(self.client_certificate) + \
            'client_certificate_filename: ' + repr(self.client_certificate_filename) + \
            'client_key: ' + repr(self.client_key) + \
            'client_key_filename: ' + repr(self.client_key_filename) + \
            '>'


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
        'id',
        'name',
        'healthy',
        'hostname',
        'port',
        'username',
        'password',
        'certificate_authority',
        'certificate_authority_filename',
        'client_certificate',
        'client_certificate_filename',
        'client_key',
        'client_key_filename',
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
        return '<sdm.KubernetesBasicAuth ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port: ' + repr(self.port) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'certificate_authority: ' + repr(self.certificate_authority) + \
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + \
            'client_certificate: ' + repr(self.client_certificate) + \
            'client_certificate_filename: ' + repr(self.client_certificate_filename) + \
            'client_key: ' + repr(self.client_key) + \
            'client_key_filename: ' + repr(self.client_key_filename) + \
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
        return '<sdm.AmazonEKS ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'endpoint: ' + repr(self.endpoint) + \
            'access_key: ' + repr(self.access_key) + \
            'secret_access_key: ' + repr(self.secret_access_key) + \
            'certificate_authority: ' + repr(self.certificate_authority) + \
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + \
            'region: ' + repr(self.region) + \
            'cluster_name: ' + repr(self.cluster_name) + \
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
        return '<sdm.GoogleGKE ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'endpoint: ' + repr(self.endpoint) + \
            'certificate_authority: ' + repr(self.certificate_authority) + \
            'certificate_authority_filename: ' + repr(self.certificate_authority_filename) + \
            'service_account_key: ' + repr(self.service_account_key) + \
            'service_account_key_filename: ' + repr(self.service_account_key_filename) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.port = None
        self.port_override = None
        self.tls_required = None

    def __repr__(self):
        return '<sdm.Oracle ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port: ' + repr(self.port) + \
            'port_override: ' + repr(self.port_override) + \
            'tls_required: ' + repr(self.tls_required) + \
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# access_key:
# secret_access_key:
# region:
# port_override:
class DynamoDB:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'endpoint',
        'access_key',
        'secret_access_key',
        'region',
        'port_override',
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.endpoint = None
        self.access_key = None
        self.secret_access_key = None
        self.region = None
        self.port_override = None

    def __repr__(self):
        return '<sdm.DynamoDB ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'endpoint: ' + repr(self.endpoint) + \
            'access_key: ' + repr(self.access_key) + \
            'secret_access_key: ' + repr(self.secret_access_key) + \
            'region: ' + repr(self.region) + \
            'port_override: ' + repr(self.port_override) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.RDP ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# endpoint:
# private_key:
# project:
# port_override:
# username:
class BigQuery:
    __slots__ = [
        'id',
        'name',
        'healthy',
        'endpoint',
        'private_key',
        'project',
        'port_override',
        'username',
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.endpoint = None
        self.private_key = None
        self.project = None
        self.port_override = None
        self.username = None

    def __repr__(self):
        return '<sdm.BigQuery ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'endpoint: ' + repr(self.endpoint) + \
            'private_key: ' + repr(self.private_key) + \
            'project: ' + repr(self.project) + \
            'port_override: ' + repr(self.port_override) + \
            'username: ' + repr(self.username) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.database = None
        self.schema = None
        self.port_override = None

    def __repr__(self):
        return '<sdm.Snowflake ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'schema: ' + repr(self.schema) + \
            'port_override: ' + repr(self.port_override) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.port = None

    def __repr__(self):
        return '<sdm.Memcached ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.Postgres ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.AuroraPostgres ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.Greenplum ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.Cockroach ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.Redshift ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.port = None
        self.public_key = None

    def __repr__(self):
        return '<sdm.SSH ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'port: ' + repr(self.port) + \
            'public_key: ' + repr(self.public_key) + \
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
        return '<sdm.HTTPBasicAuth ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'url: ' + repr(self.url) + \
            'healthcheck_path: ' + repr(self.healthcheck_path) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'headers_blacklist: ' + repr(self.headers_blacklist) + \
            'default_path: ' + repr(self.default_path) + \
            'subdomain: ' + repr(self.subdomain) + \
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
        return '<sdm.HTTPNoAuth ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'url: ' + repr(self.url) + \
            'healthcheck_path: ' + repr(self.healthcheck_path) + \
            'headers_blacklist: ' + repr(self.headers_blacklist) + \
            'default_path: ' + repr(self.default_path) + \
            'subdomain: ' + repr(self.subdomain) + \
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
        return '<sdm.HTTPAuth ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'url: ' + repr(self.url) + \
            'healthcheck_path: ' + repr(self.healthcheck_path) + \
            'auth_header: ' + repr(self.auth_header) + \
            'headers_blacklist: ' + repr(self.headers_blacklist) + \
            'default_path: ' + repr(self.default_path) + \
            'subdomain: ' + repr(self.subdomain) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.username = None
        self.password = None
        self.port_override = None
        self.port = None
        self.tls_required = None

    def __repr__(self):
        return '<sdm.Cassandra ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'tls_required: ' + repr(self.tls_required) + \
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
        return '<sdm.Mysql ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
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
        return '<sdm.AuroraMysql ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
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
        return '<sdm.Clustrix ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
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
        return '<sdm.Maria ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
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
        return '<sdm.Memsql ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            '>'


# id: Unique identifier of the Resource.
# name: Unique human-readable name of the Resource.
# healthy: True if the datasource is reachable and the credentials are valid.
# hostname:
# port_override:
# username:
# password:
# port:
class DruID:
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

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.port_override = None
        self.username = None
        self.password = None
        self.port = None

    def __repr__(self):
        return '<sdm.DruID ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'port_override: ' + repr(self.port_override) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
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
        'port',
        'override_database',
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
        self.override_database = None

    def __repr__(self):
        return '<sdm.SQLServer ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'database: ' + repr(self.database) + \
            'port_override: ' + repr(self.port_override) + \
            'port: ' + repr(self.port) + \
            'override_database: ' + repr(self.override_database) + \
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
class MongoHybrID:
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
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.auth_database = None
        self.port_override = None
        self.username = None
        self.password = None
        self.port = None
        self.replica_set = None
        self.connect_to_replica = None

    def __repr__(self):
        return '<sdm.MongoHybrID ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'auth_database: ' + repr(self.auth_database) + \
            'port_override: ' + repr(self.port_override) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
            'replica_set: ' + repr(self.replica_set) + \
            'connect_to_replica: ' + repr(self.connect_to_replica) + \
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
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.auth_database = None
        self.port_override = None
        self.username = None
        self.password = None
        self.port = None

    def __repr__(self):
        return '<sdm.MongoHost ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'auth_database: ' + repr(self.auth_database) + \
            'port_override: ' + repr(self.port_override) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
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
    ]

    def __init__(self):
        self.id = None
        self.name = None
        self.healthy = None
        self.hostname = None
        self.auth_database = None
        self.port_override = None
        self.username = None
        self.password = None
        self.port = None
        self.replica_set = None
        self.connect_to_replica = None

    def __repr__(self):
        return '<sdm.MongoReplicaSet ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'hostname: ' + repr(self.hostname) + \
            'auth_database: ' + repr(self.auth_database) + \
            'port_override: ' + repr(self.port_override) + \
            'username: ' + repr(self.username) + \
            'password: ' + repr(self.password) + \
            'port: ' + repr(self.port) + \
            'replica_set: ' + repr(self.replica_set) + \
            'connect_to_replica: ' + repr(self.connect_to_replica) + \
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
        return '<sdm.Athena ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'healthy: ' + repr(self.healthy) + \
            'access_key: ' + repr(self.access_key) + \
            'secret_access_key: ' + repr(self.secret_access_key) + \
            'output: ' + repr(self.output) + \
            'port_override: ' + repr(self.port_override) + \
            'region: ' + repr(self.region) + \
            '>'


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.CreateResponseMetadata ' + \
            '>'


# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.GetResponseMetadata ' + \
            '>'


# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []

    def __init__(self):
        pass

    def __repr__(self):
        return '<sdm.UpdateResponseMetadata ' + \
            '>'


# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []

    def __init__(self):
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

    def __init__(self):
        self.limit = None
        self.remaining = None
        self.reset_at = None
        self.bucket = None

    def __repr__(self):
        return '<sdm.RateLimitMetadata ' + \
            'limit: ' + repr(self.limit) + \
            'remaining: ' + repr(self.remaining) + \
            'reset_at: ' + repr(self.reset_at) + \
            'bucket: ' + repr(self.bucket) + \
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

    def __init__(self):
        self.meta = None
        self.node = None
        self.token = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeCreateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'node: ' + repr(self.node) + \
            'token: ' + repr(self.token) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeGetResponse ' + \
            'meta: ' + repr(self.meta) + \
            'node: ' + repr(self.node) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.node = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeUpdateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'node: ' + repr(self.node) + \
            'rate_limit: ' + repr(self.rate_limit) + \
            '>'


# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class NodeDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.NodeDeleteResponse ' + \
            'meta: ' + repr(self.meta) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None

    def __repr__(self):
        return '<sdm.Relay ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'state: ' + repr(self.state) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
        self.listen_address = None
        self.bind_address = None

    def __repr__(self):
        return '<sdm.Gateway ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'state: ' + repr(self.state) + \
            'listen_address: ' + repr(self.listen_address) + \
            'bind_address: ' + repr(self.bind_address) + \
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

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceCreateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'resource: ' + repr(self.resource) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceGetResponse ' + \
            'meta: ' + repr(self.meta) + \
            'resource: ' + repr(self.resource) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.resource = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceUpdateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'resource: ' + repr(self.resource) + \
            'rate_limit: ' + repr(self.rate_limit) + \
            '>'


# ResourceDeleteResponse returns information about a Resource that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class ResourceDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.ResourceDeleteResponse ' + \
            'meta: ' + repr(self.meta) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentCreateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'role_attachment: ' + repr(self.role_attachment) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.role_attachment = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentGetResponse ' + \
            'meta: ' + repr(self.meta) + \
            'role_attachment: ' + repr(self.role_attachment) + \
            'rate_limit: ' + repr(self.rate_limit) + \
            '>'


# RoleAttachmentDeleteResponse returns information about a RoleAttachment that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleAttachmentDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleAttachmentDeleteResponse ' + \
            'meta: ' + repr(self.meta) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.id = None
        self.composite_role_id = None
        self.attached_role_id = None

    def __repr__(self):
        return '<sdm.RoleAttachment ' + \
            'id: ' + repr(self.id) + \
            'composite_role_id: ' + repr(self.composite_role_id) + \
            'attached_role_id: ' + repr(self.attached_role_id) + \
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

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleCreateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'role: ' + repr(self.role) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleGetResponse ' + \
            'meta: ' + repr(self.meta) + \
            'role: ' + repr(self.role) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.meta = None
        self.role = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleUpdateResponse ' + \
            'meta: ' + repr(self.meta) + \
            'role: ' + repr(self.role) + \
            'rate_limit: ' + repr(self.rate_limit) + \
            '>'


# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
# rate_limit: Rate limit information.
class RoleDeleteResponse:
    __slots__ = [
        'meta',
        'rate_limit',
    ]

    def __init__(self):
        self.meta = None
        self.rate_limit = None

    def __repr__(self):
        return '<sdm.RoleDeleteResponse ' + \
            'meta: ' + repr(self.meta) + \
            'rate_limit: ' + repr(self.rate_limit) + \
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

    def __init__(self):
        self.id = None
        self.name = None
        self.composite = None

    def __repr__(self):
        return '<sdm.Role ' + \
            'id: ' + repr(self.id) + \
            'name: ' + repr(self.name) + \
            'composite: ' + repr(self.composite) + \
            '>'
