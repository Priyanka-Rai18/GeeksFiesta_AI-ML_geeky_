import requests

url = 'http://127.0.0.1:5000/'
r = requests.post(url,json={'Year':2016, 'Month':2, 'Day':4,'Hour':6 ,'Temperature':20.2,'Pressure':1234,'Wind_direction':SE,'Wind_speed':2.5})

print(r.json())