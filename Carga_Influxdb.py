from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json

# You can generate a Token from the "Tokens Tab" in the UI
token = "3k6YbRuuGzJww_J4AYOmEB2zYzWUuIAdeLKt_bFkRmu9UyZWRf696v0uIXDilgad5M3yX3Jxo00m0RONdxcdKA=="
org = "Spacebee"
bucket = "TITO_dev"

client = InfluxDBClient(url="http://192.168.1.10:8086", token=token, org=org)

data = [
    {
        "measurement": "Battery",
        "tags": {
            "TM_ID": "32"
        },
        "time": "2023-08-16T10:00:00Z",
        "fields": {
            "Estado": "Ok",
            "Porcentaje": 11.98
        }
    },{
        "measurement": "Maquina_de_estado",
        "tags": {
            "TM_ID": "20"
        },
        "time": "2023-08-16T10:00:00Z",
        "fields": {
            "Estado": "Mov"
        }
    }
]

write_api = client.write_api(write_options=SYNCHRONOUS)
write_api.write(bucket=bucket, record=data)

client.close()
