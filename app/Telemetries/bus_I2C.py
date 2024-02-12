from telemetry_interface import TelemetryInterface


busStatus_enum={
  0:"OFF",
  1:"Nominal",
  2:"Error Bus 1",
  3:"Secundary Bus"
}


class busI2c(TelemetryInterface):
    def __init__(self):
        self.name="Bus I2C"
        self.operation=11
        self.area_version=0



    def parseData(self,body):
        "Parse the output argument, where the response is a byte sequence, and return a dictionary."
        data={}
        status_int = int.from_bytes(body, byteorder='little')
        data["Status I2C Bus"]=busStatus_enum[status_int]
        return data

