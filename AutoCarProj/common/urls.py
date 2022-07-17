

from django import views
from django.contrib import admin
from django.urls import path, include
from common.views import SignUpView, ProfileUpdateView, ProfileView
from JobApp import views 
from common import views 
from django.contrib.auth import views as auth_views 
urlpatterns = [

    path('',views.start_page , name='start-page'),

    path('language',views.choose_lang , name='language'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    path('homepage', views.homepage, name="homepage"),
    path('homepage-arb', views.homepage_arb, name="homepage-arb"),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Authentication 
    path('register/', SignUpView.as_view(), name="register"),

    path('login', auth_views.LoginView.as_view(
        template_name='common/login.html'
        ),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
        ),
        name='logout'
    ),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
