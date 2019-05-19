import json
import traceback

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from discussion.models import Discussion
from user.models import User


@csrf_exempt
def create(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    if not {'user_id','content'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        params = request.POST.dict()
        dis=Discussion.objects.create(**params)
        res['data']['discussion_id']=dis.id
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'discussion_id','update'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Discussion.objects.filter(id=request.POST['discussion_id']).update(**json.loads(request.POST['update']))
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def delete(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'discussion_id'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Discussion.objects.filter(id=request.POST['discussion_id']).update(status=0)
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def list(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    try:
        params = request.POST.dict()
        page=0
        size=20
        if 'page' in params:
            page=params['page']
            params.pop('page')
        if 'size' in params:
            size=params['size']
            params.pop('size')
        params['status']=1
        res['data']['count']=Discussion.objects.filter(**params).count()
        res['data']['discussion']=[]
        qset=Discussion.objects.filter(**params).order_by('-ctime')[page*size:(page+1)*size]
        dynamics=json.loads(serializers.serialize("json", qset))
        print(dynamics)
        for dynamic in dynamics:
            data_row=dynamic['fields']
            data_row['dynamic_id']=dynamic['pk']
            data_row['images']=json.loads(data_row['images'])
            data_row['user_info'] = json.loads(serializers.serialize("json", User.objects.filter(id=dynamic['fields']['user_id'])))[0]['fields']
            data_row['user_info'].pop('password')
            # data_row['user_info'].pop('status')
            # data_row['user_info'].pop('ctime')
            data_row['user_info'].pop('mtime')
            res['data']['discussion'].append(data_row)
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))