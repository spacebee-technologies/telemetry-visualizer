from telemetry_interface import TelemetryInterface
import struct


class accelerometer(TelemetryInterface):
    def __init__(self):
        self.name="Accelerometer"
        self.operation=3
        self.area_version=0




    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        x_byte=body[:4]
        y_byte=body[4:8]
        z_byte=body[8:12]
        x= struct.unpack('<f', x_byte)[0]
        y= struct.unpack('<f', y_byte)[0]
        z= struct.unpack('<f', z_byte)[0]
        data["x"]=x
        data["y"]=y
        data["z"]=z
        return data


