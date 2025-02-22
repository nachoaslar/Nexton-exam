from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from django_base.base_utils.base_viewsets import BaseGenericViewSet
from candidates.models import Candidate
from candidates.utils import send_notification


class CandidatesView(BaseGenericViewSet):
    queryset = Candidate.objects.all()
    permissions = {
        "default": [AllowAny],
    }

    @action(detail=False, methods=["post"], url_path="send-notification")
    def send_notification(self, request):
        """Get all candidates without a current job and send a notification
        indicating that we have X amount of candidates without a job and
        indicate the location with the most amount of unemployed candidates"""

        candidates = Candidate.get_candidates_without_job()
        location = Candidate.get_most_popular_location(candidates)

        send_notification(location, candidates.count())
        return Response({"message": "Notification sent"}, status=status.HTTP_200_OK)
