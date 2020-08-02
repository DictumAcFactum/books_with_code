from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .pilot_views import PilotList, PilotDetail
from .drone_views import DroneDetail, DroneList, DroneCategoryDetail, DroneCategoryList
from .competition_views import CompetitionDetail, CompetitionList


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
