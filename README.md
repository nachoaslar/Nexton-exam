# Nexton Exam

This project is based on the [Django Base Project](https://github.com/Linkcharsoft/django-base-project). Unnecessary files were removed, and the required ones were added to kickstart the project.

## 1. How to Run the Project

To run the project locally:

1. Clone the repository
2. Create a `.env` file by copying the `.env.example`
3. Start the project with Docker Compose:

```bash
docker-compose up -d
```

## 2. Project Explanation

The project automatically loads data from CSV files into Django Models using a custom script. When the project is started, the following models are populated:

- **Candidates**
- **CandidateJobs**
- **CandidateEducations**

### Key Endpoint

The following API endpoint is available:

- **POST** `/api/candidates/send-notification/`:  
Sends a notification saying the amount of candidate without a current job, and the location with the most amount of unemployed candidates

## 3. Other Considerations

- You can modify the database engine by updating the `DB_ENGINE` variable and adding the required database connection details in the `.env` file.

- To load data manually, run the following command:

```bash
python manage.py load_data
```

### Created By:

- **Juan Ignacio Borrelli**  
Email: nacho2911@hotmail.com
