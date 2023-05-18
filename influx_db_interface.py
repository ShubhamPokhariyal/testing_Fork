import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "p6iddglXeQAwojxiZZoMLCOt_B-YSXeWfu6JldGIyva6lPDIDCruK2lgPcE7WLRSwRNbERuvxsd-0uqNj8nRuw=="
org = "RKGIT"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="Timeseries"
write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(12):
    point = (Point("measurement1").tag("tagname1", "tagvalue1").field("field1", value))
    a=write_api.write(bucket=bucket, org="RKGIT", record=point)
    print(point)
    time.sleep(1)


query_api = write_client.query_api()

query = """from(bucket: "Timeseries")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="RKGIT")

for table in tables:
  for record in table.records:
    print(record)

query_api = write_client.query_api()

query = """from(bucket: "Timeseries")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="RKGIT")

for table in tables:
    for record in table.records:
        print(record)
