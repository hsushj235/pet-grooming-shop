from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Contract
import json

# Create your views here.
@csrf_exempt
def api_submit_booking(request):
    """在线预约提交接口"""
    if request.method != 'POST':
        return JsonResponse({'code': 405, 'msg': '仅支持 POST 请求'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'code': 400, 'msg': '请求体格式错误'}, status=400)

    pet_name = data.get('petName', '').strip()
    pet_type = data.get('petType', 'dog')
    breed = data.get('breed', '').strip()
    weight = data.get('weight', '')
    service = data.get('service', '').strip()
    date = data.get('date', '').strip()
    time = data.get('time', '').strip()
    phone = data.get('phone', '').strip()
    remark = data.get('remark', '').strip()

    # 基础校验
    errors = []
    if not pet_name:
        errors.append('请输入宠物姓名')
    if not service:
        errors.append('请选择服务项目')
    if not date:
        errors.append('请选择预约日期')
    if not time:
        errors.append('请选择预约时段')
    if not phone:
        errors.append('请输入主人手机号')

    if errors:
        return JsonResponse({'code': 400, 'msg': '；'.join(errors)}, status=400)

    # 体重转 Decimal
    from decimal import Decimal, InvalidOperation
    weight_val = None
    if weight:
        try:
            weight_val = Decimal(weight)
        except InvalidOperation:
            pass

    contract = Contract.objects.create(
        pet_name=pet_name,
        pet_type=pet_type,
        breed=breed,
        weight=weight_val,
        service=service,
        date=date,
        time=time,
        phone=phone,
        remark=remark,
    )

    return JsonResponse({
        'code': 200,
        'msg': '预约成功！我们将短信通知您确认信息。',
        'data': {
            'id': contract.id,
            'pet_name': contract.pet_name,
            'service': contract.service,
            'date': str(contract.date),
            'time': contract.time,
        }
    })

@csrf_exempt
def api_list_bookings(request):
    """获取所有预约记录（用于后台管理）"""
    bookings = Contract.objects.all().order_by('-created_at')
    result = [{
        'id': b.id,
        'pet_name': b.pet_name,
        'pet_type': b.pet_type,
        'breed': b.breed,
        'weight': float(b.weight) if b.weight else None,
        'service': b.service,
        'date': str(b.date),
        'time': b.time,
        'phone': b.phone,
        'remark': b.remark,
        'created_at': b.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    } for b in bookings]
    return JsonResponse({'code': 200, 'data': result})
