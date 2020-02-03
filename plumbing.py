import grpc
import google.rpc as rpc
import json
from google.rpc import status_pb2
from . import errors
from . import models
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from .options_pb2 import *
from .spec_pb2 import *
from .account_grants_pb2 import *
from .accounts_pb2 import *
from .drivers_pb2 import *
from .nodes_pb2 import *
from .resources_pb2 import *
from .role_attachments_pb2 import *
from .roles_pb2 import *


def quote_filter_args(filter, *args):
    parts = filter.split("?")
    if len(parts) != len(args) + 1:
        raise errors.BadRequestError("incorrect number of replacements")
    b = ""
    for i, v in enumerate(parts):
        b += v
        if i < len(args):
            s = str(args[i])
            s = json.dumps(s)
            b += s
    return b


def timestamp_to_porcelain(t):
    return t.ToDatetime()


def timestamp_to_plumbing(t):
    res = Timestamp()
    res.FromDatetime(t)
    return res


def create_response_metadata_to_porcelain(plumbing):
    porcelain = models.CreateResponseMetadata()
    return porcelain


def create_response_metadata_to_plumbing(porcelain):
    plumbing = CreateResponseMetadata()
    return plumbing


def repeated_create_response_metadata_to_plumbing(porcelains):
    return [
        create_response_metadata_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_create_response_metadata_to_porcelain(plumbings):
    return [
        create_response_metadata_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def get_response_metadata_to_porcelain(plumbing):
    porcelain = models.GetResponseMetadata()
    return porcelain


def get_response_metadata_to_plumbing(porcelain):
    plumbing = GetResponseMetadata()
    return plumbing


def repeated_get_response_metadata_to_plumbing(porcelains):
    return [
        get_response_metadata_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_get_response_metadata_to_porcelain(plumbings):
    return [
        get_response_metadata_to_porcelain(plumbing) for plumbing in plumbings
    ]


def update_response_metadata_to_porcelain(plumbing):
    porcelain = models.UpdateResponseMetadata()
    return porcelain


def update_response_metadata_to_plumbing(porcelain):
    plumbing = UpdateResponseMetadata()
    return plumbing


def repeated_update_response_metadata_to_plumbing(porcelains):
    return [
        update_response_metadata_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_update_response_metadata_to_porcelain(plumbings):
    return [
        update_response_metadata_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def delete_response_metadata_to_porcelain(plumbing):
    porcelain = models.DeleteResponseMetadata()
    return porcelain


def delete_response_metadata_to_plumbing(porcelain):
    plumbing = DeleteResponseMetadata()
    return plumbing


def repeated_delete_response_metadata_to_plumbing(porcelains):
    return [
        delete_response_metadata_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_delete_response_metadata_to_porcelain(plumbings):
    return [
        delete_response_metadata_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def rate_limit_metadata_to_porcelain(plumbing):
    porcelain = models.RateLimitMetadata()
    porcelain.limit = plumbing.limit
    porcelain.remaining = plumbing.remaining
    porcelain.reset_at = timestamp_to_porcelain(plumbing.reset_at)
    porcelain.bucket = plumbing.bucket
    return porcelain


def rate_limit_metadata_to_plumbing(porcelain):
    plumbing = RateLimitMetadata()
    if porcelain.limit != None:
        plumbing.limit = porcelain.limit
    if porcelain.remaining != None:
        plumbing.remaining = porcelain.remaining
    if porcelain.reset_at != None:
        plumbing.reset_at = timestamp_to_plumbing(porcelain.reset_at)
    if porcelain.bucket != None:
        plumbing.bucket = porcelain.bucket
    return plumbing


def repeated_rate_limit_metadata_to_plumbing(porcelains):
    return [
        rate_limit_metadata_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_rate_limit_metadata_to_porcelain(plumbings):
    return [
        rate_limit_metadata_to_porcelain(plumbing) for plumbing in plumbings
    ]


def account_grant_create_response_to_porcelain(plumbing):
    porcelain = models.AccountGrantCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.account_grant = account_grant_to_porcelain(
        plumbing.account_grant)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_grant_create_response_to_plumbing(porcelain):
    plumbing = AccountGrantCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.account_grant != None:
        plumbing.account_grant = account_grant_to_plumbing(
            porcelain.account_grant)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_grant_create_response_to_plumbing(porcelains):
    return [
        account_grant_create_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_grant_create_response_to_porcelain(plumbings):
    return [
        account_grant_create_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_grant_get_response_to_porcelain(plumbing):
    porcelain = models.AccountGrantGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.account_grant = account_grant_to_porcelain(
        plumbing.account_grant)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_grant_get_response_to_plumbing(porcelain):
    plumbing = AccountGrantGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.account_grant != None:
        plumbing.account_grant = account_grant_to_plumbing(
            porcelain.account_grant)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_grant_get_response_to_plumbing(porcelains):
    return [
        account_grant_get_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_grant_get_response_to_porcelain(plumbings):
    return [
        account_grant_get_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_grant_delete_response_to_porcelain(plumbing):
    porcelain = models.AccountGrantDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_grant_delete_response_to_plumbing(porcelain):
    plumbing = AccountGrantDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_grant_delete_response_to_plumbing(porcelains):
    return [
        account_grant_delete_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_grant_delete_response_to_porcelain(plumbings):
    return [
        account_grant_delete_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_grant_to_porcelain(plumbing):
    porcelain = models.AccountGrant()
    porcelain.id = plumbing.id
    porcelain.resource_id = plumbing.resource_id
    porcelain.account_id = plumbing.account_id
    porcelain.start_from = timestamp_to_porcelain(plumbing.start_from)
    porcelain.valid_until = timestamp_to_porcelain(plumbing.valid_until)
    return porcelain


def account_grant_to_plumbing(porcelain):
    plumbing = AccountGrant()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.resource_id != None:
        plumbing.resource_id = porcelain.resource_id
    if porcelain.account_id != None:
        plumbing.account_id = porcelain.account_id
    if porcelain.start_from != None:
        plumbing.start_from = timestamp_to_plumbing(porcelain.start_from)
    if porcelain.valid_until != None:
        plumbing.valid_until = timestamp_to_plumbing(porcelain.valid_until)
    return plumbing


def repeated_account_grant_to_plumbing(porcelains):
    return [account_grant_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_account_grant_to_porcelain(plumbings):
    return [account_grant_to_porcelain(plumbing) for plumbing in plumbings]


def account_create_response_to_porcelain(plumbing):
    porcelain = models.AccountCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.account = account_to_porcelain(plumbing.account)
    porcelain.token = plumbing.token
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_create_response_to_plumbing(porcelain):
    plumbing = AccountCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.account != None:
        plumbing.account = account_to_plumbing(porcelain.account)
    if porcelain.token != None:
        plumbing.token = porcelain.token
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_create_response_to_plumbing(porcelains):
    return [
        account_create_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_create_response_to_porcelain(plumbings):
    return [
        account_create_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_get_response_to_porcelain(plumbing):
    porcelain = models.AccountGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.account = account_to_porcelain(plumbing.account)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_get_response_to_plumbing(porcelain):
    plumbing = AccountGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.account != None:
        plumbing.account = account_to_plumbing(porcelain.account)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_get_response_to_plumbing(porcelains):
    return [
        account_get_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_account_get_response_to_porcelain(plumbings):
    return [
        account_get_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def account_update_response_to_porcelain(plumbing):
    porcelain = models.AccountUpdateResponse()
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    porcelain.account = account_to_porcelain(plumbing.account)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_update_response_to_plumbing(porcelain):
    plumbing = AccountUpdateResponse()
    if porcelain.meta != None:
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.account != None:
        plumbing.account = account_to_plumbing(porcelain.account)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_update_response_to_plumbing(porcelains):
    return [
        account_update_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_update_response_to_porcelain(plumbings):
    return [
        account_update_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_delete_response_to_porcelain(plumbing):
    porcelain = models.AccountDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def account_delete_response_to_plumbing(porcelain):
    plumbing = AccountDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_account_delete_response_to_plumbing(porcelains):
    return [
        account_delete_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_account_delete_response_to_porcelain(plumbings):
    return [
        account_delete_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def account_to_plumbing(porcelain):
    plumbing = Account()
    if isinstance(porcelain, models.User):
        plumbing.user.CopyFrom(user_to_plumbing(porcelain))
    if isinstance(porcelain, models.Service):
        plumbing.service.CopyFrom(service_to_plumbing(porcelain))
    return plumbing


def account_to_porcelain(plumbing):
    if plumbing.HasField('user'):
        return user_to_porcelain(plumbing.user)
    if plumbing.HasField('service'):
        return service_to_porcelain(plumbing.service)
    return None


def repeated_account_to_plumbing(porcelains):
    return [account_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_account_to_porcelain(plumbings):
    return [account_to_porcelain(plumbing) for plumbing in plumbings]


def user_to_porcelain(plumbing):
    porcelain = models.User()
    porcelain.id = plumbing.id
    porcelain.email = plumbing.email
    porcelain.first_name = plumbing.first_name
    porcelain.last_name = plumbing.last_name
    return porcelain


def user_to_plumbing(porcelain):
    plumbing = User()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.email != None:
        plumbing.email = porcelain.email
    if porcelain.first_name != None:
        plumbing.first_name = porcelain.first_name
    if porcelain.last_name != None:
        plumbing.last_name = porcelain.last_name
    return plumbing


def repeated_user_to_plumbing(porcelains):
    return [user_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_user_to_porcelain(plumbings):
    return [user_to_porcelain(plumbing) for plumbing in plumbings]


def service_to_porcelain(plumbing):
    porcelain = models.Service()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    return porcelain


def service_to_plumbing(porcelain):
    plumbing = Service()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    return plumbing


def repeated_service_to_plumbing(porcelains):
    return [service_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_service_to_porcelain(plumbings):
    return [service_to_porcelain(plumbing) for plumbing in plumbings]


def resource_to_plumbing(porcelain):
    plumbing = Resource()
    if isinstance(porcelain, models.Athena):
        plumbing.athena.CopyFrom(athena_to_plumbing(porcelain))
    if isinstance(porcelain, models.BigQuery):
        plumbing.big_query.CopyFrom(big_query_to_plumbing(porcelain))
    if isinstance(porcelain, models.Cassandra):
        plumbing.cassandra.CopyFrom(cassandra_to_plumbing(porcelain))
    if isinstance(porcelain, models.Druid):
        plumbing.druid.CopyFrom(druid_to_plumbing(porcelain))
    if isinstance(porcelain, models.DynamoDB):
        plumbing.dynamo_db.CopyFrom(dynamo_db_to_plumbing(porcelain))
    if isinstance(porcelain, models.AmazonES):
        plumbing.amazon_es.CopyFrom(amazon_es_to_plumbing(porcelain))
    if isinstance(porcelain, models.Elastic):
        plumbing.elastic.CopyFrom(elastic_to_plumbing(porcelain))
    if isinstance(porcelain, models.HTTPBasicAuth):
        plumbing.http_basic_auth.CopyFrom(
            http_basic_auth_to_plumbing(porcelain))
    if isinstance(porcelain, models.HTTPNoAuth):
        plumbing.http_no_auth.CopyFrom(http_no_auth_to_plumbing(porcelain))
    if isinstance(porcelain, models.HTTPAuth):
        plumbing.http_auth.CopyFrom(http_auth_to_plumbing(porcelain))
    if isinstance(porcelain, models.Kubernetes):
        plumbing.kubernetes.CopyFrom(kubernetes_to_plumbing(porcelain))
    if isinstance(porcelain, models.KubernetesBasicAuth):
        plumbing.kubernetes_basic_auth.CopyFrom(
            kubernetes_basic_auth_to_plumbing(porcelain))
    if isinstance(porcelain, models.AmazonEKS):
        plumbing.amazon_eks.CopyFrom(amazon_eks_to_plumbing(porcelain))
    if isinstance(porcelain, models.GoogleGKE):
        plumbing.google_gke.CopyFrom(google_gke_to_plumbing(porcelain))
    if isinstance(porcelain, models.KubernetesServiceAccount):
        plumbing.kubernetes_service_account.CopyFrom(
            kubernetes_service_account_to_plumbing(porcelain))
    if isinstance(porcelain, models.Memcached):
        plumbing.memcached.CopyFrom(memcached_to_plumbing(porcelain))
    if isinstance(porcelain, models.MongoLegacyHost):
        plumbing.mongo_legacy_host.CopyFrom(
            mongo_legacy_host_to_plumbing(porcelain))
    if isinstance(porcelain, models.MongoLegacyReplicaset):
        plumbing.mongo_legacy_replicaset.CopyFrom(
            mongo_legacy_replicaset_to_plumbing(porcelain))
    if isinstance(porcelain, models.MongoHost):
        plumbing.mongo_host.CopyFrom(mongo_host_to_plumbing(porcelain))
    if isinstance(porcelain, models.MongoReplicaSet):
        plumbing.mongo_replica_set.CopyFrom(
            mongo_replica_set_to_plumbing(porcelain))
    if isinstance(porcelain, models.Mysql):
        plumbing.mysql.CopyFrom(mysql_to_plumbing(porcelain))
    if isinstance(porcelain, models.AuroraMysql):
        plumbing.aurora_mysql.CopyFrom(aurora_mysql_to_plumbing(porcelain))
    if isinstance(porcelain, models.Clustrix):
        plumbing.clustrix.CopyFrom(clustrix_to_plumbing(porcelain))
    if isinstance(porcelain, models.Maria):
        plumbing.maria.CopyFrom(maria_to_plumbing(porcelain))
    if isinstance(porcelain, models.Memsql):
        plumbing.memsql.CopyFrom(memsql_to_plumbing(porcelain))
    if isinstance(porcelain, models.Oracle):
        plumbing.oracle.CopyFrom(oracle_to_plumbing(porcelain))
    if isinstance(porcelain, models.Postgres):
        plumbing.postgres.CopyFrom(postgres_to_plumbing(porcelain))
    if isinstance(porcelain, models.AuroraPostgres):
        plumbing.aurora_postgres.CopyFrom(
            aurora_postgres_to_plumbing(porcelain))
    if isinstance(porcelain, models.Greenplum):
        plumbing.greenplum.CopyFrom(greenplum_to_plumbing(porcelain))
    if isinstance(porcelain, models.Cockroach):
        plumbing.cockroach.CopyFrom(cockroach_to_plumbing(porcelain))
    if isinstance(porcelain, models.Redshift):
        plumbing.redshift.CopyFrom(redshift_to_plumbing(porcelain))
    if isinstance(porcelain, models.Presto):
        plumbing.presto.CopyFrom(presto_to_plumbing(porcelain))
    if isinstance(porcelain, models.RDP):
        plumbing.rdp.CopyFrom(rdp_to_plumbing(porcelain))
    if isinstance(porcelain, models.Redis):
        plumbing.redis.CopyFrom(redis_to_plumbing(porcelain))
    if isinstance(porcelain, models.ElasticacheRedis):
        plumbing.elasticache_redis.CopyFrom(
            elasticache_redis_to_plumbing(porcelain))
    if isinstance(porcelain, models.Snowflake):
        plumbing.snowflake.CopyFrom(snowflake_to_plumbing(porcelain))
    if isinstance(porcelain, models.SQLServer):
        plumbing.sql_server.CopyFrom(sql_server_to_plumbing(porcelain))
    if isinstance(porcelain, models.SSH):
        plumbing.ssh.CopyFrom(ssh_to_plumbing(porcelain))
    if isinstance(porcelain, models.Sybase):
        plumbing.sybase.CopyFrom(sybase_to_plumbing(porcelain))
    if isinstance(porcelain, models.Teradata):
        plumbing.teradata.CopyFrom(teradata_to_plumbing(porcelain))
    return plumbing


def resource_to_porcelain(plumbing):
    if plumbing.HasField('athena'):
        return athena_to_porcelain(plumbing.athena)
    if plumbing.HasField('big_query'):
        return big_query_to_porcelain(plumbing.big_query)
    if plumbing.HasField('cassandra'):
        return cassandra_to_porcelain(plumbing.cassandra)
    if plumbing.HasField('druid'):
        return druid_to_porcelain(plumbing.druid)
    if plumbing.HasField('dynamo_db'):
        return dynamo_db_to_porcelain(plumbing.dynamo_db)
    if plumbing.HasField('amazon_es'):
        return amazon_es_to_porcelain(plumbing.amazon_es)
    if plumbing.HasField('elastic'):
        return elastic_to_porcelain(plumbing.elastic)
    if plumbing.HasField('http_basic_auth'):
        return http_basic_auth_to_porcelain(plumbing.http_basic_auth)
    if plumbing.HasField('http_no_auth'):
        return http_no_auth_to_porcelain(plumbing.http_no_auth)
    if plumbing.HasField('http_auth'):
        return http_auth_to_porcelain(plumbing.http_auth)
    if plumbing.HasField('kubernetes'):
        return kubernetes_to_porcelain(plumbing.kubernetes)
    if plumbing.HasField('kubernetes_basic_auth'):
        return kubernetes_basic_auth_to_porcelain(
            plumbing.kubernetes_basic_auth)
    if plumbing.HasField('amazon_eks'):
        return amazon_eks_to_porcelain(plumbing.amazon_eks)
    if plumbing.HasField('google_gke'):
        return google_gke_to_porcelain(plumbing.google_gke)
    if plumbing.HasField('kubernetes_service_account'):
        return kubernetes_service_account_to_porcelain(
            plumbing.kubernetes_service_account)
    if plumbing.HasField('memcached'):
        return memcached_to_porcelain(plumbing.memcached)
    if plumbing.HasField('mongo_legacy_host'):
        return mongo_legacy_host_to_porcelain(plumbing.mongo_legacy_host)
    if plumbing.HasField('mongo_legacy_replicaset'):
        return mongo_legacy_replicaset_to_porcelain(
            plumbing.mongo_legacy_replicaset)
    if plumbing.HasField('mongo_host'):
        return mongo_host_to_porcelain(plumbing.mongo_host)
    if plumbing.HasField('mongo_replica_set'):
        return mongo_replica_set_to_porcelain(plumbing.mongo_replica_set)
    if plumbing.HasField('mysql'):
        return mysql_to_porcelain(plumbing.mysql)
    if plumbing.HasField('aurora_mysql'):
        return aurora_mysql_to_porcelain(plumbing.aurora_mysql)
    if plumbing.HasField('clustrix'):
        return clustrix_to_porcelain(plumbing.clustrix)
    if plumbing.HasField('maria'):
        return maria_to_porcelain(plumbing.maria)
    if plumbing.HasField('memsql'):
        return memsql_to_porcelain(plumbing.memsql)
    if plumbing.HasField('oracle'):
        return oracle_to_porcelain(plumbing.oracle)
    if plumbing.HasField('postgres'):
        return postgres_to_porcelain(plumbing.postgres)
    if plumbing.HasField('aurora_postgres'):
        return aurora_postgres_to_porcelain(plumbing.aurora_postgres)
    if plumbing.HasField('greenplum'):
        return greenplum_to_porcelain(plumbing.greenplum)
    if plumbing.HasField('cockroach'):
        return cockroach_to_porcelain(plumbing.cockroach)
    if plumbing.HasField('redshift'):
        return redshift_to_porcelain(plumbing.redshift)
    if plumbing.HasField('presto'):
        return presto_to_porcelain(plumbing.presto)
    if plumbing.HasField('rdp'):
        return rdp_to_porcelain(plumbing.rdp)
    if plumbing.HasField('redis'):
        return redis_to_porcelain(plumbing.redis)
    if plumbing.HasField('elasticache_redis'):
        return elasticache_redis_to_porcelain(plumbing.elasticache_redis)
    if plumbing.HasField('snowflake'):
        return snowflake_to_porcelain(plumbing.snowflake)
    if plumbing.HasField('sql_server'):
        return sql_server_to_porcelain(plumbing.sql_server)
    if plumbing.HasField('ssh'):
        return ssh_to_porcelain(plumbing.ssh)
    if plumbing.HasField('sybase'):
        return sybase_to_porcelain(plumbing.sybase)
    if plumbing.HasField('teradata'):
        return teradata_to_porcelain(plumbing.teradata)
    return None


def repeated_resource_to_plumbing(porcelains):
    return [resource_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_resource_to_porcelain(plumbings):
    return [resource_to_porcelain(plumbing) for plumbing in plumbings]


def athena_to_porcelain(plumbing):
    porcelain = models.Athena()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.access_key = plumbing.access_key
    porcelain.secret_access_key = plumbing.secret_access_key
    porcelain.output = plumbing.output
    porcelain.port_override = plumbing.port_override
    porcelain.region = plumbing.region
    return porcelain


def athena_to_plumbing(porcelain):
    plumbing = Athena()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.access_key != None:
        plumbing.access_key = porcelain.access_key
    if porcelain.secret_access_key != None:
        plumbing.secret_access_key = porcelain.secret_access_key
    if porcelain.output != None:
        plumbing.output = porcelain.output
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.region != None:
        plumbing.region = porcelain.region
    return plumbing


def repeated_athena_to_plumbing(porcelains):
    return [athena_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_athena_to_porcelain(plumbings):
    return [athena_to_porcelain(plumbing) for plumbing in plumbings]


def big_query_to_porcelain(plumbing):
    porcelain = models.BigQuery()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.private_key = plumbing.private_key
    porcelain.project = plumbing.project
    porcelain.port_override = plumbing.port_override
    porcelain.endpoint = plumbing.endpoint
    porcelain.username = plumbing.username
    return porcelain


def big_query_to_plumbing(porcelain):
    plumbing = BigQuery()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.private_key != None:
        plumbing.private_key = porcelain.private_key
    if porcelain.project != None:
        plumbing.project = porcelain.project
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.endpoint != None:
        plumbing.endpoint = porcelain.endpoint
    if porcelain.username != None:
        plumbing.username = porcelain.username
    return plumbing


def repeated_big_query_to_plumbing(porcelains):
    return [big_query_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_big_query_to_porcelain(plumbings):
    return [big_query_to_porcelain(plumbing) for plumbing in plumbings]


def cassandra_to_porcelain(plumbing):
    porcelain = models.Cassandra()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def cassandra_to_plumbing(porcelain):
    plumbing = Cassandra()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_cassandra_to_plumbing(porcelains):
    return [cassandra_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_cassandra_to_porcelain(plumbings):
    return [cassandra_to_porcelain(plumbing) for plumbing in plumbings]


def druid_to_porcelain(plumbing):
    porcelain = models.Druid()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port_override = plumbing.port_override
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    return porcelain


def druid_to_plumbing(porcelain):
    plumbing = Druid()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_druid_to_plumbing(porcelains):
    return [druid_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_druid_to_porcelain(plumbings):
    return [druid_to_porcelain(plumbing) for plumbing in plumbings]


def dynamo_db_to_porcelain(plumbing):
    porcelain = models.DynamoDB()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.access_key = plumbing.access_key
    porcelain.secret_access_key = plumbing.secret_access_key
    porcelain.region = plumbing.region
    porcelain.endpoint = plumbing.endpoint
    porcelain.port_override = plumbing.port_override
    return porcelain


def dynamo_db_to_plumbing(porcelain):
    plumbing = DynamoDB()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.access_key != None:
        plumbing.access_key = porcelain.access_key
    if porcelain.secret_access_key != None:
        plumbing.secret_access_key = porcelain.secret_access_key
    if porcelain.region != None:
        plumbing.region = porcelain.region
    if porcelain.endpoint != None:
        plumbing.endpoint = porcelain.endpoint
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    return plumbing


def repeated_dynamo_db_to_plumbing(porcelains):
    return [dynamo_db_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_dynamo_db_to_porcelain(plumbings):
    return [dynamo_db_to_porcelain(plumbing) for plumbing in plumbings]


def amazon_es_to_porcelain(plumbing):
    porcelain = models.AmazonES()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.region = plumbing.region
    porcelain.secret_access_key = plumbing.secret_access_key
    porcelain.endpoint = plumbing.endpoint
    porcelain.access_key = plumbing.access_key
    porcelain.port_override = plumbing.port_override
    return porcelain


def amazon_es_to_plumbing(porcelain):
    plumbing = AmazonES()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.region != None:
        plumbing.region = porcelain.region
    if porcelain.secret_access_key != None:
        plumbing.secret_access_key = porcelain.secret_access_key
    if porcelain.endpoint != None:
        plumbing.endpoint = porcelain.endpoint
    if porcelain.access_key != None:
        plumbing.access_key = porcelain.access_key
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    return plumbing


def repeated_amazon_es_to_plumbing(porcelains):
    return [amazon_es_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_amazon_es_to_porcelain(plumbings):
    return [amazon_es_to_porcelain(plumbing) for plumbing in plumbings]


def elastic_to_porcelain(plumbing):
    porcelain = models.Elastic()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def elastic_to_plumbing(porcelain):
    plumbing = Elastic()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_elastic_to_plumbing(porcelains):
    return [elastic_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_elastic_to_porcelain(plumbings):
    return [elastic_to_porcelain(plumbing) for plumbing in plumbings]


def http_basic_auth_to_porcelain(plumbing):
    porcelain = models.HTTPBasicAuth()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.url = plumbing.url
    porcelain.healthcheck_path = plumbing.healthcheck_path
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.headers_blacklist = plumbing.headers_blacklist
    porcelain.default_path = plumbing.default_path
    porcelain.subdomain = plumbing.subdomain
    return porcelain


def http_basic_auth_to_plumbing(porcelain):
    plumbing = HTTPBasicAuth()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.url != None:
        plumbing.url = porcelain.url
    if porcelain.healthcheck_path != None:
        plumbing.healthcheck_path = porcelain.healthcheck_path
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.headers_blacklist != None:
        plumbing.headers_blacklist = porcelain.headers_blacklist
    if porcelain.default_path != None:
        plumbing.default_path = porcelain.default_path
    if porcelain.subdomain != None:
        plumbing.subdomain = porcelain.subdomain
    return plumbing


def repeated_http_basic_auth_to_plumbing(porcelains):
    return [http_basic_auth_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_http_basic_auth_to_porcelain(plumbings):
    return [http_basic_auth_to_porcelain(plumbing) for plumbing in plumbings]


def http_no_auth_to_porcelain(plumbing):
    porcelain = models.HTTPNoAuth()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.url = plumbing.url
    porcelain.healthcheck_path = plumbing.healthcheck_path
    porcelain.headers_blacklist = plumbing.headers_blacklist
    porcelain.default_path = plumbing.default_path
    porcelain.subdomain = plumbing.subdomain
    return porcelain


def http_no_auth_to_plumbing(porcelain):
    plumbing = HTTPNoAuth()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.url != None:
        plumbing.url = porcelain.url
    if porcelain.healthcheck_path != None:
        plumbing.healthcheck_path = porcelain.healthcheck_path
    if porcelain.headers_blacklist != None:
        plumbing.headers_blacklist = porcelain.headers_blacklist
    if porcelain.default_path != None:
        plumbing.default_path = porcelain.default_path
    if porcelain.subdomain != None:
        plumbing.subdomain = porcelain.subdomain
    return plumbing


def repeated_http_no_auth_to_plumbing(porcelains):
    return [http_no_auth_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_http_no_auth_to_porcelain(plumbings):
    return [http_no_auth_to_porcelain(plumbing) for plumbing in plumbings]


def http_auth_to_porcelain(plumbing):
    porcelain = models.HTTPAuth()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.url = plumbing.url
    porcelain.healthcheck_path = plumbing.healthcheck_path
    porcelain.auth_header = plumbing.auth_header
    porcelain.headers_blacklist = plumbing.headers_blacklist
    porcelain.default_path = plumbing.default_path
    porcelain.subdomain = plumbing.subdomain
    return porcelain


def http_auth_to_plumbing(porcelain):
    plumbing = HTTPAuth()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.url != None:
        plumbing.url = porcelain.url
    if porcelain.healthcheck_path != None:
        plumbing.healthcheck_path = porcelain.healthcheck_path
    if porcelain.auth_header != None:
        plumbing.auth_header = porcelain.auth_header
    if porcelain.headers_blacklist != None:
        plumbing.headers_blacklist = porcelain.headers_blacklist
    if porcelain.default_path != None:
        plumbing.default_path = porcelain.default_path
    if porcelain.subdomain != None:
        plumbing.subdomain = porcelain.subdomain
    return plumbing


def repeated_http_auth_to_plumbing(porcelains):
    return [http_auth_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_http_auth_to_porcelain(plumbings):
    return [http_auth_to_porcelain(plumbing) for plumbing in plumbings]


def kubernetes_to_porcelain(plumbing):
    porcelain = models.Kubernetes()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port = plumbing.port
    porcelain.certificate_authority = plumbing.certificate_authority
    porcelain.certificate_authority_filename = plumbing.certificate_authority_filename
    porcelain.client_certificate = plumbing.client_certificate
    porcelain.client_certificate_filename = plumbing.client_certificate_filename
    porcelain.client_key = plumbing.client_key
    porcelain.client_key_filename = plumbing.client_key_filename
    return porcelain


def kubernetes_to_plumbing(porcelain):
    plumbing = Kubernetes()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.certificate_authority != None:
        plumbing.certificate_authority = porcelain.certificate_authority
    if porcelain.certificate_authority_filename != None:
        plumbing.certificate_authority_filename = porcelain.certificate_authority_filename
    if porcelain.client_certificate != None:
        plumbing.client_certificate = porcelain.client_certificate
    if porcelain.client_certificate_filename != None:
        plumbing.client_certificate_filename = porcelain.client_certificate_filename
    if porcelain.client_key != None:
        plumbing.client_key = porcelain.client_key
    if porcelain.client_key_filename != None:
        plumbing.client_key_filename = porcelain.client_key_filename
    return plumbing


def repeated_kubernetes_to_plumbing(porcelains):
    return [kubernetes_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_kubernetes_to_porcelain(plumbings):
    return [kubernetes_to_porcelain(plumbing) for plumbing in plumbings]


def kubernetes_basic_auth_to_porcelain(plumbing):
    porcelain = models.KubernetesBasicAuth()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port = plumbing.port
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    return porcelain


def kubernetes_basic_auth_to_plumbing(porcelain):
    plumbing = KubernetesBasicAuth()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    return plumbing


def repeated_kubernetes_basic_auth_to_plumbing(porcelains):
    return [
        kubernetes_basic_auth_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_kubernetes_basic_auth_to_porcelain(plumbings):
    return [
        kubernetes_basic_auth_to_porcelain(plumbing) for plumbing in plumbings
    ]


def amazon_eks_to_porcelain(plumbing):
    porcelain = models.AmazonEKS()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.endpoint = plumbing.endpoint
    porcelain.access_key = plumbing.access_key
    porcelain.secret_access_key = plumbing.secret_access_key
    porcelain.certificate_authority = plumbing.certificate_authority
    porcelain.certificate_authority_filename = plumbing.certificate_authority_filename
    porcelain.region = plumbing.region
    porcelain.cluster_name = plumbing.cluster_name
    return porcelain


def amazon_eks_to_plumbing(porcelain):
    plumbing = AmazonEKS()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.endpoint != None:
        plumbing.endpoint = porcelain.endpoint
    if porcelain.access_key != None:
        plumbing.access_key = porcelain.access_key
    if porcelain.secret_access_key != None:
        plumbing.secret_access_key = porcelain.secret_access_key
    if porcelain.certificate_authority != None:
        plumbing.certificate_authority = porcelain.certificate_authority
    if porcelain.certificate_authority_filename != None:
        plumbing.certificate_authority_filename = porcelain.certificate_authority_filename
    if porcelain.region != None:
        plumbing.region = porcelain.region
    if porcelain.cluster_name != None:
        plumbing.cluster_name = porcelain.cluster_name
    return plumbing


def repeated_amazon_eks_to_plumbing(porcelains):
    return [amazon_eks_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_amazon_eks_to_porcelain(plumbings):
    return [amazon_eks_to_porcelain(plumbing) for plumbing in plumbings]


def google_gke_to_porcelain(plumbing):
    porcelain = models.GoogleGKE()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.endpoint = plumbing.endpoint
    porcelain.certificate_authority = plumbing.certificate_authority
    porcelain.certificate_authority_filename = plumbing.certificate_authority_filename
    porcelain.service_account_key = plumbing.service_account_key
    porcelain.service_account_key_filename = plumbing.service_account_key_filename
    return porcelain


def google_gke_to_plumbing(porcelain):
    plumbing = GoogleGKE()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.endpoint != None:
        plumbing.endpoint = porcelain.endpoint
    if porcelain.certificate_authority != None:
        plumbing.certificate_authority = porcelain.certificate_authority
    if porcelain.certificate_authority_filename != None:
        plumbing.certificate_authority_filename = porcelain.certificate_authority_filename
    if porcelain.service_account_key != None:
        plumbing.service_account_key = porcelain.service_account_key
    if porcelain.service_account_key_filename != None:
        plumbing.service_account_key_filename = porcelain.service_account_key_filename
    return plumbing


def repeated_google_gke_to_plumbing(porcelains):
    return [google_gke_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_google_gke_to_porcelain(plumbings):
    return [google_gke_to_porcelain(plumbing) for plumbing in plumbings]


def kubernetes_service_account_to_porcelain(plumbing):
    porcelain = models.KubernetesServiceAccount()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port = plumbing.port
    porcelain.token = plumbing.token
    return porcelain


def kubernetes_service_account_to_plumbing(porcelain):
    plumbing = KubernetesServiceAccount()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.token != None:
        plumbing.token = porcelain.token
    return plumbing


def repeated_kubernetes_service_account_to_plumbing(porcelains):
    return [
        kubernetes_service_account_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_kubernetes_service_account_to_porcelain(plumbings):
    return [
        kubernetes_service_account_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def memcached_to_porcelain(plumbing):
    porcelain = models.Memcached()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def memcached_to_plumbing(porcelain):
    plumbing = Memcached()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_memcached_to_plumbing(porcelains):
    return [memcached_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_memcached_to_porcelain(plumbings):
    return [memcached_to_porcelain(plumbing) for plumbing in plumbings]


def mongo_legacy_host_to_porcelain(plumbing):
    porcelain = models.MongoLegacyHost()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.auth_database = plumbing.auth_database
    porcelain.port_override = plumbing.port_override
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    porcelain.replica_set = plumbing.replica_set
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def mongo_legacy_host_to_plumbing(porcelain):
    plumbing = MongoLegacyHost()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.auth_database != None:
        plumbing.auth_database = porcelain.auth_database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.replica_set != None:
        plumbing.replica_set = porcelain.replica_set
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_mongo_legacy_host_to_plumbing(porcelains):
    return [
        mongo_legacy_host_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_mongo_legacy_host_to_porcelain(plumbings):
    return [mongo_legacy_host_to_porcelain(plumbing) for plumbing in plumbings]


def mongo_legacy_replicaset_to_porcelain(plumbing):
    porcelain = models.MongoLegacyReplicaset()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.auth_database = plumbing.auth_database
    porcelain.port_override = plumbing.port_override
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    porcelain.replica_set = plumbing.replica_set
    porcelain.connect_to_replica = plumbing.connect_to_replica
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def mongo_legacy_replicaset_to_plumbing(porcelain):
    plumbing = MongoLegacyReplicaset()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.auth_database != None:
        plumbing.auth_database = porcelain.auth_database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.replica_set != None:
        plumbing.replica_set = porcelain.replica_set
    if porcelain.connect_to_replica != None:
        plumbing.connect_to_replica = porcelain.connect_to_replica
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_mongo_legacy_replicaset_to_plumbing(porcelains):
    return [
        mongo_legacy_replicaset_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_mongo_legacy_replicaset_to_porcelain(plumbings):
    return [
        mongo_legacy_replicaset_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def mongo_host_to_porcelain(plumbing):
    porcelain = models.MongoHost()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.auth_database = plumbing.auth_database
    porcelain.port_override = plumbing.port_override
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def mongo_host_to_plumbing(porcelain):
    plumbing = MongoHost()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.auth_database != None:
        plumbing.auth_database = porcelain.auth_database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_mongo_host_to_plumbing(porcelains):
    return [mongo_host_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_mongo_host_to_porcelain(plumbings):
    return [mongo_host_to_porcelain(plumbing) for plumbing in plumbings]


def mongo_replica_set_to_porcelain(plumbing):
    porcelain = models.MongoReplicaSet()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.auth_database = plumbing.auth_database
    porcelain.port_override = plumbing.port_override
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    porcelain.replica_set = plumbing.replica_set
    porcelain.connect_to_replica = plumbing.connect_to_replica
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def mongo_replica_set_to_plumbing(porcelain):
    plumbing = MongoReplicaSet()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.auth_database != None:
        plumbing.auth_database = porcelain.auth_database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.replica_set != None:
        plumbing.replica_set = porcelain.replica_set
    if porcelain.connect_to_replica != None:
        plumbing.connect_to_replica = porcelain.connect_to_replica
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_mongo_replica_set_to_plumbing(porcelains):
    return [
        mongo_replica_set_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_mongo_replica_set_to_porcelain(plumbings):
    return [mongo_replica_set_to_porcelain(plumbing) for plumbing in plumbings]


def mysql_to_porcelain(plumbing):
    porcelain = models.Mysql()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def mysql_to_plumbing(porcelain):
    plumbing = Mysql()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_mysql_to_plumbing(porcelains):
    return [mysql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_mysql_to_porcelain(plumbings):
    return [mysql_to_porcelain(plumbing) for plumbing in plumbings]


def aurora_mysql_to_porcelain(plumbing):
    porcelain = models.AuroraMysql()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def aurora_mysql_to_plumbing(porcelain):
    plumbing = AuroraMysql()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_aurora_mysql_to_plumbing(porcelains):
    return [aurora_mysql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_aurora_mysql_to_porcelain(plumbings):
    return [aurora_mysql_to_porcelain(plumbing) for plumbing in plumbings]


def clustrix_to_porcelain(plumbing):
    porcelain = models.Clustrix()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def clustrix_to_plumbing(porcelain):
    plumbing = Clustrix()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_clustrix_to_plumbing(porcelains):
    return [clustrix_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_clustrix_to_porcelain(plumbings):
    return [clustrix_to_porcelain(plumbing) for plumbing in plumbings]


def maria_to_porcelain(plumbing):
    porcelain = models.Maria()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def maria_to_plumbing(porcelain):
    plumbing = Maria()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_maria_to_plumbing(porcelains):
    return [maria_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_maria_to_porcelain(plumbings):
    return [maria_to_porcelain(plumbing) for plumbing in plumbings]


def memsql_to_porcelain(plumbing):
    porcelain = models.Memsql()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def memsql_to_plumbing(porcelain):
    plumbing = Memsql()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_memsql_to_plumbing(porcelains):
    return [memsql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_memsql_to_porcelain(plumbings):
    return [memsql_to_porcelain(plumbing) for plumbing in plumbings]


def oracle_to_porcelain(plumbing):
    porcelain = models.Oracle()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port = plumbing.port
    porcelain.port_override = plumbing.port_override
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def oracle_to_plumbing(porcelain):
    plumbing = Oracle()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_oracle_to_plumbing(porcelains):
    return [oracle_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_oracle_to_porcelain(plumbings):
    return [oracle_to_porcelain(plumbing) for plumbing in plumbings]


def postgres_to_porcelain(plumbing):
    porcelain = models.Postgres()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def postgres_to_plumbing(porcelain):
    plumbing = Postgres()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_postgres_to_plumbing(porcelains):
    return [postgres_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_postgres_to_porcelain(plumbings):
    return [postgres_to_porcelain(plumbing) for plumbing in plumbings]


def aurora_postgres_to_porcelain(plumbing):
    porcelain = models.AuroraPostgres()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def aurora_postgres_to_plumbing(porcelain):
    plumbing = AuroraPostgres()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_aurora_postgres_to_plumbing(porcelains):
    return [aurora_postgres_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_aurora_postgres_to_porcelain(plumbings):
    return [aurora_postgres_to_porcelain(plumbing) for plumbing in plumbings]


def greenplum_to_porcelain(plumbing):
    porcelain = models.Greenplum()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def greenplum_to_plumbing(porcelain):
    plumbing = Greenplum()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_greenplum_to_plumbing(porcelains):
    return [greenplum_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_greenplum_to_porcelain(plumbings):
    return [greenplum_to_porcelain(plumbing) for plumbing in plumbings]


def cockroach_to_porcelain(plumbing):
    porcelain = models.Cockroach()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def cockroach_to_plumbing(porcelain):
    plumbing = Cockroach()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_cockroach_to_plumbing(porcelains):
    return [cockroach_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_cockroach_to_porcelain(plumbings):
    return [cockroach_to_porcelain(plumbing) for plumbing in plumbings]


def redshift_to_porcelain(plumbing):
    porcelain = models.Redshift()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def redshift_to_plumbing(porcelain):
    plumbing = Redshift()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_redshift_to_plumbing(porcelains):
    return [redshift_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_redshift_to_porcelain(plumbings):
    return [redshift_to_porcelain(plumbing) for plumbing in plumbings]


def presto_to_porcelain(plumbing):
    porcelain = models.Presto()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.username = plumbing.username
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def presto_to_plumbing(porcelain):
    plumbing = Presto()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_presto_to_plumbing(porcelains):
    return [presto_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_presto_to_porcelain(plumbings):
    return [presto_to_porcelain(plumbing) for plumbing in plumbings]


def rdp_to_porcelain(plumbing):
    porcelain = models.RDP()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def rdp_to_plumbing(porcelain):
    plumbing = RDP()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_rdp_to_plumbing(porcelains):
    return [rdp_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_rdp_to_porcelain(plumbings):
    return [rdp_to_porcelain(plumbing) for plumbing in plumbings]


def redis_to_porcelain(plumbing):
    porcelain = models.Redis()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port_override = plumbing.port_override
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    return porcelain


def redis_to_plumbing(porcelain):
    plumbing = Redis()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_redis_to_plumbing(porcelains):
    return [redis_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_redis_to_porcelain(plumbings):
    return [redis_to_porcelain(plumbing) for plumbing in plumbings]


def elasticache_redis_to_porcelain(plumbing):
    porcelain = models.ElasticacheRedis()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.port_override = plumbing.port_override
    porcelain.password = plumbing.password
    porcelain.port = plumbing.port
    porcelain.tls_required = plumbing.tls_required
    return porcelain


def elasticache_redis_to_plumbing(porcelain):
    plumbing = ElasticacheRedis()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.tls_required != None:
        plumbing.tls_required = porcelain.tls_required
    return plumbing


def repeated_elasticache_redis_to_plumbing(porcelains):
    return [
        elasticache_redis_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_elasticache_redis_to_porcelain(plumbings):
    return [elasticache_redis_to_porcelain(plumbing) for plumbing in plumbings]


def snowflake_to_porcelain(plumbing):
    porcelain = models.Snowflake()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.schema = plumbing.schema
    porcelain.port_override = plumbing.port_override
    return porcelain


def snowflake_to_plumbing(porcelain):
    plumbing = Snowflake()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.schema != None:
        plumbing.schema = porcelain.schema
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    return plumbing


def repeated_snowflake_to_plumbing(porcelains):
    return [snowflake_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_snowflake_to_porcelain(plumbings):
    return [snowflake_to_porcelain(plumbing) for plumbing in plumbings]


def sql_server_to_porcelain(plumbing):
    porcelain = models.SQLServer()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.database = plumbing.database
    porcelain.port_override = plumbing.port_override
    porcelain.schema = plumbing.schema
    porcelain.port = plumbing.port
    porcelain.override_database = plumbing.override_database
    return porcelain


def sql_server_to_plumbing(porcelain):
    plumbing = SQLServer()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.database != None:
        plumbing.database = porcelain.database
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.schema != None:
        plumbing.schema = porcelain.schema
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.override_database != None:
        plumbing.override_database = porcelain.override_database
    return plumbing


def repeated_sql_server_to_plumbing(porcelains):
    return [sql_server_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_sql_server_to_porcelain(plumbings):
    return [sql_server_to_porcelain(plumbing) for plumbing in plumbings]


def ssh_to_porcelain(plumbing):
    porcelain = models.SSH()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.port = plumbing.port
    porcelain.public_key = plumbing.public_key
    return porcelain


def ssh_to_plumbing(porcelain):
    plumbing = SSH()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.public_key != None:
        plumbing.public_key = porcelain.public_key
    return plumbing


def repeated_ssh_to_plumbing(porcelains):
    return [ssh_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_ssh_to_porcelain(plumbings):
    return [ssh_to_porcelain(plumbing) for plumbing in plumbings]


def sybase_to_porcelain(plumbing):
    porcelain = models.Sybase()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    porcelain.password = plumbing.password
    return porcelain


def sybase_to_plumbing(porcelain):
    plumbing = Sybase()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    if porcelain.password != None:
        plumbing.password = porcelain.password
    return plumbing


def repeated_sybase_to_plumbing(porcelains):
    return [sybase_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_sybase_to_porcelain(plumbings):
    return [sybase_to_porcelain(plumbing) for plumbing in plumbings]


def teradata_to_porcelain(plumbing):
    porcelain = models.Teradata()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.healthy = plumbing.healthy
    porcelain.hostname = plumbing.hostname
    porcelain.username = plumbing.username
    porcelain.password = plumbing.password
    porcelain.port_override = plumbing.port_override
    porcelain.port = plumbing.port
    return porcelain


def teradata_to_plumbing(porcelain):
    plumbing = Teradata()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.healthy != None:
        plumbing.healthy = porcelain.healthy
    if porcelain.hostname != None:
        plumbing.hostname = porcelain.hostname
    if porcelain.username != None:
        plumbing.username = porcelain.username
    if porcelain.password != None:
        plumbing.password = porcelain.password
    if porcelain.port_override != None:
        plumbing.port_override = porcelain.port_override
    if porcelain.port != None:
        plumbing.port = porcelain.port
    return plumbing


def repeated_teradata_to_plumbing(porcelains):
    return [teradata_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_teradata_to_porcelain(plumbings):
    return [teradata_to_porcelain(plumbing) for plumbing in plumbings]


def node_create_response_to_porcelain(plumbing):
    porcelain = models.NodeCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.node = node_to_porcelain(plumbing.node)
    porcelain.token = plumbing.token
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def node_create_response_to_plumbing(porcelain):
    plumbing = NodeCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.node != None:
        plumbing.node = node_to_plumbing(porcelain.node)
    if porcelain.token != None:
        plumbing.token = porcelain.token
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_node_create_response_to_plumbing(porcelains):
    return [
        node_create_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_node_create_response_to_porcelain(plumbings):
    return [
        node_create_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def node_get_response_to_porcelain(plumbing):
    porcelain = models.NodeGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.node = node_to_porcelain(plumbing.node)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def node_get_response_to_plumbing(porcelain):
    plumbing = NodeGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.node != None:
        plumbing.node = node_to_plumbing(porcelain.node)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_node_get_response_to_plumbing(porcelains):
    return [
        node_get_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_node_get_response_to_porcelain(plumbings):
    return [node_get_response_to_porcelain(plumbing) for plumbing in plumbings]


def node_update_response_to_porcelain(plumbing):
    porcelain = models.NodeUpdateResponse()
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    porcelain.node = node_to_porcelain(plumbing.node)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def node_update_response_to_plumbing(porcelain):
    plumbing = NodeUpdateResponse()
    if porcelain.meta != None:
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.node != None:
        plumbing.node = node_to_plumbing(porcelain.node)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_node_update_response_to_plumbing(porcelains):
    return [
        node_update_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_node_update_response_to_porcelain(plumbings):
    return [
        node_update_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def node_delete_response_to_porcelain(plumbing):
    porcelain = models.NodeDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def node_delete_response_to_plumbing(porcelain):
    plumbing = NodeDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_node_delete_response_to_plumbing(porcelains):
    return [
        node_delete_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_node_delete_response_to_porcelain(plumbings):
    return [
        node_delete_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def node_to_plumbing(porcelain):
    plumbing = Node()
    if isinstance(porcelain, models.Relay):
        plumbing.relay.CopyFrom(relay_to_plumbing(porcelain))
    if isinstance(porcelain, models.Gateway):
        plumbing.gateway.CopyFrom(gateway_to_plumbing(porcelain))
    return plumbing


def node_to_porcelain(plumbing):
    if plumbing.HasField('relay'):
        return relay_to_porcelain(plumbing.relay)
    if plumbing.HasField('gateway'):
        return gateway_to_porcelain(plumbing.gateway)
    return None


def repeated_node_to_plumbing(porcelains):
    return [node_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_node_to_porcelain(plumbings):
    return [node_to_porcelain(plumbing) for plumbing in plumbings]


def relay_to_porcelain(plumbing):
    porcelain = models.Relay()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.state = plumbing.state
    return porcelain


def relay_to_plumbing(porcelain):
    plumbing = Relay()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.state != None:
        plumbing.state = porcelain.state
    return plumbing


def repeated_relay_to_plumbing(porcelains):
    return [relay_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_relay_to_porcelain(plumbings):
    return [relay_to_porcelain(plumbing) for plumbing in plumbings]


def gateway_to_porcelain(plumbing):
    porcelain = models.Gateway()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.state = plumbing.state
    porcelain.listen_address = plumbing.listen_address
    porcelain.bind_address = plumbing.bind_address
    return porcelain


def gateway_to_plumbing(porcelain):
    plumbing = Gateway()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.state != None:
        plumbing.state = porcelain.state
    if porcelain.listen_address != None:
        plumbing.listen_address = porcelain.listen_address
    if porcelain.bind_address != None:
        plumbing.bind_address = porcelain.bind_address
    return plumbing


def repeated_gateway_to_plumbing(porcelains):
    return [gateway_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_gateway_to_porcelain(plumbings):
    return [gateway_to_porcelain(plumbing) for plumbing in plumbings]


def resource_create_response_to_porcelain(plumbing):
    porcelain = models.ResourceCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.resource = resource_to_porcelain(plumbing.resource)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def resource_create_response_to_plumbing(porcelain):
    plumbing = ResourceCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.resource != None:
        plumbing.resource = resource_to_plumbing(porcelain.resource)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_resource_create_response_to_plumbing(porcelains):
    return [
        resource_create_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_resource_create_response_to_porcelain(plumbings):
    return [
        resource_create_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def resource_get_response_to_porcelain(plumbing):
    porcelain = models.ResourceGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.resource = resource_to_porcelain(plumbing.resource)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def resource_get_response_to_plumbing(porcelain):
    plumbing = ResourceGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.resource != None:
        plumbing.resource = resource_to_plumbing(porcelain.resource)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_resource_get_response_to_plumbing(porcelains):
    return [
        resource_get_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_resource_get_response_to_porcelain(plumbings):
    return [
        resource_get_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def resource_update_response_to_porcelain(plumbing):
    porcelain = models.ResourceUpdateResponse()
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    porcelain.resource = resource_to_porcelain(plumbing.resource)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def resource_update_response_to_plumbing(porcelain):
    plumbing = ResourceUpdateResponse()
    if porcelain.meta != None:
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.resource != None:
        plumbing.resource = resource_to_plumbing(porcelain.resource)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_resource_update_response_to_plumbing(porcelains):
    return [
        resource_update_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_resource_update_response_to_porcelain(plumbings):
    return [
        resource_update_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def resource_delete_response_to_porcelain(plumbing):
    porcelain = models.ResourceDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def resource_delete_response_to_plumbing(porcelain):
    plumbing = ResourceDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_resource_delete_response_to_plumbing(porcelains):
    return [
        resource_delete_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_resource_delete_response_to_porcelain(plumbings):
    return [
        resource_delete_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def role_attachment_create_response_to_porcelain(plumbing):
    porcelain = models.RoleAttachmentCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.role_attachment = role_attachment_to_porcelain(
        plumbing.role_attachment)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_attachment_create_response_to_plumbing(porcelain):
    plumbing = RoleAttachmentCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.role_attachment != None:
        plumbing.role_attachment = role_attachment_to_plumbing(
            porcelain.role_attachment)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_attachment_create_response_to_plumbing(porcelains):
    return [
        role_attachment_create_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_role_attachment_create_response_to_porcelain(plumbings):
    return [
        role_attachment_create_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def role_attachment_get_response_to_porcelain(plumbing):
    porcelain = models.RoleAttachmentGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.role_attachment = role_attachment_to_porcelain(
        plumbing.role_attachment)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_attachment_get_response_to_plumbing(porcelain):
    plumbing = RoleAttachmentGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.role_attachment != None:
        plumbing.role_attachment = role_attachment_to_plumbing(
            porcelain.role_attachment)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_attachment_get_response_to_plumbing(porcelains):
    return [
        role_attachment_get_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_role_attachment_get_response_to_porcelain(plumbings):
    return [
        role_attachment_get_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def role_attachment_delete_response_to_porcelain(plumbing):
    porcelain = models.RoleAttachmentDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_attachment_delete_response_to_plumbing(porcelain):
    plumbing = RoleAttachmentDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_attachment_delete_response_to_plumbing(porcelains):
    return [
        role_attachment_delete_response_to_plumbing(porcelain)
        for porcelain in porcelains
    ]


def repeated_role_attachment_delete_response_to_porcelain(plumbings):
    return [
        role_attachment_delete_response_to_porcelain(plumbing)
        for plumbing in plumbings
    ]


def role_attachment_to_porcelain(plumbing):
    porcelain = models.RoleAttachment()
    porcelain.id = plumbing.id
    porcelain.composite_role_id = plumbing.composite_role_id
    porcelain.attached_role_id = plumbing.attached_role_id
    return porcelain


def role_attachment_to_plumbing(porcelain):
    plumbing = RoleAttachment()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.composite_role_id != None:
        plumbing.composite_role_id = porcelain.composite_role_id
    if porcelain.attached_role_id != None:
        plumbing.attached_role_id = porcelain.attached_role_id
    return plumbing


def repeated_role_attachment_to_plumbing(porcelains):
    return [role_attachment_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_role_attachment_to_porcelain(plumbings):
    return [role_attachment_to_porcelain(plumbing) for plumbing in plumbings]


def role_create_response_to_porcelain(plumbing):
    porcelain = models.RoleCreateResponse()
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    porcelain.role = role_to_porcelain(plumbing.role)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_create_response_to_plumbing(porcelain):
    plumbing = RoleCreateResponse()
    if porcelain.meta != None:
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.role != None:
        plumbing.role = role_to_plumbing(porcelain.role)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_create_response_to_plumbing(porcelains):
    return [
        role_create_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_role_create_response_to_porcelain(plumbings):
    return [
        role_create_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def role_get_response_to_porcelain(plumbing):
    porcelain = models.RoleGetResponse()
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    porcelain.role = role_to_porcelain(plumbing.role)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_get_response_to_plumbing(porcelain):
    plumbing = RoleGetResponse()
    if porcelain.meta != None:
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.role != None:
        plumbing.role = role_to_plumbing(porcelain.role)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_get_response_to_plumbing(porcelains):
    return [
        role_get_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_role_get_response_to_porcelain(plumbings):
    return [role_get_response_to_porcelain(plumbing) for plumbing in plumbings]


def role_update_response_to_porcelain(plumbing):
    porcelain = models.RoleUpdateResponse()
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    porcelain.role = role_to_porcelain(plumbing.role)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_update_response_to_plumbing(porcelain):
    plumbing = RoleUpdateResponse()
    if porcelain.meta != None:
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.role != None:
        plumbing.role = role_to_plumbing(porcelain.role)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_update_response_to_plumbing(porcelains):
    return [
        role_update_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_role_update_response_to_porcelain(plumbings):
    return [
        role_update_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def role_delete_response_to_porcelain(plumbing):
    porcelain = models.RoleDeleteResponse()
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(
        plumbing.rate_limit)
    return porcelain


def role_delete_response_to_plumbing(porcelain):
    plumbing = RoleDeleteResponse()
    if porcelain.meta != None:
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
    if porcelain.rate_limit != None:
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(
            porcelain.rate_limit)
    return plumbing


def repeated_role_delete_response_to_plumbing(porcelains):
    return [
        role_delete_response_to_plumbing(porcelain) for porcelain in porcelains
    ]


def repeated_role_delete_response_to_porcelain(plumbings):
    return [
        role_delete_response_to_porcelain(plumbing) for plumbing in plumbings
    ]


def role_to_porcelain(plumbing):
    porcelain = models.Role()
    porcelain.id = plumbing.id
    porcelain.name = plumbing.name
    porcelain.composite = plumbing.composite
    return porcelain


def role_to_plumbing(porcelain):
    plumbing = Role()
    if porcelain.id != None:
        plumbing.id = porcelain.id
    if porcelain.name != None:
        plumbing.name = porcelain.name
    if porcelain.composite != None:
        plumbing.composite = porcelain.composite
    return plumbing


def repeated_role_to_plumbing(porcelains):
    return [role_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_role_to_porcelain(plumbings):
    return [role_to_porcelain(plumbing) for plumbing in plumbings]


def is_status_detail(x):
    # Return True if a metadata is a grpc-status-details
    if (hasattr(x, 'key') and (hasattr(x, 'value'))
            and x.key.startswith('grpc-status-details')):
        return True
    return False


def get_status_metadata(err):
    # Extracts error details from a grpc.RpcError.
    # Returns a status object and a list of details.
    metadata = err.trailing_metadata()

    # get only metadata relevant to status details
    status_md = [x for x in metadata if is_status_detail(x)]
    st = None
    if status_md:
        for md in status_md:
            st = status_pb2.Status()
            # there should be exactly one status for every RpcError
            # so MergeFromString should at worst append more details
            # but never override st.message and st.code in every loop
            st.MergeFromString(md.value)

    return st


def error_to_porcelain(err):
    if not isinstance(err, grpc.RpcError):
        return errors.RPCError(str(err), 2)  # Unknown
    # get_status_metadata fails for deadline exceeded
    if err.code().name == 'DEADLINE_EXCEEDED':
        return errors.TimeoutError()
    status = get_status_metadata(err)
    if status is None:
        code, name = err.code().value
        return errors.RPCError(name, code)
    if err.code() == grpc.StatusCode.INVALID_ARGUMENT:
        return errors.BadRequestError(status.message)
    elif err.code() == grpc.StatusCode.NOT_FOUND:
        return errors.NotFoundError(status.message)
    elif err.code() == grpc.StatusCode.ALREADY_EXISTS:
        return errors.AlreadyExistsError(status.message)
    elif err.code() == grpc.StatusCode.PERMISSION_DENIED:
        return errors.PermissionError(status.message)
    elif err.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
        for detail in status.details:
            if detail.Is(RateLimitMetadata.DESCRIPTOR):
                rate_limit = RateLimitMetadata()
                detail.Unpack(rate_limit)
                return errors.RateLimitError(
                    status.message,
                    rate_limit_metadata_to_porcelain(rate_limit))
    elif err.code() == grpc.StatusCode.INTERNAL:
        return errors.InternalError(status.message)
    elif err.code() == grpc.StatusCode.UNAUTHENTICATED:
        return errors.AuthenticationError(status.message)

    code = err.code().value[0]
    return errors.RPCError(status.message, code)
