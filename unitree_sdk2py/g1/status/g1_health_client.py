import json
from ...rpc.client import Client
from .g1_health_api import *

class G1HealthClient(Client):
    def __init__(self):
        super().__init__(HEALTH_SERVICE_NAME, False)
        self._SetApiVerson(HEALTH_API_VERSION)
        self._RegistApi(ROBOT_API_ID_GET_HEALTH_STATUS, 0)

    def GetHealthStatus(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(ROBOT_API_ID_GET_HEALTH_STATUS, parameter)
        if code == 0:
            return code, json.loads(data)
        else:
            return code, None