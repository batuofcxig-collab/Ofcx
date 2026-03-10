from django.urls import path

# Import your views here
# from . import views

urlpatterns = [
    # API routes for users
    path('api/users/', views.users_api, name='users_api'),

    # API routes for blog
    path('api/blog/', views.blog_api, name='blog_api'),

    # API routes for ecommerce
    path('api/ecommerce/', views.ecommerce_api, name='ecommerce_api'),

    # API routes for social apps
    path('api/social/', views.social_api, name='social_api'),
]