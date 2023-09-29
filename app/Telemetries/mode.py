from telemetry_interface import TelemetryInterface
import struct

mode_enum={
  0:"OFF",
  1:"MANUAL",
  3:"AUTO"
}


class mode(TelemetryInterface):
    def __init__(self):
        self.name="Mode"
        self.operation=1
        self.area_version=0



    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        mode_int = int.from_bytes(body, byteorder='little')
        data["Mode"]=mode_enum[mode_int]
        return data

