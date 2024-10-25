from django.urls import path, include
from .views import get_suporte_page, get_guide_list

axios_patterns = [
    path('get-guide-list/', get_guide_list, name='get-guide-list')
]

urlpatterns = [
    path('suporte', get_suporte_page, name="suporte"),
    path('suporte/api/', include(axios_patterns))
]
