import io

import xlwt
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls import util
from polls.models import User


def login(request: HttpRequest) -> HttpResponse:
    """用户登录"""
    hint = ''
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username and password:
            password = util.gen_md5_digest(password)
            # user = User.objects.filter(username=username, password=password).first()
            user = User.objects.filter(user_name=username).first()
            if user:
                # request.session['userid'] = user.no
                # request.session['username'] = user.username
                request.session['userid'] = user.id
                request.session['username'] = user.user_name
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return HttpResponse(hint)


def add_user(request):
    user = User(100, 'Xiapengyu', 30, 'PM', '17688556401')
    user.save()
    return HttpResponse('添加用户成功')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


@api_view(('GET',))
def query_user(request: HttpRequest) -> HttpResponse:
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    data = serializer.data
    for item in queryset:
        print(str(item))
    res = {'code': 20000, 'msg': '操作成功', 'data': data}
    return Response(res)


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


def export_user(request):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('用户信息表')
    queryset = User.objects.all()
    columns = ('姓名', '年龄', '职业', '手机')
    for index, name in enumerate(columns):
        sheet.write(0, index, name)

    props = ('user_name', 'age', 'job', 'phone')
    for row, user in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(user, prop, '')
            sheet.write(row + 1, col, value)
    # 保存Excel
    buffer = io.BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename = 'user.xls'
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    response['content-disposition'] = f'attachment; filename*=user.xls'
    return response
