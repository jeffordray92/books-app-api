from book_club.models import Logs


def log_action(user, model_name, action, details=""):
    Logs.objects.create(
        user=user,
        model_name=model_name,
        action=action,
        details=details
    )
