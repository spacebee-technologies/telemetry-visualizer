from telemetry_interface import TelemetryInterface
import struct

profile_enum={
    0: "NOTHING",
    1: "HOME",
    2: "SET_HEIGHT",
    3: "STAND",
    4: "PHASE_OUT",
    5: "FORWARD",
    6: "PHASE_IN",
    7: "RE_STAND",
    8: "TURN"
}

class profile(TelemetryInterface):
    def __init__(self):
        self.name="Profile"
        self.operation=4
        self.area_version=0



    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        profile_int = int.from_bytes(body, byteorder='little')
        data["Profile"]=profile_enum[profile_int]
        return data

