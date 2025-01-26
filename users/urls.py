from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    # path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/',views.logout_view,name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='users/password-change-form.html'),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='users/password-change-done.html'),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password-reset-form.html'),name='password_reset'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_view.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),name='password_reset_complete'),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),

]
