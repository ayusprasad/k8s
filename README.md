# ☸️ Kubernetes Deployment & Orchestration Lab

A complete containerized Python web application demonstrating **Docker packaging**, **Kubernetes Deployment**, **Pod Replication**, and **Cluster Service Routing**.

---

## 🌟 Key Features
- **Stateless Flask Service:** Lightweight container exposing health checks and dynamic template rendering.
- **Kubernetes Deployment Manifest:** Pre-configured with 2 pod replicas, CPU/memory limits, and selector match labels.
- **Kubernetes Service Manifest:** Routes port 8080 traffic across healthy pod replicas on port 5000.
- **Production Containerization:** Optimized Python 3.11 slim image.

---

## 🚀 Quickstart

### 1. Build Container Image
```bash
docker build -t kubernetes-test-app:latest .
```

---

### 2. Deploy to Kubernetes Cluster (Minikube / Kind / K8s)
```bash
# Apply deployment and service
kubectl apply -f deployment.yaml

# Inspect pods
kubectl get pods -l app=kubernetes-test-app

# Port-forward service to local browser
kubectl port-forward service/kubernetes-test-app 8080:8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

---

### 3. Local Standalone Run
```bash
pip install -r requirements.txt
python app.py
```
Open [http://localhost:5000](http://localhost:5000).

---

## 📁 Repository Structure
```text
k8s/
├── app.py             # Flask web application
├── Dockerfile         # Container image specification
├── deployment.yaml    # Kubernetes Deployment & Service manifest
├── requirements.txt   # Python dependencies
├── static/            # Static CSS stylesheets
├── templates/         # HTML Jinja templates
└── README.md          # Project guide
```
