import collections


# CreateResponseMetadata
class CreateResponseMetadata:
    __slots__ = ['affected']
    def __init__(self):
        self.affected = None

# GetResponseMetadata
class GetResponseMetadata:
    __slots__ = ['found']
    def __init__(self):
        self.found = None

# UpdateResponseMetadata
class UpdateResponseMetadata:
    __slots__ = ['affected']
    def __init__(self):
        self.affected = None

# DeleteResponseMetadata
class DeleteResponseMetadata:
    __slots__ = ['affected']
    def __init__(self):
        self.affected = None

# BatchUpdateResponseMetadata
class BatchUpdateResponseMetadata:
    __slots__ = ['found', 'affected']
    def __init__(self):
        self.found = None
        self.affected = None

# BatchDeleteResponseMetadata
class BatchDeleteResponseMetadata:
    __slots__ = ['found', 'affected']
    def __init__(self):
        self.found = None
        self.affected = None

# NodeCreateResponse reports how the nodes were created in the system. It can
# communicate partial successes or failures.
class NodeCreateResponse:
    __slots__ = ['meta', 'nodes', 'tokens']
    def __init__(self):
        self.meta = None
        self.nodes = None
        self.tokens = None

# NodeGetResponse returns a requested node.
class NodeGetResponse:
    __slots__ = ['meta', 'node']
    def __init__(self):
        self.meta = None
        self.node = None

# NodeUpdateResponse returns the fields of a node after it has been updated by
# a NodeUpdateRequest.
class NodeUpdateResponse:
    __slots__ = ['meta', 'node']
    def __init__(self):
        self.meta = None
        self.node = None

# NodeDeleteResponse returns information about a node that was deleted.
class NodeDeleteResponse:
    __slots__ = ['meta']
    def __init__(self):
        self.meta = None

# NodeListResponse returns a list of nodes that meet the criteria of a
# NodeListRequest.
class NodeListResponse:
    __slots__ = ['nodes']
    def __init__(self):
        self.nodes = None

# NodeBatchUpdateResponse returns a list of nodes updated via
# NodeBatchUpdateRequest.
class NodeBatchUpdateResponse:
    __slots__ = ['meta', 'nodes']
    def __init__(self):
        self.meta = None
        self.nodes = None

# NodeBatchDeleteResponse returns information about nodes deleted via a
# NodeBatchDeleteRequest.
class NodeBatchDeleteResponse:
    __slots__ = ['meta']
    def __init__(self):
        self.meta = None

# Relay represents a StrongDM CLI installation running in relay mode.
class Relay:
    __slots__ = ['id', 'name']
    def __init__(self):
        self.id = None
        self.name = None

# Gateway represents a StrongDM CLI installation running in gateway mode.
class Gateway:
    __slots__ = ['id', 'name', 'listen_address', 'bind_address']
    def __init__(self):
        self.id = None
        self.name = None
        self.listen_address = None
        self.bind_address = None

# Token holds the bearer token used to start up nodes.
class Token:
    __slots__ = ['id', 'token']
    def __init__(self):
        self.id = None
        self.token = None
