from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent,TextMessage
from module import func
# Create your views here.

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(requests):
    if requests.method == 'POST':
        signature = requests.META['HTTP_X_LINE_SIGNATURE']
        body = requests.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        
        for event in events:
            if isinstance(event, MessageEvent):
                mtext = event.message.text
              
                if mtext == '請問你是誰？':
                    func.sendText(event)
                    
                elif mtext == '請給我圖片':
                    func.sendImage(event)
                    
                     
                elif mtext == '傳送貼圖給我':
                    func.sendStick(event)
                
                elif mtext == '多項傳送':
                    func.sendMulti(event)
                    
                elif mtext == '問我一個問題':
                    func.sendQuickreply(event)
                    
                elif mtext == '傳送位置':
                    func.sendPosition(event)
                
                elif mtext == '傳送聲音':
                    func.sendVoice(event)
                    
                elif mtext == '傳送影片':
                    func.sendVideo(event)
        return HttpResponse()
    
    else:
        return HttpResponseBadRequest()
    