import requests

url = 'http://127.0.0.1:5000/predict_ap'
# r = requests.post(url,json={/'experience':2, /'test_score':9, /'interview_score':6})

# print(r.json())
r = requests.get(url)
try:
    data = r.json()
except ValueError:
    print("Response content is not valid JSON")
