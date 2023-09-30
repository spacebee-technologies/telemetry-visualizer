from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


class DB_Interface:
    def __init__(self,ip):
        # You can generate a Token from the "Tokens Tab" in the UI
        self.token = "BpQbQsV9kvCb7zRVwuoPyyyN-Feb9PQOvBGvPuU0vNSul5tJ4NXoAGHynet4dpzyn36njgMqXmPVPQpzs67eRA=="
        self.org = "Spacebee"
        self.bucket = "TITO_dev"
        self.port=8086
        self.client = InfluxDBClient(url="http://localhost:8086", token=self.token,org=self.org)


    def writeData(self,telemetry):
        data = [
            {
                "measurement": telemetry.name,
                "tags": {
                    "TM_ID": telemetry.operation
                },
                "time":datetime.utcnow(),
                "fields": {
                    "timestamp":telemetry.timestamp,
                }
            }
        ]
        data[0]["fields"].update(telemetry.data)
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=self.bucket, record=data)

        print("------------------------")
        print("Finish")