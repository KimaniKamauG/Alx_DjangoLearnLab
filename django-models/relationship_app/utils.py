from django.core.exceptions import PermissionDenied

# Utility function to check roles

def check_role(user, role_name):
    if user.is_authenticated and hasattr(user, 'userprofile'):
        return user.profile.role == role_name
    raise PermissionDenied