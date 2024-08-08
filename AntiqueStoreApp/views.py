from django.shortcuts import render,redirect
from . forms import UserForm,AntiqueItemForm,AuctionItemForm
from . models import User,AntiqueItem,Auction
from django.core.mail import send_mail
from vintage_treasures import settings
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def homeView(request):
	k = AntiqueItem.objects.filter(usitem_id=request.user.id)
	h=Auction.objects.filter(winner_id=request.user.id)
	f = AntiqueItem.objects.all()
	g = Auction.objects.all()
	cdt = {}
	jdt={}
	for j in f:
		cdt[j.id]=j.name	
		if j.usitem_id in cdt:
			cdt[j.id]=j.name,j.TagLine,j.description,j.image,j.startingprice,j.maximumprice,j.itemtype,cdt[j.usitem_id]
	for l in g:
		jdt[l.winner_id]=l.item
		if l.winner_id in jdt:
			jdt[l.id]=l.item,l.start_time,l.end_time,l.bid_amount,l.highest_bid,l.winner_name,jdt[l.winner_id]
	return render(request,'html/home.html',{'rj':k,'bj':h,'uj':cdt.values(),'kj':jdt.values()})

def signupView(request):
	if request.method=="POST":
		g=UserForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/login')
	g=UserForm()
	return render(request,'html/signup.html',{'t':g})

def antique(request):
	return render(request,'html/antique.html')
def art(request):
	return render(request,'html/art.html')
def jewellery(request):
	return render(request,'html/jewellery.html')
def buy(request):
	context  ={
	"Confirmation" : "item Bought Succesfully",
	"Greetings" : "Thank you !",
	}
	if request.method == "POST":
		e = request.POST['email'].split(',')
		s = "Item Bought Succesfully"
		d = "Thankyou for buying items in our website and hope you come back soon to buy again.It's pleasure to have you !.Thankyou"
		y = settings.EMAIL_HOST_USER
		z = send_mail(s,d,y,e)
		if z==1:
			messages.success(request,"Your Item bought succesfully")
			return redirect('/buy')
		else:
			return HttpResponse("Not Sent")
	return render(request,'html/buy.html',context)

def itemDeleteView(request,y):
	p=AntiqueItem.objects.get(id=y)
	if request.method=="POST":
		p.delete()
		return redirect('/item_list')
	return render(request,"html/item_delete.html",{'h':p})

def itemUpdateView(request,w):
	f=AntiqueItem.objects.get(id=w)
	if request.method=="POST":
		f.name=request.POST['n']
		f.description=request.POST['y']
		f.startingprice=request.POST['b']
		f.save()
		return redirect("/item_list")
	return render(request,'html/item_update.html',{'s':f})

def sellitemView(request):
	context  ={
	"Confirmation" : "Details Submitted Succesfully",
	"Greetings" : "You will be provided with our agent who can help you..!",
	}
	if request.method == "POST":
		e = request.POST['email'].split(',')
		s = "Details submitted Succesfully"
		d = "Dear, "+request.POST['cname']+"\n"+"Contact Details"+"\n"+"Agent name: Mahesh"+"\n"+"Agent Ph.no:9347820369"+"\n"+"Store Location: Rajahmundry-533101"+"\n"+"Thankyou for visting our website and hope you come back soon.It's pleasure to have you !."
		y = settings.EMAIL_HOST_USER
		z = send_mail(s,d,y,e)
		if z==1:
			messages.success(request,"Details Submitted Succesfully")
			return redirect('/sell_item')
		else:
			return HttpResponse("Not Sent")
	return render(request,'html/sellitem.html',context)

def auctionView(request):
	a=Auction.objects.filter(winner_id=request.user.id)
	if request.method=="POST":
		# j=AntiqueItemForm(request.POST)
		r= AuctionItemForm(request.POST)
		if r.is_valid():
			c=r.save(commit=False)
			c.winner_id=request.user.id 
			c.save()
			return redirect('/auction')
	r=AuctionItemForm()
	return render(request,'html/Auction.html',{'p':r,'q':a})
def itemView(request):
	h=AntiqueItem.objects.filter(usitem_id=request.user.id)
	if request.method=="POST":
		# j=AntiqueItemForm(request.POST)
		j= AntiqueItemForm(request.POST, request.FILES)
		if j.is_valid():
			c=j.save(commit=False)
			c.usitem_id=request.user.id 
			c.save()
			return redirect('/item_list')
	j=AntiqueItemForm()
	return render(request,'html/item_list.html',{'w':j,'s':h})
def auctionItemDeleteView(request,z):
	p=Auction.objects.get(id=z)
	if request.method=="POST":
		p.delete()
		return redirect('/auction')
	return render(request,"html/auction_item_delete.html",{'a':p})

def auctionItemUpdateView(request,a):
	f=Auction.objects.get(id=a)
	if request.method=="POST":
		f.item=request.POST['n']
		f.start_time=request.POST['y']
		f.end_time=request.POST['b']
		f.bid_amount=request.POST['a']
		f.highest_bid=request.POST['c']
		f.winner_name=request.POST['d']
		f.save()
		return redirect("/auction")
	return render(request,'html/auction_item_update.html',{'b':f})