from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,AudioSendMessage,VideoSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event): #send text
    try:
        message = TextSendMessage(
                text = "您好~~~我是chatbot_servicer"
        )
        line_bot_api.reply_message(event.reply_token,message)
        
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        
def sendImage(event): #傳送照片
    try:
        message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/OQBFjKK.jpg",
                preview_image_url = "https://i.imgur.com/OQBFjKK.jpg"
               
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

def sendStick(event): #傳送貼圖
    try:
        message = StickerSendMessage(
                package_id = '1',
                sticker_id = '2'
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤!"))
        
def sendMulti(event): #多項傳送
    try:
        message = [ #list
                StickerSendMessage( #send sticks
                        package_id = '1',
                        sticker_id = '2'
                ),
                TextSendMessage( #send y texts
                        text = "This is anime pic"
                ),
                ImageSendMessage( #send pics
                        original_content_url = "https://i.imgur.com/OQBFjKK.jpg",
                        preview_image_url = "https://i.imgur.com/OQBFjKK.jpg"
                        )
                ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤!"))
        
def sendPosition(event): #傳送位置
    try:
        message = LocationSendMessage(
                title = '101大樓',
                address = '台北市信義路五段７號',
                latitude = 25.034207,
                longitude = 121.564590
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤!"))
        
def sendQuickreply(event): #快速選單
    try:
        message = TextSendMessage(
                text = '選擇你喜歡的角色',
                quick_reply = QuickReply(
                        items = [
                                QuickReplyButton(
                                        action = MessageAction(label='Yukina',text='Yukina')
                                ),
                                QuickReplyButton(
                                        action = MessageAction(label='Ringo',text='Ringo')
                                ),
                                QuickReplyButton(
                                        action = MessageAction(label='Saten Ruiko',text='Saten Ruiko')
                                ),
                                QuickReplyButton(
                                        action = MessageAction(label='RFB',text='RFB')
                                ),
            
                                ]
                        )
                ) 
      
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤!"))
    
baseurl = 'https://da394f357879.ngrok.io/static/'
    
def sendVoice(event):
    try:
        message = AudioSendMessage(
                original_content_url = baseurl + 'Black_bullet-op.mp3',
                duration = 100000
       )
        line_bot_api.reply_message(event.reply_token,message)
        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤!"))
        
def sendVideo(event):
    try:
        message = VideoSendMessage(
                original_content_url = baseurl + 'MyVideo_1.mp4' ,
                preview_image_url = baseurl + 'videopic.jpg'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
          line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤!"))
    
        
        

