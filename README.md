# Flask Greeting on Kubernetes

[![CI](https://github.com/ayusprasad/k8s/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/k8s/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web-000000?logo=flask&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Manifests-326CE5?logo=kubernetes&logoColor=white)

A minimal Flask greeting service packaged in Docker and described by Kubernetes Deployment and Service manifests.

## Architecture

~~~text
Browser → Flask app (port 5000) → Docker image → Kubernetes Deployment (2 pods) → Service (port 8080)
~~~

## Local setup

### Prerequisites

- Python 3.11 or newer
- Docker
- A local Kubernetes cluster such as Minikube for the cluster demo

### Run with Python

~~~bash
git clone https://github.com/ayusprasad/k8s.git
cd k8s
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
~~~

Visit http://127.0.0.1:5000.

### Build and deploy locally

~~~bash
docker build -t kubernetes-test-app:latest .
kubectl apply -f deployment.yaml
kubectl get pods,services
~~~

The manifest targets a local cluster that has the kubernetes-test-app:latest image. The Service listens on port 8080 and forwards to port 5000.

## Quality checks

~~~bash
pytest -q
ruff check --select E4,E7,E9,F app.py tests
~~~

CI runs lint, tests, compilation, and a Docker image build for pushes and pull requests. No credentials are required.
