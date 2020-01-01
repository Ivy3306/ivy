# coding=utf8
import requests,json

import time

curTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))

payload  = {
    'action':'add_course',
    'data':f'{{"name":"初学{curTime}","desc":"初中化学课程","display_idx":"1"}}'
}

response = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload)

r = response.json()
print(r)



