# RequestMetadata 
class RequestMetadata:
    page: string 
# ResponseMetadata 
class ResponseMetadata:
    next_page: string 

    found: int64 

    affected: int64 

class RelayCreateRequest:
    metadata: RequestMetadata 

    node: Node 

class RelayCreateResponse:
    metadata: ResponseMetadata 

    node: Node 

class RelayUpdateRequest:
    metadata: RequestMetadata 

    node: Node 

class RelayUpdateResponse:
    metadata: ResponseMetadata 

    node: Node 

class RelayDeleteRequest:
    metadata: RequestMetadata 

    id: string 

class RelayDeleteResponse:
    metadata: ResponseMetadata 

class RelayListRequest:
    metadata: RequestMetadata 

class RelayListResponse:
    metadata: ResponseMetadata 

    nodes: Node 

class RelayGetRequest:
    metadata: RequestMetadata 

    id: string 

class RelayGetResponse:
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


class Relays:
    """Relays service""" 
    def __init__(self):
        # TODO: initialize something
    
    
    def create(self, reqeust: RelayCreateRequest):
        """Create adds a new relay, and returns the new relay""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/relays by POST
        # Body: *
        # ResponseBody: 
        return RelayCreateResponse()
    
    def update(self, reqeust: RelayUpdateRequest):
        """Update modifies an existing relay""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/relays/{node.id} by POST
        # Body: *
        # ResponseBody: 
        return RelayUpdateResponse()
    
    def delete(self, reqeust: RelayDeleteRequest):
        """Delete removes an existing relay""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/relays/{id} by DELETE
        # Body: 
        # ResponseBody: 
        return RelayDeleteResponse()
    
    def list(self, reqeust: RelayListRequest):
        """List returns all existing relays""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/relays by GET
        # Body: 
        # ResponseBody: 
        return RelayListResponse()
    
    def get(self, reqeust: RelayGetRequest):
        """Get finds a sandwich by id""" 
        # TODO: implement this
        # Host: app.strongdm.com
        # BasePath: 
        # Dial to /v1/relays/{id} by GET
        # Body: 
        # ResponseBody: 
        return RelayGetResponse()
    


