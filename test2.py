import requests,datetime

testdate=datetime.datetime.now()
testData={"test":"123","todo":{"date":testdate}}

requests.post('https://azure-bot-framework.herokuapp.com/api/v1/cron-messages',json=testData)