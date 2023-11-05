from telemetry_interface import TelemetryInterface
import struct


class accelerometer(TelemetryInterface):
    def __init__(self):
        self.name="Test"
        self.operation=0
        self.area_version=0




    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        data["message"] = body.decode('utf-8')
        return data


