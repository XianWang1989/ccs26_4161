
# views.py
from postman.views import compose

urlpatterns = [
    ...,
    path('postman/compose/', compose, name='compose'),
]
