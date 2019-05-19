import json
import os
import random
import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ConsultantService.settings import BASE_DIR, MEDIA_URL_PREFIX


@csrf_exempt
def uploadImage(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    print(request.POST)
    if request.method == 'POST':
        files = request.FILES.getlist('images', None)  # input 标签中的name值
        print(files)
        if not files:
            res={'code':-1,'msg':"无上传文件", 'data':[]}
        else:
            date=time.strftime('%Y%m%d',time.localtime())
            url_mid = '/media/images/'+date+'/'
            dirs = BASE_DIR + url_mid
            folder = os.path.exists(dirs)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(dirs)  # makedirs 创建文件时如果路径不存在会创建这个路径
            try:
                for file in files:
                    suffix = os.path.splitext(file.name)[1]
                    fname = "avatar_%s_%06d%s"%(str(int(round(time.time() * 1000))), random.randint(0,100000), suffix)
                    path = dirs + fname
                    f = open(path,'wb')
                    for line in file.chunks():
                        f.write(line)
                    f.close()
                    res['data'].append(MEDIA_URL_PREFIX+url_mid+fname)
            except Exception as e:
                res['code']=-2
                res['msg']=e
    return HttpResponse(json.dumps(res))

@csrf_exempt
def uploadAvatar(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    print(request.POST)
    if request.method == 'POST':
        files = request.FILES.getlist('images', None)  # input 标签中的name值
        print(files)
        if not files:
            res={'code':-1,'msg':"无上传文件", 'data':[]}
        else:
            t=time.strftime('%Y%m%d%H%M%S',time.localtime())
            url_mid = '/media/avatar/'
            dirs = BASE_DIR + url_mid
            folder = os.path.exists(dirs)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(dirs)  # makedirs 创建文件时如果路径不存在会创建这个路径
            try:
                for file in files:
                    suffix = os.path.splitext(file.name)[1]
                    fname = "avatar_%s_%06d%s"%(t, random.randint(0,100000), suffix)
                    path = dirs + fname
                    f = open(path,'wb')
                    for line in file.chunks():
                        f.write(line)
                    f.close()
                    res['data'].append(MEDIA_URL_PREFIX+url_mid+fname)
            except Exception as e:
                res['code']=-2
                res['msg']=e
    return HttpResponse(json.dumps(res))

@csrf_exempt
def uploadDisImg(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    print(request.POST)
    if request.method == 'POST':
        files = request.FILES.getlist('images', None)  # input 标签中的name值
        print(files)
        if not files:
            res={'code':-1,'msg':"无上传文件", 'data':[]}
        else:
            date=time.strftime('%Y%m%d',time.localtime())
            url_mid = '/media/discussion/'+date+'/'
            dirs = BASE_DIR + url_mid
            folder = os.path.exists(dirs)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(dirs)  # makedirs 创建文件时如果路径不存在会创建这个路径
            try:
                for file in files:
                    suffix = os.path.splitext(file.name)[1]
                    fname = "avatar_%s_%06d%s"%(time.strftime('%Y%m%d%H%M%S',time.localtime()), random.randint(0,100000), suffix)
                    path = dirs + fname
                    f = open(path,'wb')
                    for line in file.chunks():
                        f.write(line)
                    f.close()
                    res['data'].append(MEDIA_URL_PREFIX+url_mid+fname)
                res['data']=json.dumps(res['data'])
            except Exception as e:
                res['code']=-2
                res['msg']=e
    return HttpResponse(json.dumps(res))