from dj_rest_auth.views import LoginView
from rest_framework.response import Response


class CustomLoginView(LoginView):
    def get_response(self):
        original_response = super().get_response()
        user_data = {
            "user_id": self.user.id,
            "username": self.user.username,
        }
        original_response.data.update(user_data)
        return original_response
