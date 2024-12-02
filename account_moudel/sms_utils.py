from kavenegar import *
from account_moudel.models import User
def send_verification_code(phone_number, code):
    try:
        api = KavenegarAPI('356F2F386B49427250374934354B4C4744475A6C4649452B6C6E74762F4D77635A6376612B4E4674586C303D')  # کلید API را جایگزین کنید
        params = {
            'sender': '2000660110',  # در صورت نیاز، شماره ارسال‌کننده را مشخص کنید
            'receptor': phone_number,  # شماره گیرنده
            'message': f'کد تایید شما: {code}',  # متن پیام
        }
        response = api.sms_send(params)
        print(response)  # می‌توانید برای دیباگ استفاده کنید
    except APIException as e:
        print(f"API Exception: {e}")
    except HTTPException as e:
        print(f"HTTP Exception: {e}")