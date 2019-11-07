import grpc
import google.rpc as rpc
from google.rpc import status_pb2
import errors
from options_pb2 import *
from spec_pb2 import *
from nodes_pb2 import *
import models

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

def batch_update_response_metadata_to_porcelain(plumbing):
    porcelain = models.BatchUpdateResponseMetadata()
    
    porcelain.found = plumbing.found
    
    porcelain.affected = plumbing.affected
    return porcelain

def batch_update_response_metadata_to_plumbing(porcelain):
    plumbing = BatchUpdateResponseMetadata()
    if porcelain.found != None:
        
        plumbing.found = porcelain.found
        
    if porcelain.affected != None:
        
        plumbing.affected = porcelain.affected
        
    return plumbing

def repeated_batch_update_response_metadata_to_plumbing(porcelains):
    return [batch_update_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_batch_update_response_metadata_to_porcelain(plumbings):
    return [batch_update_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def batch_delete_response_metadata_to_porcelain(plumbing):
    porcelain = models.BatchDeleteResponseMetadata()
    
    porcelain.found = plumbing.found
    
    porcelain.affected = plumbing.affected
    return porcelain

def batch_delete_response_metadata_to_plumbing(porcelain):
    plumbing = BatchDeleteResponseMetadata()
    if porcelain.found != None:
        
        plumbing.found = porcelain.found
        
    if porcelain.affected != None:
        
        plumbing.affected = porcelain.affected
        
    return plumbing

def repeated_batch_delete_response_metadata_to_plumbing(porcelains):
    return [batch_delete_response_metadata_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_batch_delete_response_metadata_to_porcelain(plumbings):
    return [batch_delete_response_metadata_to_porcelain(plumbing) for plumbing in plumbings]

def node_create_response_to_porcelain(plumbing):
    porcelain = models.NodeCreateResponse()
    
    porcelain.meta = create_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.nodes = node_to_porcelain(plumbing.nodes)
    
    porcelain.tokens = token_to_porcelain(plumbing.tokens)
    return porcelain

def node_create_response_to_plumbing(porcelain):
    plumbing = NodeCreateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = create_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.nodes != None:
        
        plumbing.nodes = node_to_plumbing(porcelain.nodes)
        
    if porcelain.tokens != None:
        
        plumbing.tokens = token_to_plumbing(porcelain.tokens)
        
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

def node_list_response_to_porcelain(plumbing):
    porcelain = models.NodeListResponse()
    
    porcelain.meta = list_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.nodes = node_to_porcelain(plumbing.nodes)
    return porcelain

def node_list_response_to_plumbing(porcelain):
    plumbing = NodeListResponse()
    if porcelain.meta != None:
        
        plumbing.meta = list_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.nodes != None:
        
        plumbing.nodes = node_to_plumbing(porcelain.nodes)
        
    return plumbing

def repeated_node_list_response_to_plumbing(porcelains):
    return [node_list_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_list_response_to_porcelain(plumbings):
    return [node_list_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_batch_update_response_to_porcelain(plumbing):
    porcelain = models.NodeBatchUpdateResponse()
    
    porcelain.meta = batch_update_response_metadata_to_porcelain(plumbing.meta)
    
    porcelain.nodes = node_to_porcelain(plumbing.nodes)
    return porcelain

def node_batch_update_response_to_plumbing(porcelain):
    plumbing = NodeBatchUpdateResponse()
    if porcelain.meta != None:
        
        plumbing.meta = batch_update_response_metadata_to_plumbing(porcelain.meta)
        
    if porcelain.nodes != None:
        
        plumbing.nodes = node_to_plumbing(porcelain.nodes)
        
    return plumbing

def repeated_node_batch_update_response_to_plumbing(porcelains):
    return [node_batch_update_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_batch_update_response_to_porcelain(plumbings):
    return [node_batch_update_response_to_porcelain(plumbing) for plumbing in plumbings]

def node_batch_delete_response_to_porcelain(plumbing):
    porcelain = models.NodeBatchDeleteResponse()
    
    porcelain.meta = batch_delete_response_metadata_to_porcelain(plumbing.meta)
    return porcelain

def node_batch_delete_response_to_plumbing(porcelain):
    plumbing = NodeBatchDeleteResponse()
    if porcelain.meta != None:
        
        plumbing.meta = batch_delete_response_metadata_to_plumbing(porcelain.meta)
        
    return plumbing

def repeated_node_batch_delete_response_to_plumbing(porcelains):
    return [node_batch_delete_response_to_plumbing(porcelain) for porcelain in porcelains]

def repeated_node_batch_delete_response_to_porcelain(plumbings):
    return [node_batch_delete_response_to_porcelain(plumbing) for plumbing in plumbings]

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
        return Error(str(err))

    status = get_status_metadata(err)
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
    return RPCError(status.message, err.code())