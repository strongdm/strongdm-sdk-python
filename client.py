import grpc
import hmac
import hashlib
import base64
import datetime
from . import svc
from . import plumbing


# Client is a strongDM API client.
class Client:
    # Creates a new strongDM API client. The `addr` parameter expects a hostname/port tuple.
    def __init__(self, addr, api_access_key, api_secret):
        self.api_access_key = api_access_key
        self.api_secret = base64.b64decode(api_secret)

        try:
            channel = grpc.insecure_channel(addr)
            if addr.endswith('443'):
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(addr, creds)
            self.nodes = svc.Nodes(channel, self)
            self.role_attachments = svc.RoleAttachments(channel, self)
            self.roles = svc.Roles(channel, self)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        self._test_options = {}

    def get_metadata(self, method_name, req):
        return [('x-sdm-authentication', self.api_access_key),
                ('x-sdm-signature',
                 self.sign(method_name, req.SerializeToString()))]

    def sign(self, method_name, request_bytes):
        def hmac_digest(key, msg_byte_string):
            return hmac.new(key, msg=msg_byte_string,
                            digestmod=hashlib.sha256).digest()

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        signing_key = hmac_digest(self.api_secret, current_date.encode())
        signing_key = hmac_digest(signing_key, b'sdm_api_v1')

        hash = hashlib.sha256()

        hash.update(method_name.encode())
        hash.update(b'\n')
        hash.update(request_bytes)

        return base64.b64encode(hmac_digest(signing_key, hash.digest()))
