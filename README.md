# DevOps Task Tracker

A simple Flask task-tracking application packaged with Docker and tested using Pytest.

## Technologies
- Python 3.12
- Flask
- Pytest
- Git and GitHub
- Docker
- Docker Hub

## Project structure
```text
DevOps_Task_Tracker_With_TestCases/
├── app.py
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── .dockerignore
└── README.md
```

## Run locally (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
py -3.12 -m pip install -r requirements-dev.txt
py -3.12 app.py
```
Open http://localhost:5000

## Run tests
```powershell
py -3.12 -m pytest -v
```

## Build and run with Docker
```powershell
docker build -t devops-task-tracker:1.0 .
docker run -d --name task-tracker -p 5000:5000 devops-task-tracker:1.0
```
Open http://localhost:5000

Health endpoint: http://localhost:5000/health

## Publish to Docker Hub
Replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username:
```powershell
docker login
docker tag devops-task-tracker:1.0 YOUR_DOCKERHUB_USERNAME/devops-task-tracker:1.0
docker push YOUR_DOCKERHUB_USERNAME/devops-task-tracker:1.0
```

## Pull and run the published image
```powershell
docker pull YOUR_DOCKERHUB_USERNAME/devops-task-tracker:1.0
docker run -d --name task-tracker-test -p 5001:5000 YOUR_DOCKERHUB_USERNAME/devops-task-tracker:1.0
```
Open http://localhost:5001

Note: This is a simple demonstration application. Tasks are stored in memory and reset when the application process restarts. Use a production WSGI server and persistent database for production deployment.
