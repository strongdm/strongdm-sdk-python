# RequestMetadata 
class RequestMetadata:
    page: string 
# ResponseMetadata 
class ResponseMetadata:
    next_page: string 

    found: int64 

    affected: int64 

class NodeCreateRequest:
    metadata: RequestMetadata 

    node: Node 

class NodeCreateResponse:
    metadata: ResponseMetadata 

    node: Node 

class NodeUpdateRequest:
    metadata: RequestMetadata 

    node: Node 

class NodeUpdateResponse:
    metadata: ResponseMetadata 

    node: Node 

class NodeDeleteRequest:
    metadata: RequestMetadata 

    id: string 

class NodeDeleteResponse:
    metadata: ResponseMetadata 

class NodeListRequest:
    metadata: RequestMetadata 

class NodeListResponse:
    metadata: ResponseMetadata 

    nodes: Node 

class NodeGetRequest:
    metadata: RequestMetadata 

    id: string 

class NodeGetResponse:
    metadata: ResponseMetadata 

    node: Node 

class ErrorDetail:
    message: string 
# Node is a domain object. 
class Node:
    id: string # id is the unique ID for this relay. 

    relay: Relay 

    gateway: Gateway 

class Relay:
    name: string # name is the human readable unique name for this relay. 

class Gateway:
    name: string # name is the human readable unique name for this relay. 

    listen_address: string # listen_address represents the network address to which nodes should dial to. 

    bind_address: string # bind_address represents the local network address to which the gateway
 must try to bind itself. 


class Nodes:
    """Nodes service""" 
    def __init__(self):
        # TODO: initialize something
    
    
    def create(self, reqeust: NodeCreateRequest):
        """Create adds a new nodes, and returns the newly created node.""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/nodes by POST
        # Body: *
        # ResponseBody: 
        return NodeCreateResponse()
    
    def update(self, reqeust: NodeUpdateRequest):
        """Update modifies an existing node""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/nodes/{node.id} by POST
        # Body: *
        # ResponseBody: 
        return NodeUpdateResponse()
    
    def delete(self, reqeust: NodeDeleteRequest):
        """Delete removes an existing node""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/nodes/{id} by DELETE
        # Body: 
        # ResponseBody: 
        return NodeDeleteResponse()
    
    def list(self, reqeust: NodeListRequest):
        """List returns all existing nodes""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/nodes by GET
        # Body: 
        # ResponseBody: 
        return NodeListResponse()
    
    def get(self, reqeust: NodeGetRequest):
        """Get finds a node by id""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/nodes/{id} by GET
        # Body: 
        # ResponseBody: 
        return NodeGetResponse()
    


