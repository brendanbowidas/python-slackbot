import urllib2, base64, ast, json, re
from pprint import pprint as pp
from log_time import make_request



def process_message(data):
    channel = data['channel']
    if 'log' and 'hours' in data['text'].lower():
        #outputs.append([channel, projects])
        num = re.findall('\d+', data['text'])
        for i in num:
            outputs.append([channel, 'Time logged sucessfully']) if make_request({'hours': i , 'description': 'test' }) else outputs.append([channel, 'Something went wrong'])

    #    outputs.append([channel, ])
