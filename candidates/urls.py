from rest_framework.routers import DefaultRouter

from candidates.views import CandidatesView


router = DefaultRouter()
router.register(r"candidates", CandidatesView, basename="candidates")
