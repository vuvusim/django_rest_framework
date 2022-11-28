import requests

reqUrl = "http://127.0.0.1:8000/movies"

headersList = {
 "Accept": "*/*",
 "User-Agent": "CodeAcademy API Test App" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)