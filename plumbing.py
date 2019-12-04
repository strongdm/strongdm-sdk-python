import grpc
import google.rpc as rpc
from google.rpc import status_pb2
from . import errors
from . import models
from google.protobuf.timestamp_pb2 import Timestamp
import datetime
from .options_pb2 import *
from .spec_pb2 import *
from .nodes_pb2 import *
from .roles_pb2 import *
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
    return [create_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_create_response_metadata_to_porcelain(plumbings):
    return [create_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def get_response_metadata_to_porcelain(plumbing):
    porcelain = models.GetResponseMetadata()
    return porcelain

def get_response_metadata_to_plumbing(porcelain):
    plumbing = GetResponseMetadata()
    return plumbing

def repeated_get_response_metadata_to_plumbing(porcelains):
    return [get_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_get_response_metadata_to_porcelain(plumbings):
    return [get_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def update_response_metadata_to_porcelain(plumbing):
    porcelain = models.UpdateResponseMetadata()
    return porcelain

def update_response_metadata_to_plumbing(porcelain):
    plumbing = UpdateResponseMetadata()
    return plumbing

def repeated_update_response_metadata_to_plumbing(porcelains):
    return [update_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_update_response_metadata_to_porcelain(plumbings):
    return [update_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def delete_response_metadata_to_porcelain(plumbing):
    porcelain = models.DeleteResponseMetadata()
    return porcelain

def delete_response_metadata_to_plumbing(porcelain):
    plumbing = DeleteResponseMetadata()
    return plumbing

def repeated_delete_response_metadata_to_plumbing(porcelains):
    return [delete_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_delete_response_metadata_to_porcelain(plumbings):
    return [delete_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

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
    return [rate_limit_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_rate_limit_metadata_to_porcelain(plumbings):
    return [rate_limit_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def node_create_response_to_porcelain(plumbing):
    porcelain = models.NodeCreateResponse()
    
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    
    porcelain.token = plumbing.token
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
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
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_node_create_response_to_plumbing(porcelains):
    return [node_create_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_create_response_to_porcelain(plumbings):
    return [node_create_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_get_response_to_porcelain(plumbing):
    porcelain = models.NodeGetResponse()
    
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def node_get_response_to_plumbing(porcelain):
    plumbing = NodeGetResponse()
    if porcelain.meta != None:
        
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.node != None:
        
        plumbing.node = node_to_plumbing(porcelain.node)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_node_get_response_to_plumbing(porcelains):
    return [node_get_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_get_response_to_porcelain(plumbings):
    return [node_get_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_update_response_to_porcelain(plumbing):
    porcelain = models.NodeUpdateResponse()
    
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def node_update_response_to_plumbing(porcelain):
    plumbing = NodeUpdateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.node != None:
        
        plumbing.node = node_to_plumbing(porcelain.node)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_node_update_response_to_plumbing(porcelains):
    return [node_update_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_update_response_to_porcelain(plumbings):
    return [node_update_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_delete_response_to_porcelain(plumbing):
    porcelain = models.NodeDeleteResponse()
    
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def node_delete_response_to_plumbing(porcelain):
    plumbing = NodeDeleteResponse()
    if porcelain.meta != None:
        
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_node_delete_response_to_plumbing(porcelains):
    return [node_delete_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_delete_response_to_porcelain(plumbings):
    return [node_delete_response_to_porcelain(plumbing) for plumbing in plumbings]

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

def role_create_response_to_porcelain(plumbing):
    porcelain = models.RoleCreateResponse()
    
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def role_create_response_to_plumbing(porcelain):
    plumbing = RoleCreateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_role_create_response_to_plumbing(porcelains):
    return [role_create_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_create_response_to_porcelain(plumbings):
    return [role_create_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_get_response_to_porcelain(plumbing):
    porcelain = models.RoleGetResponse()
    
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def role_get_response_to_plumbing(porcelain):
    plumbing = RoleGetResponse()
    if porcelain.meta != None:
        
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_role_get_response_to_plumbing(porcelains):
    return [role_get_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_get_response_to_porcelain(plumbings):
    return [role_get_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_update_response_to_porcelain(plumbing):
    porcelain = models.RoleUpdateResponse()
    
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def role_update_response_to_plumbing(porcelain):
    plumbing = RoleUpdateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_role_update_response_to_plumbing(porcelains):
    return [role_update_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_update_response_to_porcelain(plumbings):
    return [role_update_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_delete_response_to_porcelain(plumbing):
    porcelain = models.RoleDeleteResponse()
    
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.rate_limit = rate_limit_metadata_to_porcelain(plumbing.rate_limit)
    return porcelain

def role_delete_response_to_plumbing(porcelain):
    plumbing = RoleDeleteResponse()
    if porcelain.meta != None:
        
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.rate_limit != None:
        
        plumbing.rate_limit = rate_limit_metadata_to_plumbing(porcelain.rate_limit)
        
    return plumbing

def repeated_role_delete_response_to_plumbing(porcelains):
    return [role_delete_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_delete_response_to_porcelain(plumbings):
    return [role_delete_response_to_porcelain(plumbing) for plumbing in plumbings]

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
    if (hasattr(x, 'key') and (hasattr(x, 'value')) and x.key.startswith('grpc-status-details')):
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
        return errors.RPCError(str(err), 2) // Unknown
    if err.code().name == 'DEADLINE_EXCEEDED':
        code, name = err.code().value
        return errors.TimeoutError()
    status = get_status_metadata(err)
    if status is None:
        code, name = err.code().value
        return errors.RPCError(name, code)
    for detail in status.details:
        # AlreadyExistsError is used when an entity already exists in the system
        if detail.Is(AlreadyExistsError.DESCRIPTOR):
            plumbing = AlreadyExistsError()
            detail.Unpack(plumbing)
            return errors.AlreadyExistsError(status.message, plumbing.entity)
        # NotFoundError is used when an entity does not exist in the system
        if detail.Is(NotFoundError.DESCRIPTOR):
            plumbing = NotFoundError()
            detail.Unpack(plumbing)
            return errors.NotFoundError(status.message, plumbing.entity)
        # BadRequestError identifies a bad request sent by the client
        if detail.Is(BadRequestError.DESCRIPTOR):
            plumbing = BadRequestError()
            detail.Unpack(plumbing)
            return errors.BadRequestError(status.message)
        # AuthenticationError is used to specify an authentication failure condition
        if detail.Is(AuthenticationError.DESCRIPTOR):
            plumbing = AuthenticationError()
            detail.Unpack(plumbing)
            return errors.AuthenticationError(status.message)
        # PermissionError is used to specify a permissions violation
        if detail.Is(PermissionError.DESCRIPTOR):
            plumbing = PermissionError()
            detail.Unpack(plumbing)
            return errors.PermissionError(status.message)
        # InternalError is used to specify an internal system error
        if detail.Is(InternalError.DESCRIPTOR):
            plumbing = InternalError()
            detail.Unpack(plumbing)
            return errors.InternalError(status.message)
        # RateLimitError is used for rate limit excess condition
        if detail.Is(RateLimitError.DESCRIPTOR):
            plumbing = RateLimitError()
            detail.Unpack(plumbing)
            return errors.RateLimitError(status.message)
    code = err.code().value[0]
    return errors.RPCError(status.message, code)