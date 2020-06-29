import http.client as ht
conn = ht.HTTPConnection("api.msg91.com")


def Send_SMS(payload,headers):

    conn.request("POST","/api/v2/sendsms?",payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print("SMS sent")

def SMS_Data():
    payload ='''{
    "sender": "BUYMOR",
    "route": "4",
    "country": "91",
    "sms":[
      {
    "message":"A message for testing perpose....testing 1,2,3. ",
    "to":["9911179884","8971287208"]
      }
     ]
    }
    '''
    headers={
        'authkey':"192268ArIqtNQVr5a548512",
        'content-type':"application/json"
    }
    Send_SMS(payload, headers)

print(SMS_Data())

