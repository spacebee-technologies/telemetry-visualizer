from telemetry_interface import TelemetryInterface
import struct


class tempPdu(TelemetryInterface):
    def __init__(self):
        self.name="Temperature PDU [°C]"
        self.help=""
        self.operation=14
        self.area_version=0


    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        temp= struct.unpack('<f', body)[0]
        data["Temperature"]=temp
        return data
