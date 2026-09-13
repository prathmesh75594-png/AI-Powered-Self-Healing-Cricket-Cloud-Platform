# 🏏 AI-Powered Self-Healing Cricket Cloud Platform

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-API-black?logo=flask">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker">
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes">
  <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus">
  <img src="https://img.shields.io/badge/DevOps-Cloud--Native-orange">
  <img src="https://img.shields.io/badge/Self--Healing-Automated-success">

</p>

<p align="center">
  <b>A cloud-native cricket platform demonstrating Docker, Kubernetes, monitoring, fault recovery and automated self-healing.</b>
</p>

---

# 🚀 Project Overview

The **AI-Powered Self-Healing Cricket Cloud Platform** is a cloud-native DevOps project designed to demonstrate how a modern application can be:

- Developed
- Containerized
- Deployed
- Orchestrated
- Monitored
- Scaled
- Recovered automatically

using modern **DevOps, Cloud, Kubernetes and Observability technologies**.

The project uses a cricket-based application as the business layer while the primary focus is on building a **reliable and resilient cloud-native infrastructure**.

The application consists of a **Flask-based Cricket API**, a web frontend, containerized workloads and Kubernetes orchestration.

The platform is designed around the principle:

> **Detect → Recover → Restore → Continue Serving**

---

# 🎯 Problem Statement

Traditional applications may become unavailable when:

- A container crashes
- An application process stops
- A Kubernetes pod fails
- Traffic increases
- A service becomes unhealthy
- Infrastructure resources become unavailable

Manual intervention can increase downtime and operational effort.

This project demonstrates how Kubernetes and monitoring technologies can be used to create a more resilient architecture where infrastructure can automatically detect failures and recover application workloads.

---

# 💡 Project Objectives

The major objectives of this project are:

### 1. Containerization

Package application components into portable Docker containers.

### 2. Kubernetes Orchestration

Deploy and manage application containers using Kubernetes.

### 3. High Availability

Run multiple API replicas so that the application does not depend on a single container.

### 4. Self-Healing

Allow Kubernetes to automatically recreate failed workloads.

### 5. Monitoring

Collect application and infrastructure metrics using monitoring tools.

### 6. Cloud-Native Architecture

Follow modern cloud-native principles such as:

- Containers
- Declarative infrastructure
- Service discovery
- Replication
- Health checks
- Observability
- Automated recovery

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      User / Browser  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Cricket Frontend   │
                         │      Nginx / HTML    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                     ┌─────────────────────────────┐
                     │      Kubernetes Service     │
                     │     cricket-api-service     │
                     └──────────────┬──────────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         ▼                     ▼
                ┌─────────────────┐   ┌─────────────────┐
                │   Cricket API   │   │   Cricket API   │
                │      Pod #1     │   │      Pod #2     │
                └────────┬────────┘   └────────┬────────┘
                         │                     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Monitoring      │
                         │     Prometheus       │
                         └──────────────────────┘
