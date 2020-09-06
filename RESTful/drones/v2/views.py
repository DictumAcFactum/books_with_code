from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .. import views


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'pilots': reverse(views.PilotList.name, request=request),
            'vehicles': reverse(views.DroneList.name, request=request),
            'competitions': reverse(views.CompetitionList.name, request=request),
            'vehicle_categories': reverse(views.DroneCategoryList.name, request=request),
        })