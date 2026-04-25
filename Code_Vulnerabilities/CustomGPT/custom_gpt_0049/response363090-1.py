
from django.db.models import Q

REQUEST_TYPE_ENTRANCE = 1
pattern = f"%{REQUEST_TYPE_ENTRANCE}%"

# This will work with both PostgreSQL and SQLite by using LIKE
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE)) | 
    Q(authorized_requests__contains=f",{REQUEST_TYPE_ENTRANCE},") | 
    Q(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE)) | 
    Q(authorized_requests__endswith=str(REQUEST_TYPE_ENTRANCE))
)
