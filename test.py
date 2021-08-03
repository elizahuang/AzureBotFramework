import requests,json
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


# conversationId=
# url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversationId)
header={'Authorization': 'Bearer ' + access_token}
response2=json.loads(r.content.decode('utf-8'))