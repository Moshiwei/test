import itchat
import requests

KEY = '996461c7ff954ce0be78132aa276e75d'

def get_response(msg):
    apiURL = 'http://www.tuling123.com/openapi/api'
    data = {
        'key':KEY,
        'info':msg,
        'useid':'Mirror',
    }
    try:
        r = requests.post(apiURL, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received:'+msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

# itchat.auto_login(hotReload=True)
# itchat.run()
itchat.logout()
