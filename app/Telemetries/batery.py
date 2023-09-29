from telemetry_interface import TelemetryInterface
import struct


class battery(TelemetryInterface):
    def __init__(self):
        self.name="Battery"
        self.help=""
        self.operation=2
        self.area_version=0


    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        voltaje= struct.unpack('f', body)[0]
        data["Voltaje"]=voltaje
        return data
