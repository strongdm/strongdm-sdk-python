import grpc
import google.rpc as rpc
from google.rpc import status_pb2
from . import errors
from . import models
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from .options_pb2 import *
from .drivers_pb2 import *
from .spec_pb2 import *
from .nodes_pb2 import *
from .resources_pb2 import *
from .role_attachments_pb2 import *
from .roles_pb2 import *


def timestamp_to_porcelain(t):
    return t.ToDatetime()


def timestamp_to_plumbing(t):
    res = Timestamp()
    res.FromDatetime(t)
    return res


def driver_to_plumbing(porcelain):
    plumbing = Driver()
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
    if isinstance(porcelain, models.Athena):
        plumbing.athena.CopyFrom(athena_to_plumbing(porcelain))
    return plumbing


def driver_to_porcelain(plumbing):
    if plumbing.mysql != None:
        return mysql_to_porcelain(plumbing.mysql)
    if plumbing.aurora_mysql != None:
        return aurora_mysql_to_porcelain(plumbing.aurora_mysql)
    if plumbing.clustrix != None:
        return clustrix_to_porcelain(plumbing.clustrix)
    if plumbing.maria != None:
        return maria_to_porcelain(plumbing.maria)
    if plumbing.memsql != None:
        return memsql_to_porcelain(plumbing.memsql)
    if plumbing.athena != None:
        return athena_to_porcelain(plumbing.athena)
    return None


def repeated_driver_to_plumbing(porcelains):
    return [driver_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_driver_to_porcelain(plumbings):
    return [driver_to_porcelain(plumbing) for plumbing in plumbings]


def mysql_to_porcelain(plumbing):
    porcelain = models.Mysql()

    porcelain.hostname = plumbing.hostname

    porcelain.username = plumbing.username

    porcelain.password = plumbing.password

    porcelain.database = plumbing.database

    porcelain.port = plumbing.port
    return porcelain


def mysql_to_plumbing(porcelain):
    plumbing = Mysql()
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
    return plumbing


def repeated_mysql_to_plumbing(porcelains):
    return [mysql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_mysql_to_porcelain(plumbings):
    return [mysql_to_porcelain(plumbing) for plumbing in plumbings]


def aurora_mysql_to_porcelain(plumbing):
    porcelain = models.AuroraMysql()

    porcelain.hostname = plumbing.hostname

    porcelain.username = plumbing.username

    porcelain.password = plumbing.password

    porcelain.database = plumbing.database

    porcelain.port = plumbing.port
    return porcelain


def aurora_mysql_to_plumbing(porcelain):
    plumbing = AuroraMysql()
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
    return plumbing


def repeated_aurora_mysql_to_plumbing(porcelains):
    return [aurora_mysql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_aurora_mysql_to_porcelain(plumbings):
    return [aurora_mysql_to_porcelain(plumbing) for plumbing in plumbings]


def clustrix_to_porcelain(plumbing):
    porcelain = models.Clustrix()

    porcelain.hostname = plumbing.hostname

    porcelain.username = plumbing.username

    porcelain.password = plumbing.password

    porcelain.database = plumbing.database

    porcelain.port = plumbing.port
    return porcelain


def clustrix_to_plumbing(porcelain):
    plumbing = Clustrix()
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
    return plumbing


def repeated_clustrix_to_plumbing(porcelains):
    return [clustrix_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_clustrix_to_porcelain(plumbings):
    return [clustrix_to_porcelain(plumbing) for plumbing in plumbings]


def maria_to_porcelain(plumbing):
    porcelain = models.Maria()

    porcelain.hostname = plumbing.hostname

    porcelain.username = plumbing.username

    porcelain.password = plumbing.password

    porcelain.database = plumbing.database

    porcelain.port = plumbing.port
    return porcelain


def maria_to_plumbing(porcelain):
    plumbing = Maria()
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
    return plumbing


def repeated_maria_to_plumbing(porcelains):
    return [maria_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_maria_to_porcelain(plumbings):
    return [maria_to_porcelain(plumbing) for plumbing in plumbings]


def memsql_to_porcelain(plumbing):
    porcelain = models.Memsql()

    porcelain.hostname = plumbing.hostname

    porcelain.username = plumbing.username

    porcelain.password = plumbing.password

    porcelain.database = plumbing.database

    porcelain.port = plumbing.port
    return porcelain


def memsql_to_plumbing(porcelain):
    plumbing = Memsql()
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
    return plumbing


def repeated_memsql_to_plumbing(porcelains):
    return [memsql_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_memsql_to_porcelain(plumbings):
    return [memsql_to_porcelain(plumbing) for plumbing in plumbings]


def athena_to_porcelain(plumbing):
    porcelain = models.Athena()

    porcelain.access_key = plumbing.access_key

    porcelain.secretAccessKey = plumbing.secretAccessKey

    porcelain.region = plumbing.region

    porcelain.output = plumbing.output
    return porcelain


def athena_to_plumbing(porcelain):
    plumbing = Athena()
    if porcelain.access_key != None:

        plumbing.access_key = porcelain.access_key
    if porcelain.secretAccessKey != None:

        plumbing.secretAccessKey = porcelain.secretAccessKey
    if porcelain.region != None:

        plumbing.region = porcelain.region
    if porcelain.output != None:

        plumbing.output = porcelain.output
    return plumbing


def repeated_athena_to_plumbing(porcelains):
    return [athena_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_athena_to_porcelain(plumbings):
    return [athena_to_porcelain(plumbing) for plumbing in plumbings]


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
    if plumbing.relay != None:
        return relay_to_porcelain(plumbing.relay)
    if plumbing.gateway != None:
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


def resource_to_porcelain(plumbing):
    porcelain = models.Resource()

    porcelain.id = plumbing.id

    porcelain.name = plumbing.name

    porcelain.port_override = plumbing.port_override

    porcelain.healthy = plumbing.healthy

    porcelain.driver = driver_to_porcelain(plumbing.driver)
    return porcelain


def resource_to_plumbing(porcelain):
    plumbing = Resource()
    if porcelain.id != None:

        plumbing.id = porcelain.id
    if porcelain.name != None:

        plumbing.name = porcelain.name
    if porcelain.port_override != None:

        plumbing.port_override = porcelain.port_override
    if porcelain.healthy != None:

        plumbing.healthy = porcelain.healthy
    if porcelain.driver != None:

        plumbing.driver = driver_to_plumbing(porcelain.driver)

    return plumbing


def repeated_resource_to_plumbing(porcelains):
    return [resource_to_plumbing(porcelain) for porcelain in porcelains]


def repeated_resource_to_porcelain(plumbings):
    return [resource_to_porcelain(plumbing) for plumbing in plumbings]


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
