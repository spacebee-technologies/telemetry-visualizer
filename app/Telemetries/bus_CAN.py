from telemetry_interface import TelemetryInterface


busStatus_enum={
  0:"OFF",
  1:"Nominal",
  2:"Error Bus 1",
  3:"Secundary Bus"
}


class busCAN(TelemetryInterface):
    def __init__(self):
        self.name="Bus CAN"
        self.operation=12
        self.area_version=0



    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        status_int = int.from_bytes(body, byteorder='little')
        data["Status CAN Bus"]=busStatus_enum[status_int]
        return data

