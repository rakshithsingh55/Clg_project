from django.shortcuts import render
from django.http import HttpResponse, request
#from .models import user
from django.db.models import Avg
from .models import dataset
from .models import user
import xlrd
from .tfidf import TFIDF
from .CosineSimilarity import CosineSimilarity


# Create your views here.
def home(request):
	return render(request, 'index.html')
# Create your views here.
def alogin(request):
	return render(request, 'admin.html')
def adminlogindef(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')

def adminhomedef(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
		return render(request, 'admin_home.html')

	else:
		return render(request, 'admin.html')
def adminlogoutdef(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')	
	
def uploaddataset(request):
	if "adminid" in request.session:
		

		return render(request, 'upload.html')

	else:
		return render(request, 'admin.html')
		

def xlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="E:\\"+file
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		dataset.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			f5 = sheet.cell(r, 5).value
			f6 = sheet.cell(r, 6).value
			f7 = sheet.cell(r, 7).value
			f8 = sheet.cell(r, 8).value
			f9 = sheet.cell(r, 9).value
			f10 = sheet.cell(r, 10).value
			f11 = sheet.cell(r, 11).value
			f12 = sheet.cell(r, 12).value
			f13 = sheet.cell(r, 13).value
			f14 = sheet.cell(r, 14).value
			f15 = sheet.cell(r, 15).value
			f16 = sheet.cell(r, 16).value
			ing=f4+" "+f5+" "+f6+" "+f7+" "+f8+" "+f9+" "+f10+" "+f11+" "+f12+" "+f13+" "+f14+" "+f15+" "+f16
			print(ing)
			d=dataset(name=f0,url=f1,description=f2,author=f3,ingredients=ing)
			d.save()
		return render(request, 'upload.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')


def viewdataset(request):
	if "adminid" in request.session:
		data=dataset.objects.all()
		return render(request, 'viewdataset.html',{'data':data})
		
	else:
		return render(request, 'admin.html')


def userreg(request):
	return render(request, 'signup.html')
def signupaction(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=user.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'signup.html',{'msg':"Email Already Registered"})
	else:
		d=user(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})


def slogin(request):
	return render(request, 'user.html')
	
def loginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=user.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=user.objects.filter(email__exact=uid)
			request.session['email']=uid
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'student.html')
def slogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')
def shome(request):
	if "email" in request.session:
		email=request.session["email"]
		d=user.objects.filter(email__exact=email)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return redirect('slogout')

def search(request):
	if "email" in request.session:
		return render(request, 'search.html')

	else:
		return render(request, 'user.html')


def searchfood(request):
	keys=request.POST['keys']
	request.session['keys']=keys
	data=dataset.objects.all()

	d={}
	
	for d1 in data:
		sc=TFIDF.process(d1.ingredients,keys)
		print(d1.name,'----------------->',sc)
		d[d1.name]=sc

	L=sorted(d, key=d.get, reverse=True)
	L=L[0:10]
	print
	data=dataset.objects.filter(name__in=L)
	print(data)
	
	return render(request, 'searchresults.html',{'data':data})

def viewfood(request,name):
	name=name.strip()
	data=dataset.objects.filter(name__exact=name)
	
	return render(request, 'viewfood.html',{'data':data})

def viewfood2(request,name):
	name=name.strip()
	data=dataset.objects.filter(name__exact=name)
	
	return render(request, 'viewfood2.html',{'data':data})


def recommendationas(request):
	fname=request.POST['name']
	ing=request.POST['ing']
	data=dataset.objects.exclude(name=fname)
	d={}
	
	for d1 in data:
		sc=CosineSimilarity.process(d1.ingredients,ing)

		print(d1.name,'++++++++++++++++>',sc)
		d[d1.name]=sc

	L=sorted(d, key=d.get, reverse=True)
	L=L[0:5]
	print
	data=dataset.objects.filter(name__in=L)
	print(data)
	
	return render(request, 'recresults.html',{'data':data})
