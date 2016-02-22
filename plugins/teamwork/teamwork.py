import urllib2, base64, ast, json

outputs = []
company = "responsemarketing"
key = "tiger390paper"
action = "projects.json"

request = urllib2.Request("https://{0}.teamwork.com/{1}".format(company, action))
request.add_header("Authorization", "BASIC " + base64.b64encode(key + ":xxx"))

response = urllib2.urlopen(request)


projects = json.loads(response.read())
project_names = {k:v for (k,v) in projects.items() if "name" in k}

def process_message(data):
    channel = data['channel']
    if 'show teamwork projects' in data['text'].lower():
        #outputs.append([channel, projects])
        print(projects)
