from django.shortcuts import render
from sms_ir import SmsIr
sms_ir = SmsIr(
    api_key,
    linenumber,
)
sms_ir.send_verify_code(
    number="+9830007487129352",
    template_id=471084,
    parameters=[
        {
            "name" : "code",
            "value": 12345,
        },
    ],
)