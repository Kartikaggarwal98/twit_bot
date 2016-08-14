from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import time
import os
from django.conf import settings
from random import shuffle
from search.models import Pokedex
# Create your views here.



def srch3(request,foo):
	#search_string=digit or 2
	search_string=str(foo) or 1
	print search_string
	list_dir=os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	result_arr=[]
	search_string=str(search_string)

	for file_name in list_dir:

		if search_string in file_name:
			result_arr.append(file_name)


	context_dict={}
	context_dict['list_dir']=list_dir

	context_dict['search_string']=search_string

	context_dict['result_arr']=result_arr
	return render(request,'search/search.html',context_dict)

def srch2(request,digit):
	search_string=digit or '1'
	print search_string
	list_dir=os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	result_arr=[]
	search_string=str(search_string)

	for file_name in list_dir:

		if search_string in file_name:
			result_arr.append(file_name)


	context_dict={}
	context_dict['list_dir']=list_dir

	context_dict['search_string']=search_string

	context_dict['result_arr']=result_arr
	return render(request,'search/search.html',context_dict)

def srch(request):
	search_string=request.GET.get("text")


	list_dir=os.listdir(os.path.join(settings.STATIC_PATH,'images'))

	result_arr=[]

	for file_name in list_dir:
		if search_string in file_name:
			result_arr.append(file_name)


	context_dict={}
	context_dict['list_dir']=list_dir

	context_dict['search_string']=search_string

	context_dict['result_arr']=result_arr

	return render(request,'search/search.html',context_dict)


def index(request):
	
	today_date=time.ctime()
	context_dict={'boldmessage':"I am bold from the context"}
	#context_dict['a']=a
	context_dict['date']=today_date
	list_dir=os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	shuffle(list_dir)
	context_dict['list_dir']=list_dir

	context_dict['pokedex']=Pokedex.objects.all()
	return render(request,'search/index.html',context_dict)
	#return HttpResponse('Hello world')

def random(request):
	list_dir=os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	shuffle(list_dir)
	context_dict['list_dir']=list_dir
	return render(request,'search/index.html',context_dict)