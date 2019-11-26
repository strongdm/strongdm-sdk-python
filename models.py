import collections


# CreateResponseMetadata is reserved for future use.
class CreateResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.CreateResponseMetadata>'.format()

# GetResponseMetadata is reserved for future use.
class GetResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.GetResponseMetadata>'.format()

# UpdateResponseMetadata is reserved for future use.
class UpdateResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.UpdateResponseMetadata>'.format()

# DeleteResponseMetadata is reserved for future use.
class DeleteResponseMetadata:
    __slots__ = []
    def __init__(self):
        pass
    def __repr__(self):
        return '<sdm.DeleteResponseMetadata>'.format()

# NodeCreateResponse reports how the Nodes were created in the system.
# meta: Reserved for future use.
# node: The created Node.
# token: The auth token generated for the Node. The Node will use this token to
# authenticate with the strongDM API.
class NodeCreateResponse:
    __slots__ = ['meta', 'node', 'token']
    def __init__(self):
        self.meta = None
        self.node = None
        self.token = None
    def __repr__(self):
        return '<sdm.NodeCreateResponse meta: {0} node: {1} token: {2}>'.format(repr(self.meta), repr(self.node), repr(self.token))

# NodeGetResponse returns a requested Node.
# meta: Reserved for future use.
# node: The requested Node.
class NodeGetResponse:
    __slots__ = ['meta', 'node']
    def __init__(self):
        self.meta = None
        self.node = None
    def __repr__(self):
        return '<sdm.NodeGetResponse meta: {0} node: {1}>'.format(repr(self.meta), repr(self.node))

# NodeUpdateResponse returns the fields of a Node after it has been updated by
# a NodeUpdateRequest.
# meta: Reserved for future use.
# node: The updated Node.
class NodeUpdateResponse:
    __slots__ = ['meta', 'node']
    def __init__(self):
        self.meta = None
        self.node = None
    def __repr__(self):
        return '<sdm.NodeUpdateResponse meta: {0} node: {1}>'.format(repr(self.meta), repr(self.node))

# NodeDeleteResponse returns information about a Node that was deleted.
# meta: Reserved for future use.
class NodeDeleteResponse:
    __slots__ = ['meta']
    def __init__(self):
        self.meta = None
    def __repr__(self):
        return '<sdm.NodeDeleteResponse meta: {0}>'.format(repr(self.meta))

# Relay represents a StrongDM CLI installation running in relay mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the relay. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
class Relay:
    __slots__ = ['id', 'name', 'state']
    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
    def __repr__(self):
        return '<sdm.Relay id: {0} name: {1} state: {2}>'.format(repr(self.id), repr(self.name), repr(self.state))

# Gateway represents a StrongDM CLI installation running in gateway mode.
# id: Unique identifier of the Relay.
# name: Unique human-readable name of the Relay.
# state: The current state of the gateway. One of: "new", "verifying_restart",
# "restarting", "started", "stopped", "dead", "unknown",
# listen_address: The public hostname/port tuple at which the gateway will be accessible to clients.
# bind_address: The hostname/port tuple which the gateway daemon will bind to.
class Gateway:
    __slots__ = ['id', 'name', 'state', 'listen_address', 'bind_address']
    def __init__(self):
        self.id = None
        self.name = None
        self.state = None
        self.listen_address = None
        self.bind_address = None
    def __repr__(self):
        return '<sdm.Gateway id: {0} name: {1} state: {2} listen_address: {3} bind_address: {4}>'.format(repr(self.id), repr(self.name), repr(self.state), repr(self.listen_address), repr(self.bind_address))

# RoleCreateResponse reports how the Roles were created in the system. It can
# communicate partial successes or failures.
# meta: Reserved for future use.
# role: The created Role.
class RoleCreateResponse:
    __slots__ = ['meta', 'role']
    def __init__(self):
        self.meta = None
        self.role = None
    def __repr__(self):
        return '<sdm.RoleCreateResponse meta: {0} role: {1}>'.format(repr(self.meta), repr(self.role))

# RoleGetResponse returns a requested Role.
# meta: Reserved for future use.
# role: The requested Role.
class RoleGetResponse:
    __slots__ = ['meta', 'role']
    def __init__(self):
        self.meta = None
        self.role = None
    def __repr__(self):
        return '<sdm.RoleGetResponse meta: {0} role: {1}>'.format(repr(self.meta), repr(self.role))

# RoleUpdateResponse returns the fields of a Role after it has been updated by
# a RoleUpdateRequest.
# meta: Reserved for future use.
# role: The updated Role.
class RoleUpdateResponse:
    __slots__ = ['meta', 'role']
    def __init__(self):
        self.meta = None
        self.role = None
    def __repr__(self):
        return '<sdm.RoleUpdateResponse meta: {0} role: {1}>'.format(repr(self.meta), repr(self.role))

# RoleDeleteResponse returns information about a Role that was deleted.
# meta: Reserved for future use.
class RoleDeleteResponse:
    __slots__ = ['meta']
    def __init__(self):
        self.meta = None
    def __repr__(self):
        return '<sdm.RoleDeleteResponse meta: {0}>'.format(repr(self.meta))

# A Role grants users access to a set of resources. Composite roles have no
# resource associations of their own, but instead grant access to the combined
# resources of their child roles.
# id: Unique identifier of the Role.
# name: Unique human-readable name of the Role.
# composite: True if the Role is a composite role.
class Role:
    __slots__ = ['id', 'name', 'composite']
    def __init__(self):
        self.id = None
        self.name = None
        self.composite = None
    def __repr__(self):
        return '<sdm.Role id: {0} name: {1} composite: {2}>'.format(repr(self.id), repr(self.name), repr(self.composite))
