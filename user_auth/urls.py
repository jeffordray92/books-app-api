from django.urls import path, include
from user_auth.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom-login'),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls'))
]
