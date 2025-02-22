from django.db import models
from django.db.models import Q, Count


class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    hire_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def get_candidates_without_job(cls):
        """Returns a queryset of candidates without any current job"""
        queryset = cls.objects.filter(~Q(jobs__end_date__isnull=True))
        # print(str(queryset.query)) # print the query
        return queryset

    @classmethod
    def get_most_popular_location(self, candidates):
        """
        input: candidates queryset
        Returns the most popular location in the candidates queryset
        """
        queryset = (
            candidates.values("location")
            .annotate(count=Count("id"))
            .order_by("-count")
            .first()
        )
        # print(str(queryset.query)) # print the query
        return queryset.get("location", None)


class CandidateEducation(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dateRange = models.CharField(max_length=255, null=True, blank=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="educations"
    )

    def __str__(self):
        return self.title


class CandidateJob(models.Model):
    id = models.IntegerField(primary_key=True)
    ocupation = models.CharField(max_length=255)
    dateRange = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    current_job = models.BooleanField(default=False)
    occupation_title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="jobs"
    )

    def __str__(self):
        return self.ocupation
