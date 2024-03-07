from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from text_translate import txt_translate, gtxt_translate, new_translator, summarize_text, ppttransform
from img import img_analyze
from django.views.decorators.csrf import csrf_exempt
import json
from texttoaudio import convert_text_to_speech, play_mp3
import requests

@csrf_exempt
def default(request):
    received_json_data=json.loads(request.body)
    text = received_json_data.get('text')
    sitename = received_json_data.get('sitename')
    language = received_json_data.get('language')
    
    if(text==None):
        res = {'flag': 'error', "pattern": "No text param found in request"}
        return JsonResponse(res)
    if(sitename==None):
        res = {'flag': 'error', "pattern": "No sitename param found in request"}
        return JsonResponse(res)
    if(language==None):
        res = {'flag': 'error', "pattern": "No language param found in request"}
        return JsonResponse(res)
    print(text)
    new = new_translator(text)
    print("*****")
    res = {"translated":new}
    
    return JsonResponse(res, status=200)

@csrf_exempt
def imganalyze(request):
    received_json_data=json.loads(request.body)
    
    imgurl = received_json_data.get('imgurl')
    language = received_json_data.get('language')
    
    if(imgurl==None):
        res = {'flag': 'error', "pattern": "No img url param found in request"}
        return JsonResponse(res)
    if(language==None):
        res = {'flag': 'error', "pattern": "No language param found in request"}
        return JsonResponse(res)
    
    new = img_analyze(imgurl)
    res = {"translated":new}
    
    return JsonResponse(res, status=200)

@csrf_exempt
def summarize(request):
    
    received_json_data=json.loads(request.body)
    
    text = received_json_data.get('artical')
    summary = summarize_text(text)
    return JsonResponse({"summary":summary}, status=200)

@csrf_exempt
def tta(request):
    received_json_data=json.loads(request.body)
    text = received_json_data.get('text')
    path = convert_text_to_speech(text)
    play_mp3(path)
    return JsonResponse({"path":"done"}, status=200)

@csrf_exempt
def ppt_convert(request):
    received_json_data=json.loads(request.body)
    text = received_json_data.get('ppturl')
    new=ppttransform(text)

    return JsonResponse({"translatedFileUrl":new}, status=200)