from opensearchpy import OpenSearch
import os
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


with open(filename, "r") as f:
    data = f.readlines()

    for i in range(len(data)):
        res = json.loads(data[i])

        # add datetime field to each entry in GMT (now - 3 hours)
        gmt = datetime.datetime.now() - datetime.timedelta(hours=3)
        res["datetime"] = gmt

        # print(res)
        es.index(index=indexname, body=res)


es.close()
