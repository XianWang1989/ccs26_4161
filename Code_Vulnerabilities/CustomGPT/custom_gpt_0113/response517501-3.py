
from django.contrib.auth.models import User
user = User.objects.get(username='your_username')  # Replace with a test user
print(user.is_authenticated)
