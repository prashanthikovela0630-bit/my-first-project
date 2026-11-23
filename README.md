# DevOps Task Tracker with Automated Testing and Docker Deployment

A beginner-friendly Flask task tracker packaged with Docker and tested using pytest.

## Features
- Add task titles through a web form
- Display tasks in the browser
- Health endpoint at `/health`
- Automated test cases using pytest
- GitHub Actions runs tests on pushes and pull requests
- Dockerfile for repeatable container deployment

## Run automated tests first
```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

## Build and run with Docker
```bash
docker build -t devops-task-tracker:1.0 .
docker run -d --name task-tracker -p 5000:5000 devops-task-tracker:1.0
```
Open http://localhost:5000

Health check:
```bash
curl http://localhost:5000/health
```

## Stop and remove
```bash
docker stop task-tracker
docker rm task-tracker
```

## Test cases
1. Homepage returns HTTP 200 and displays the project title.
2. A valid task title is accepted and stored.
3. A blank task title is not stored.
4. Health endpoint returns HTTP 200 and the expected JSON response.

## GitHub workflow
The workflow in `.github/workflows/tests.yml` automatically installs test dependencies and runs pytest for pushes and pull requests.

## Note
Tasks are stored in application memory. They reset when the application restarts.
