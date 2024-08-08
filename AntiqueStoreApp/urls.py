from django.urls import path
from .import views
from django.contrib.auth import views as ad
urlpatterns = [
    path('home/',views.homeView,name="home_url"),
    path('antique/',views.antique,name="antique_url"),
    path('jewellery/',views.jewellery,name="jewellery_url"),
    path('buy/',views.buy,name="buy_url"),
    path('art/',views.art,name="art_url"),
    path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="login_url"),
	path('signup/',views.signupView,name="signup_url"),
	path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="logout_url"),
    path('item_list/',views.itemView,name="item_list_url"),
    path('item_delete/<int:y>/',views.itemDeleteView,name="item_delete_url"),
    path('item_update/<int:w>/',views.itemUpdateView,name="item_update_url"),
    path('sell_item/',views.sellitemView,name="sell_item_url"),
    path('auction/',views.auctionView,name="auction_url"),
    path('auction_Item_Delete/<int:z>/',views.auctionItemDeleteView,name="auction_delete_url"),
    path('auction_Item_Update/<int:a>/',views.auctionItemUpdateView,name="auction_update_url"),
]