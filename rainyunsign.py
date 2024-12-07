import json
import os
import http.client

rtokens = json.loads(os.getenv('rtokens'))

for token in rtokens:
    conn = http.client.HTTPSConnection("api.v2.rainyun.com")
    payload = json.dumps({
    "task_name": "每日签到"
    })
    headers = {
    'x-api-key': token,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/user/reward/tasks", payload, headers)
    res = conn.getresponse()
