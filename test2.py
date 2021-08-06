import requests,datetime,json

testdate= datetime.datetime(2021, 8, 6, 2, 0)
testData=json.dumps({"test":"123","todo":{"date":"123"}})

requests.post('https://azure-bot-framework.herokuapp.com/api/v1/cron-messages',data=testData)