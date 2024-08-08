from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import User,AntiqueItem,Auction
from image_uploader_widget.widgets import ImageUploaderWidget

class UserForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Password Again",
		}))
	class Meta:
		model = User
		fields= ["username","uid"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
		}
class AntiqueItemForm(forms.ModelForm):
	class Meta:
		model=AntiqueItem
		fields=["name","itemtype","TagLine","description","startingprice","maximumprice","image"]
		label={
			'image': ImageUploaderWidget(),
		}
		widgets={
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Name",
			}),
		"itemtype":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Item Type",
			}),
		"TagLine":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Title",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Description",
			}),
		"startingprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Min Price",
			}),
		"maximumprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Max Price",
			}),
		}

class AuctionItemForm(forms.ModelForm):
	class Meta:
		model=Auction
		fields=["item","start_time","end_time","bid_amount","highest_bid","winner_name"]
		widgets={
		"item":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Item Name",
			}),
		"start_time":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"start_time",
			}),
		"end_time":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"end_time",
			}),
		"bid_amount":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Bid Amount",
			}),
		"highest_bid":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Highest Bid",
			}),
		"winner_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Winner Name",
			}),
		}
