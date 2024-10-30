from django.urls import path, include
from .views import get_suporte_page, get_guide_list, get_assistances

axios_patterns = [
    path('get-guide-list/', get_guide_list, name='get-guide-list'),
    path('get-assistances/', get_assistances, name='get-assistances')
]

urlpatterns = [
    path('suporte', get_suporte_page, name="suporte"),
    path('suporte/api/', include(axios_patterns))
]
