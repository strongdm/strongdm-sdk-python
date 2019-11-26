# RPCError is a generic RPC error
class RPCError(Exception):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code

# AlreadyExistsError is used when an entity already exists in the system
class AlreadyExistsError(RPCError):
    def __init__(self, msg, entity):
        super().__init__(msg, 6)
        self.entity = entity

# NotFoundError is used when an entity does not exist in the system
class NotFoundError(RPCError):
    def __init__(self, msg, entity):
        super().__init__(msg, 5)
        self.entity = entity

# BadRequestError identifies a bad request sent by the client
class BadRequestError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 3)

# AuthenticationError is used to specify an authentication failure condition
class AuthenticationError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 16)

# PermissionError is used to specify a permissions violation
class PermissionError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 7)

# InternalError is used to specify an internal system error
class InternalError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 13)

# RateLimitError is used for rate limit excess condition
class RateLimitError(RPCError):
    def __init__(self, msg):
        super().__init__(msg, 8)


class TimeoutError(RPCError):
    def __init__(self):
        super().__init__('deadline exceeded', 4)