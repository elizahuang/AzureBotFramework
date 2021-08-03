import requests,json
result=requests.get('https://tsmcbot-404notfound.du.r.appspot.com/api/myehr').content
print(result)