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
print('type: ',type(response))
access_token_dict=response
access_token=response['access_token']

# url='https://api.botframework.com'#https://smba.trafficmanager.net/apis/v3/conversations/12345/activities
# header={'Authorization': 'Bearer ' + access_token}
# response2=json.loads(r.content.decode('utf-8'))
# print('JWT token response:\n',response2)

channel_id='msteams'

'''try to get conversation id'''
# # userId='29:1lNWDIz8Jn0YgoFx8LTJWrkqchAJb1Vg0bJK-PvHxe2FHzNXzFHYaeA0P9j58qQyPVVUCKUfpbZlBNcepHMaajg'
usesrid_office='29:1htJmKwuNtPEggpMm5kJ73ht47oIbddUOeEh1r1DFpf7vJmh83_C7Q3sBnFcxS3EJv5hHqcu0Po3_-dMmfqnMfA'
teams_appid='30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
# header={'Authorization': 'Bearer ' + access_token} #, 'content-type':'application/json'
# url=f'https://smba.trafficmanager.net/apac/v3/conversations'
# payload={
#     "bot": {
#         "id": "30eba4f2-6e15-458b-9fdf-f8bbf25efb4f",#30eba4f2-6e15-458b-9fdf-f8bbf25efb4f
#         "name": "AzureBot001_Regis"
#     },
#     "isGroup": False,
#     "members": [
#         {
#             "id": usesrid_office,
#             "name": "Yi Huang 黃懿"
#         }
#     ],
#     "topicName": "Testing proactive msg"
# }
# r = requests.post(url,json=(payload), headers=header)
# response2=json.loads(r.content.decode('utf-8'))
# print('conversationId:\n',response2)

# url =f'https://graph.microsoft.com/v1.0/appCatalogs/teamsApps?$filter=%s'%(teams_appid)
# header={'Authorization': 'Bearer ' + access_token}
# r = requests.get(url)
# response2=json.loads(r.content)
# print('conversationId:\n',response2)



#userid, teamsappid
url =f'https://graph.microsoft.com/beta/users/%s/teamwork/installedApps?$expand=teamsApp&$filter=teamsApp/%s' %(usesrid_office,teams_appid)
header={'Authorization': 'Bearer ' + access_token}
r = requests.get(url,json=access_token_dict)
response2=json.loads(r.content)
print('conversationId:\n',response2)




# url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversationId)
# MessageFactory.text(
#                         "Welcome to CardBot. "
#                         + "This bot will show you different types of Rich Cards. "
#                         + "Please type anything to get started."
#                     )
# r = requests.post(url, data=(payload), headers=headers)
# response3=json.loads(r.content.decode('utf-8'))


