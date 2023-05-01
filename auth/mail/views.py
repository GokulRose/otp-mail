from django.shortcuts import render
from auth import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import random
import array
import time
def mail(request):
	MAX_LEN = 9
	DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
	COMBINED_LIST = DIGITS
	rand_digit = random.choice(DIGITS)
	temp_pass = rand_digit
	for x in range(MAX_LEN - 4):
	    temp_pass = temp_pass + random.choice(COMBINED_LIST)
	    temp_pass_list = array.array('u', temp_pass)
	    random.shuffle(temp_pass_list)
	    password = ""
	for x in temp_pass_list:
	    password = password + x
	    lol=password
	    with open("deeznuts.txt","w")as f:
	    	print(lol,file=f)
	subject = "Greetings"
	msg     = "Your OTP to login into server is "
	lol =msg+password
	to      = "to  email"
	res     = send_mail(subject,lol, settings.EMAIL_HOST_USER,[to])
	if(res == 1):
		return render(request,'index.html')
	else:
		return HttpResponse("OTP could not sent")

def login(request):
	if request.method=='POST':
		str2=request.POST['otp']
		lel=str2
		with open("deez.txt","w")as f:
			print(lel,file=f)
		fileptr=open('deeznuts.txt', 'r')
		nope=open('deez.txt','r')
		pas1=fileptr.read()
		pas2=nope.read()
		print(pas1)
		print(pas2)
		if pas1==pas2:
			return HttpResponse("logged in Successfully")
		else:
			return HttpResponse("OTP mismatch")
	else:
		return render(request,'index.html')