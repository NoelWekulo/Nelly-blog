from django.urls import path


from . import views

app_name = 'HealthApp'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('category/', views.category, name='category'),
    path('checkout/', views.checkout, name='checkout'),
    path('search_result/', views.search_result, name='search_result'),
    path('shop/', views.shop, name='shop'),
    path('blog-detail/<str:slug>/', views.single, name='blog_detail'),
    path('thankyou/', views.thankyou, name='thankyou'),
]