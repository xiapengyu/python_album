from django.http import HttpResponse, JsonResponse
from polls.models import User


def add_user(request):
    user = User(100, 'Xiapengyu', 30, 'PM', '17688556401')
    user.save()
    return HttpResponse('添加用户成功')


def praise_or_criticize(request):
    """好评"""
    try:
        tno = int(request.GET.get('tno'))
        teacher = User.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        data = {'code': 20000, 'msg': '操作成功', 'count': count}
    except (ValueError, User.DoseNotExist):
        data = {'code': 20001, 'msg': '操作失败'}
    return JsonResponse(data)
