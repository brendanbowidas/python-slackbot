import urllib2, base64, json, requests
from datetime import datetime


outputs = []
company = "responsemarketing"
key = "tiger390paper"
my_id = "156874"
action = "time_entries.json"
project_id = "174958"




def make_request(input):
    url = "https://{0}.teamwork.com/projects/{1}/{2}".format(company, project_id, action)
    data = {"time-entry": {'description': input['description'], "person-id": my_id, "hours": input['hours'], "date": "20160222"}}
    headers = {"Authorization": "BASIC " +  base64.b64encode(key + ":xxx"), "Content-type": "application/json"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)

    return True if r.json()['STATUS'] == 'OK' else False
