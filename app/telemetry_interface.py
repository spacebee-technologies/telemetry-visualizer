import struct

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    


class TelemetryInterface(metaclass=SingletonMeta):

    timestamp=None              # 64 bits	time in milliseconds
    interaction_stage = 1       # 8 bits	1 or 2 according to message order
    transaction_id = None       # Unique incremental identifier
    service= 0                  # 0 for telemetries (TM) or 1 for telecommands (TC)
    operation=None              # 16 bits	Unique identifier for a given telemetry or telecommand
    area_version=None           # 16 bits	Protocol version
    data={}                     # Dictionary with all the telemetry data

    name=""                     # string Name of the telemetry
    help=""                     # string Description and usage for the telemetry

    def loadParameters(self,data,transaction_id,timestamp,area_version):
        self.transaction_id=transaction_id
        self.timestamp=timestamp
        self.area_version=area_version
        self.data=data

    def getOperationNumber(self):
        return self.operation

    def parseData(self,body):
        "Parse the output argument, where the body is a byte sequence, and return a dictionary."
        raise NotImplementedError("Telemetry must implement this method")










