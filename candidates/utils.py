import pandas as pd
from candidates.models import Candidate, CandidateEducation, CandidateJob


def import_candidates():
    df = pd.read_csv("csv/CANDIDATES.csv")
    objects = [Candidate(**row) for _, row in df.iterrows()]
    Candidate.objects.bulk_create(objects, ignore_conflicts=True)


def import_education():
    df = pd.read_csv("csv/EDUCATION.csv")

    df.rename(columns={"education_id": "id"}, inplace=True)

    df = df.where(pd.notna(df), None)

    objects = [
        CandidateEducation(
            id=row["id"],
            title=row["title"],
            description=row["description"] or "",
            dateRange=row["dateRange"] if row["dateRange"] else None,
            candidate_id=row["candidate_id"],
        )
        for _, row in df.iterrows()
    ]

    CandidateEducation.objects.bulk_create(objects, ignore_conflicts=True)


def import_jobs():
    df = pd.read_csv("csv/JOBS.csv")

    df = df.where(pd.notna(df), None)

    for col in ["start_date", "end_date"]:
        df[col] = df[col].apply(lambda x: str(x) if x else None)

    objects = [CandidateJob(**row) for _, row in df.iterrows()]
    CandidateJob.objects.bulk_create(objects, ignore_conflicts=True)


def import_data():
    import_candidates()
    import_education()
    import_jobs()


def send_notification(location, candidates):
    """
    Emulates sending a notification
    Receives the location (string) and the amount of candidates (int) without a job
    """
    print(f"Currenltly there are {candidates} candidates without a job")
    print(f"The location with the most candidates without a job is {location}")
