from django.contrib import admin
from candidates.models import Candidate, CandidateEducation, CandidateJob


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "location", "hire_flag")
    search_fields = ("title", "location")


@admin.register(CandidateEducation)
class CandidateEducationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "dateRange", "candidate")
    search_fields = ("title", "description", "dateRange")
    list_filter = ("candidate",)


@admin.register(CandidateJob)
class CandidateJobAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ocupation",
        "dateRange",
        "skills",
        "current_job",
        "occupation_title",
        "start_date",
        "end_date",
        "candidate",
    )
    search_fields = ("ocupation", "dateRange", "skills", "occupation_title")
    list_filter = ("current_job", "candidate")
