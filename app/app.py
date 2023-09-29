from db_interface import DB_Interface
from telemetry_manager import TelemetryManager

TM_manager=TelemetryManager()
database=DB_Interface("192.168.68.63")

while True:
    telemetry=TM_manager.receiveTelemetries()
    print(f"Saving... {telemetry.data}")
    database.writeData(telemetry)
    print("Saved")