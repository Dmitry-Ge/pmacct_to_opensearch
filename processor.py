from opensearchpy import OpenSearch
import os
import sys
import json
import datetime

filename = os.path.join(os.path.dirname(__file__), "pmacct.json")
indexname = "pmacct-" + datetime.datetime.now().strftime("%Y-%m-%d")

es = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
)

# will be get lines of jsons from stdin
data = []
gmt = datetime.datetime.now() - datetime.timedelta(hours=3)

for line in sys.stdin:
    # print(line)
    data.append(line)


for line in data:
    try:
        es.index(index=indexname, body={**json.loads(line), "datetime": gmt})
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error: {e} in line: {line}")

es.close()
