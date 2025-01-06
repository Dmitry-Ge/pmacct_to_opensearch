from opensearchpy import OpenSearch
import os
import json
import datetime


indexname = "pmacct-" + datetime.datetime.now().strftime("%Y-%m-%d")
gmt = datetime.datetime.now() - datetime.timedelta(hours=3)

es = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

data = []
for line in sys.stdin:
    data.append(line)


for line in data:
    res = json.loads(line)
    res["datetime"] = gmt

    try:
        es.index(index=indexname, body=res)
    except Exception as e:
        print(f"Error: {e} in line: {line}")

es.close()
