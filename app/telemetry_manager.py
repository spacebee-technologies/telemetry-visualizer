from communication import Communication
from message_manager import MessageManager
from Telemetries import all_telemetries


class TelemetryManager:
    communication = Communication()
    message_manager=MessageManager()
    telemetries = [cls() for cls in all_telemetries]

    def getTelemetry(self,id):
        "Retrieve the telemetry using its telemetry ID."
        for telemetry in self.telemetries:
            if telemetry.getOperationNumber() == id:
                return telemetry
        return id

    def receiveTelemetries(self):
        pack_data=self.communication.receive()
        unpack_data=self.message_manager.unpack(pack_data)
        telemetry=self.getTelemetry(unpack_data['operation_id'])
        data=telemetry.parseData(unpack_data['body'])
        telemetry.loadParameters(data,unpack_data['transaction_id'],unpack_data['timestamp'],unpack_data['area_version'])
        return telemetry
    
