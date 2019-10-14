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

    relay: Relay 

class RelayCreateResponse:
    metadata: ResponseMetadata 

    relay: Relay 

class RelayUpdateRequest:
    metadata: RequestMetadata 

    relay: Relay 

class RelayUpdateResponse:
    metadata: ResponseMetadata 

    relay: Relay 

class RelayDeleteRequest:
    metadata: RequestMetadata 

    id: string 

class RelayDeleteResponse:
    metadata: ResponseMetadata 

class RelayListRequest:
    metadata: RequestMetadata 

class RelayListResponse:
    metadata: ResponseMetadata 

    relays: Relay 

class RelayGetRequest:
    metadata: RequestMetadata 

    id: string 

class RelayGetResponse:
    metadata: ResponseMetadata 

    relay: Relay 

class ErrorDetail:
    message: string 
# Relay is a domain object. 
class Relay:
    id: string # id is the unique ID for this relay. 

    name: string # name is the human readable unique name for this relay. 


class Relays:
    """Relays service""" 
    def __init__(self):
        # TODO: initialize something
    
    
    def create(self, reqeust: RelayCreateRequest):
        """Create adds a new relay, and returns the new relay""" 
        # TODO: implement this
        # Host: http://app.strongdm.com/
        # BasePath: 
        # Dial to /v1/relays by POST
        # Body: *
        # ResponseBody: 
        return RelayCreateResponse()
    
    def update(self, reqeust: RelayUpdateRequest):
        """Update modifies an existing relay""" 
        # TODO: implement this
        # Host: http://app.strongdm.com/
        # BasePath: 
        # Dial to /v1/relays/{relay.id} by POST
        # Body: *
        # ResponseBody: 
        return RelayUpdateResponse()
    
    def delete(self, reqeust: RelayDeleteRequest):
        """Delete removes an existing relay""" 
        # TODO: implement this
        # Host: http://app.strongdm.com/
        # BasePath: 
        # Dial to /v1/relays/{id} by DELETE
        # Body: 
        # ResponseBody: 
        return RelayDeleteResponse()
    
    def list(self, reqeust: RelayListRequest):
        """List returns all existing relays""" 
        # TODO: implement this
        # Host: http://app.strongdm.com/
        # BasePath: 
        # Dial to /v1/relays by GET
        # Body: 
        # ResponseBody: 
        return RelayListResponse()
    
    def get(self, reqeust: RelayGetRequest):
        """Get finds a sandwich by id""" 
        # TODO: implement this
        # Host: http://app.strongdm.com/
        # BasePath: 
        # Dial to /v1/relays/{id} by GET
        # Body: 
        # ResponseBody: 
        return RelayGetResponse()
    
class Relays2:
    """This is relay2 service""" 
    def __init__(self):
        # TODO: initialize something
    
    


