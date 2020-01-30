import grpc
import hmac
import random
import hashlib
import base64
import datetime
import time
from . import svc
from . import plumbing

# These defaults are taken from AWS. Customization of these values
# is a future step in the API.
DEFAULT_MAX_RETRIES = 3
DEFAULT_BASE_RETRY_DELAY = 0.0030  # 30 ms
DEFAULT_MAX_RETRY_DELAY = 300  # 300 seconds


# Client is a strongDM API client.
class Client:
    # Creates a new strongDM API client. The `addr` parameter expects a hostname/port tuple.
    def __init__(self, addr, api_access_key, api_secret):
        self.api_access_key = api_access_key
        self.api_secret = base64.b64decode(api_secret)
        self.max_retries = DEFAULT_MAX_RETRIES
        self.base_retry_delay = DEFAULT_BASE_RETRY_DELAY
        self.max_retry_delay = DEFAULT_MAX_RETRY_DELAY

        try:
            channel = grpc.insecure_channel(addr)
            if addr.endswith('443'):
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(addr, creds)
            self.account_grants = svc.AccountGrants(channel, self)
            self.accounts = svc.Accounts(channel, self)
            self.nodes = svc.Nodes(channel, self)
            self.resources = svc.Resources(channel, self)
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

        current_utc_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
        signing_key = hmac_digest(self.api_secret, current_utc_date.encode())
        signing_key = hmac_digest(signing_key, b'sdm_api_v1')

        hash = hashlib.sha256()

        hash.update(method_name.encode())
        hash.update(b'\n')
        hash.update(request_bytes)

        return base64.b64encode(hmac_digest(signing_key, hash.digest()))

    def jitterSleep(self, iter):
        dur_max = self.base_retry_delay * 2**iter
        if (dur_max > self.max_retry_delay):
            dur_max = self.max_retry_delay
        # get a value between 0 and max
        dur = random.random() * dur_max
        time.sleep(dur)

    def shouldRetry(self, iter, err):
        if (iter >= self.max_retries - 1):
            return False
        if not isinstance(err, grpc.RpcError):
            return True
        return err.code() == grpc.StatusCode.INTERNAL
