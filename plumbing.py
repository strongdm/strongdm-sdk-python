import grpc
import google.rpc as rpc
from google.rpc import status_pb2
from . import errors
from . import models
from .options_pb2 import *
from .spec_pb2 import *
from .nodes_pb2 import *
from .roles_pb2 import *

def create_response_metadata_to_porcelain(plumbing):
    porcelain = models.CreateResponseMetadata()
    
    porcelain.affected = plumbing.affected
    return porcelain

def create_response_metadata_to_plumbing(porcelain):
    plumbing = CreateResponseMetadata()
    if porcelain.affected != None:
        
        plumbing.affected = porcelain.affected
        
    return plumbing

def repeated_create_response_metadata_to_plumbing(porcelains):
    return [create_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_create_response_metadata_to_porcelain(plumbings):
    return [create_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def get_response_metadata_to_porcelain(plumbing):
    porcelain = models.GetResponseMetadata()
    
    porcelain.found = plumbing.found
    return porcelain

def get_response_metadata_to_plumbing(porcelain):
    plumbing = GetResponseMetadata()
    if porcelain.found != None:
        
        plumbing.found = porcelain.found
        
    return plumbing

def repeated_get_response_metadata_to_plumbing(porcelains):
    return [get_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_get_response_metadata_to_porcelain(plumbings):
    return [get_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def update_response_metadata_to_porcelain(plumbing):
    porcelain = models.UpdateResponseMetadata()
    
    porcelain.affected = plumbing.affected
    return porcelain

def update_response_metadata_to_plumbing(porcelain):
    plumbing = UpdateResponseMetadata()
    if porcelain.affected != None:
        
        plumbing.affected = porcelain.affected
        
    return plumbing

def repeated_update_response_metadata_to_plumbing(porcelains):
    return [update_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_update_response_metadata_to_porcelain(plumbings):
    return [update_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def delete_response_metadata_to_porcelain(plumbing):
    porcelain = models.DeleteResponseMetadata()
    
    porcelain.affected = plumbing.affected
    return porcelain

def delete_response_metadata_to_plumbing(porcelain):
    plumbing = DeleteResponseMetadata()
    if porcelain.affected != None:
        
        plumbing.affected = porcelain.affected
        
    return plumbing

def repeated_delete_response_metadata_to_plumbing(porcelains):
    return [delete_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_delete_response_metadata_to_porcelain(plumbings):
    return [delete_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def node_create_response_to_porcelain(plumbing):
    porcelain = models.NodeCreateResponse()
    
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    
    porcelain.token = token_to_porcelain(plumbing.token)
    return porcelain

def node_create_response_to_plumbing(porcelain):
    plumbing = NodeCreateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.node != None:
        
        plumbing.node = node_to_plumbing(porcelain.node)
        
    if porcelain.token != None:
        
        plumbing.token = token_to_plumbing(porcelain.token)
        
    return plumbing

def repeated_node_create_response_to_plumbing(porcelains):
    return [node_create_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_create_response_to_porcelain(plumbings):
    return [node_create_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_get_response_to_porcelain(plumbing):
    porcelain = models.NodeGetResponse()
    
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    return porcelain

def node_get_response_to_plumbing(porcelain):
    plumbing = NodeGetResponse()
    if porcelain.meta != None:
        
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.node != None:
        
        plumbing.node = node_to_plumbing(porcelain.node)
        
    return plumbing

def repeated_node_get_response_to_plumbing(porcelains):
    return [node_get_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_get_response_to_porcelain(plumbings):
    return [node_get_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_update_response_to_porcelain(plumbing):
    porcelain = models.NodeUpdateResponse()
    
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.node = node_to_porcelain(plumbing.node)
    return porcelain

def node_update_response_to_plumbing(porcelain):
    plumbing = NodeUpdateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.node != None:
        
        plumbing.node = node_to_plumbing(porcelain.node)
        
    return plumbing

def repeated_node_update_response_to_plumbing(porcelains):
    return [node_update_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_update_response_to_porcelain(plumbings):
    return [node_update_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_delete_response_to_porcelain(plumbing):
    porcelain = models.NodeDeleteResponse()
    
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    return porcelain

def node_delete_response_to_plumbing(porcelain):
    plumbing = NodeDeleteResponse()
    if porcelain.meta != None:
        
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
        
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
    return porcelain

def relay_to_plumbing(porcelain):
    plumbing = Relay()
    if porcelain.id != None:
        
        plumbing.id = porcelain.id
        
    if porcelain.name != None:
        
        plumbing.name = porcelain.name
        
    return plumbing

def repeated_relay_to_plumbing(porcelains):
    return [relay_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_relay_to_porcelain(plumbings):
    return [relay_to_porcelain(plumbing) for plumbing in plumbings]

def gateway_to_porcelain(plumbing):
    porcelain = models.Gateway()
    
    porcelain.id = plumbing.id
    
    porcelain.name = plumbing.name
    
    porcelain.listen_address = plumbing.listen_address
    
    porcelain.bind_address = plumbing.bind_address
    return porcelain

def gateway_to_plumbing(porcelain):
    plumbing = Gateway()
    if porcelain.id != None:
        
        plumbing.id = porcelain.id
        
    if porcelain.name != None:
        
        plumbing.name = porcelain.name
        
    if porcelain.listen_address != None:
        
        plumbing.listen_address = porcelain.listen_address
        
    if porcelain.bind_address != None:
        
        plumbing.bind_address = porcelain.bind_address
        
    return plumbing

def repeated_gateway_to_plumbing(porcelains):
    return [gateway_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_gateway_to_porcelain(plumbings):
    return [gateway_to_porcelain(plumbing) for plumbing in plumbings]

def token_to_porcelain(plumbing):
    porcelain = models.Token()
    
    porcelain.id = plumbing.id
    
    porcelain.token = plumbing.token
    return porcelain

def token_to_plumbing(porcelain):
    plumbing = Token()
    if porcelain.id != None:
        
        plumbing.id = porcelain.id
        
    if porcelain.token != None:
        
        plumbing.token = porcelain.token
        
    return plumbing

def repeated_token_to_plumbing(porcelains):
    return [token_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_token_to_porcelain(plumbings):
    return [token_to_porcelain(plumbing) for plumbing in plumbings]

def role_create_response_to_porcelain(plumbing):
    porcelain = models.RoleCreateResponse()
    
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    return porcelain

def role_create_response_to_plumbing(porcelain):
    plumbing = RoleCreateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    return plumbing

def repeated_role_create_response_to_plumbing(porcelains):
    return [role_create_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_create_response_to_porcelain(plumbings):
    return [role_create_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_get_response_to_porcelain(plumbing):
    porcelain = models.RoleGetResponse()
    
    porcelain.meta = get_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    return porcelain

def role_get_response_to_plumbing(porcelain):
    plumbing = RoleGetResponse()
    if porcelain.meta != None:
        
        plumbing.meta = get_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    return plumbing

def repeated_role_get_response_to_plumbing(porcelains):
    return [role_get_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_get_response_to_porcelain(plumbings):
    return [role_get_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_update_response_to_porcelain(plumbing):
    porcelain = models.RoleUpdateResponse()
    
    porcelain.meta = update_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.role = role_to_porcelain(plumbing.role)
    return porcelain

def role_update_response_to_plumbing(porcelain):
    plumbing = RoleUpdateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = update_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.role != None:
        
        plumbing.role = role_to_plumbing(porcelain.role)
        
    return plumbing

def repeated_role_update_response_to_plumbing(porcelains):
    return [role_update_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_role_update_response_to_porcelain(plumbings):
    return [role_update_response_to_porcelain(plumbing) for plumbing in plumbings]

def role_delete_response_to_porcelain(plumbing):
    porcelain = models.RoleDeleteResponse()
    
    porcelain.meta = delete_response_metadata_to_porcelain(plumbing.meta)
    return porcelain

def role_delete_response_to_plumbing(porcelain):
    plumbing = RoleDeleteResponse()
    if porcelain.meta != None:
        
        plumbing.meta = delete_response_metadata_to_plumbing(porcelain.meta)
        
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
    
    porcelain.roles = role_to_porcelain(plumbing.roles)
    return porcelain

def role_to_plumbing(porcelain):
    plumbing = Role()
    if porcelain.id != None:
        
        plumbing.id = porcelain.id
        
    if porcelain.name != None:
        
        plumbing.name = porcelain.name
        
    if porcelain.composite != None:
        
        plumbing.composite = porcelain.composite
        
    if porcelain.roles != None:
        
        plumbing.roles = role_to_plumbing(porcelain.roles)
        
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
        return errors.Error(str(err))

    status = get_status_metadata(err)
    if status is None:
        return errors.Error(str(err))
    for detail in status.details:
        # AlreadyExistsError is used when an entity already exists in the system
        if detail.Is(AlreadyExistsError.DESCRIPTOR):
            plumbing = AlreadyExistsError()
            detail.Unpack(plumbing)
            return errors.AlreadyExistsError(status.message, plumbing.entities)
        # NotFoundError is used when an entity does not exist in the system
        if detail.Is(NotFoundError.DESCRIPTOR):
            plumbing = NotFoundError()
            detail.Unpack(plumbing)
            return errors.NotFoundError(status.message, plumbing.entities)
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
            return errors.PermissionError(status.message, plumbing.permission, plumbing.entities)
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
    return errors.RPCError(status.message, err.code())