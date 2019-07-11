import json
import traceback

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from diary.models import Diary


@csrf_exempt
def create(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    if not {'user_id','title','label','content'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': json.dumps(request.POST.dict())}))
    try:
        params = request.POST.dict()
        dis=Diary.objects.create(**params)
        res['data']['id']=dis.id
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
        res['data']['count']=Diary.objects.filter(**params).count()
        res['data']['diary']=[]
        qset=Diary.objects.filter(**params).order_by('-ctime')[page*size:(page+1)*size]
        diaries=json.loads(serializers.serialize("json", qset))

        for diary in diaries:
            data_row=diary['fields']
            data_row['id']=diary['pk']
            data_row['images']=json.loads(data_row['images'])
            data_row['ctime']=data_row['ctime'].replace('T',' ')[:-4]
            data_row['mtime'] = data_row['mtime'].replace('T',' ')[:-4]
            del data_row['status']
            res['data']['diary'].append(data_row)
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id','update'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Diary.objects.filter(id=request.POST['id']).update(**json.loads(request.POST['update']))
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))


@csrf_exempt
def delete(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Diary.objects.filter(id=request.POST['id']).update(status=0)
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({'code': -2, 'msg': 'error-2', 'data': []}))
    return HttpResponse(json.dumps(res))