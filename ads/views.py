import json

from django.db.models import QuerySet
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category, BaseModel


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class BaseView(View):
    model: BaseModel = BaseModel

    def get(self, request):
        positions: QuerySet = self.model.objects.all()
        response: list[dict] = [model_to_dict(position) for position in positions]

        return JsonResponse(response, safe=False)

    def post(self, request):
        request_data = json.loads(request.body)
        position = self.model()
        position.__dict__.update(request_data)

        position.save()

        return JsonResponse(model_to_dict(position), safe=False, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(BaseView):
    model = Ad


@method_decorator(csrf_exempt, name="dispatch")
class CatsView(BaseView):
    model = Category


class BaseDetailView(DetailView):
    model: BaseModel = None

    def get(self, request, *args, **kwargs):
        position = self.get_object()

        return JsonResponse(model_to_dict(position))


class AdsDetailView(BaseDetailView):
    model = Ad


class CatsDetailView(BaseDetailView):
    model = Category
