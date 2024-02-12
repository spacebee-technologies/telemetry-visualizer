from telemetry_interface import TelemetryInterface
import struct


class Current_M6(TelemetryInterface):
    def __init__(self):
        self.name="Current Motor 6 [A]"
        self.help=""
        self.operation=10
        self.area_version=0


    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        current= struct.unpack('<f', body)[0]
        data["Current"]=current
        return data
