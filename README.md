# 🏏 AI-Powered Self-Healing Cricket Cloud Platform

<p align="center">

  <img src="https://img.shields.io/badge/Kubernetes-Container%20Orchestration-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/DevOps-Cloud%20Native-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" />

</p>

<p align="center">

  <strong>A cloud-native cricket platform designed to detect failures, monitor workloads, and demonstrate Kubernetes self-healing.</strong>

</p>

---

## 🌟 Overview

**AI-Powered Self-Healing Cricket Cloud Platform** is a cloud-native DevOps project that combines a cricket analytics application with modern containerization, Kubernetes orchestration, monitoring, and automated recovery concepts.

The goal of this project is not only to deploy an application, but to demonstrate how a production-style platform can:

- 📦 Package applications using Docker
- ☸️ Deploy and manage workloads using Kubernetes
- 🔄 Recover failed application instances automatically
- 📊 Monitor application and infrastructure health
- 🚨 Detect unhealthy workloads
- 📈 Scale workloads using Kubernetes capabilities
- 🧪 Test failure and recovery scenarios
- 🔧 Apply real-world DevOps and SRE principles

The project currently contains a **Flask-based Cricket API**, a web frontend, Kubernetes manifests, and a monitoring layer.

---

# 🎯 Why This Project?

Traditional application deployment often looks like:

```text
Developer
    │
    ▼
Application
    │
    ▼
Server
    │
    ▼
Application Failure
    │
    ▼
Manual Investigation
    │
    ▼
Manual Restart
