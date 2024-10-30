from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Subcategoria
from .utils import get_models_by_subcategory_dto, get_support_contents_by_name_dto

from services.apis.ploomes.technical_assistance import TechnicalAssistance

# Create your views here.
def get_suporte_page(request : HttpRequest) -> HttpResponse:
    template_name = 'suporte.html'
    models = get_models_by_subcategory_dto(1)
    context = {
        'models': models
    }
    return render(request, template_name, context)

def get_guide_list(request : HttpRequest) -> JsonResponse:
    support_contents = get_support_contents_by_name_dto('Guia')
    return JsonResponse({'guides': support_contents})


def get_assistances(request : HttpRequest) -> JsonResponse:
    assistances_api = TechnicalAssistance()
    assistances = assistances_api.getAllAssistances()
    return JsonResponse({'assistances': assistances})