import requests,json
from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
# result=requests.get('https://tsmcbot-404notfound.du.r.appspot.com/api/myehr').content
# print(result)


url='https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'


payload = {'Host': 'login.microsoftonline.com',
    "Content-Type": "application/x-www-form-urlencoded",
    'grant_type':'client_credentials',
    'client_id':'30eba4f2-6e15-458b-9fdf-f8bbf25efb4f',
    'client_secret':'ElizaHuangTaigidian2021',
    'scope':'https://api.botframework.com/.default'}
# Host: login.microsoftonline.com
# Content-Type: application/x-www-form-urlencoded

# grant_type=client_credentials&client_id=MICROSOFT-APP-ID&client_secret=MICROSOFT-APP-PASSWORD&scope=https%3A%2F%2Fapi.botframework.com%2F.default
headers = {}# 
r = requests.post(url, data=(payload), headers=headers)# data=json.dumps(payload)
response=json.loads(r.content.decode('utf-8'))
print('access_token response:\n',response)
access_token=response['access_token']

# url='https://api.botframework.com'#https://smba.trafficmanager.net/apis/v3/conversations/12345/activities
# header={'Authorization': 'Bearer ' + access_token}
# response2=json.loads(r.content.decode('utf-8'))
# print('JWT token response:\n',response2)


# conversationId='29:1htJmKwuNtPEggpMm5kJ73ht47oIbddUOeEh1r1DFpf7vJmh83_C7Q3sBnFcxS3EJv5hHqcu0Po3_-dMmfqnMfA'
conversationId='29:1lNWDIz8Jn0YgoFx8LTJWrkqchAJb1Vg0bJK-PvHxe2FHzNXzFHYaeA0P9j58qQyPVVUCKUfpbZlBNcepHMaajg'
header={'Authorization': 'Bearer ' + access_token, 'content-type':'application/json'}
url=f'https://smba.trafficmanager.net/apac/v3/conversations'
payload={
    "bot": {
        "id": "30eba4f2-6e15-458b-9fdf-f8bbf25efb4f",
        "name": "AzureBot001_Regis"
    },
    "isGroup": False,
    "members": [
        {
            "id": "010281b3-d5d6-4bc8-b561-bf4794b97036",#010281b3-d5d6-4bc8-b561-bf4794b97036
            "name": "黃懿"
        }
    ],
    "topicName": "Testing proactive msg"
}
r = requests.post(url,json=(payload), headers=headers)
response2=json.loads(r.content.decode('utf-8'))
print('conversationId:\n',response2)

# url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversationId)
# MessageFactory.text(
#                         "Welcome to CardBot. "
#                         + "This bot will show you different types of Rich Cards. "
#                         + "Please type anything to get started."
#                     )
# r = requests.post(url, data=(payload), headers=headers)
# response3=json.loads(r.content.decode('utf-8'))


testCard={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
         {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "00",
                    "value": "00"
                },
                {
                    "title": "01",
                    "value": "01"
                },
                {
                    "title": "02",
                    "value": "02"
                },
                {
                    "title": "03",
                    "value": "03"
                },
                {
                    "title": "04",
                    "value": "04"
                },
                {
                    "title": "05",
                    "value": "05"
                },
                {
                    "title": "06",
                    "value": "06"
                },
                {
                    "title": "07",
                    "value": "07"
                },
                {
                    "title": "08",
                    "value": "08"
                },
                {
                    "title": "09",
                    "value": "09"
                },
                {
                    "title": "10",
                    "value": "10"
                },
                {
                    "title": "11",
                    "value": "11"
                },
                {
                    "title": "12",
                    "value": "12"
                },
                {
                    "title": "13",
                    "value": "13"
                },
                {
                    "title": "14",
                    "value": "14"
                },
                {
                    "title": "15",
                    "value": "15"
                },
                {
                    "title": "16",
                    "value": "16"
                },
                {
                    "title": "17",
                    "value": "17"
                },
                {
                    "title": "18",
                    "value": "18"
                },
                {
                    "title": "19",
                    "value": "19"
                },
                {
                    "title": "20",
                    "value": "20"
                },
                {
                    "title": "21",
                    "value": "21"
                },
                {
                    "title": "22",
                    "value": "22"
                },
                {
                    "title": "23",
                    "value": "23"
                }
            ],
            "placeholder": "請選擇 hr (24小時制)",
            "id": "start_time_hour"
        }, 
    ]
}