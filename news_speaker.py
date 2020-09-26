from win32com.client import Dispatch
import requests
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
secret = str(input("enter your API key"))
url = str(input("enter URL from platform(NEWSAPI) to get headlines"))
n = int(input("enter a number of lines that you want to hear"))
k=0

# Specify the query and number of returns
parameters = {
    'q': 'big data', # query phrase
    'pageSize':n,  # maximum is 100
    'apiKey': secret # your own API key
}


response = requests.get(url, params=parameters)

# Convert the response to JSON format and pretty print it
response_json = response.json()
# pprint.pprint(response_json)
for i in response_json['articles']:
    l=i['title']
    print(l)
    if(k==0):
        speak(l)
        k+=1
    elif(k<n):
        speak("next line is ")
        speak(l)
        k+=1
    else:
        speak(l)
        k+=1






