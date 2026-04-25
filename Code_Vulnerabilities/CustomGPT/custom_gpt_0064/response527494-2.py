
from postman.views import SendView

urlpatterns = [
    # other paths
    path('send/', SendView.as_view(), name='send'),
]
