import json

def fetchone(result):
    data = result.fetchone()

    return json.loads(json.dumps(data._asdict(), default=str)) if data else None
