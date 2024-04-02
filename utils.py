from kavenegar import *

def otpcode_sender(phone_number,code):
    try:
        api = KavenegarAPI('6B37594171514648706D444A31464E652F534562366A4B474C564172322F686D776967686C6335326C634D3D')
        params = {
            'sender':10008663,
            'receptor' : phone_number ,
            'message': code
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)