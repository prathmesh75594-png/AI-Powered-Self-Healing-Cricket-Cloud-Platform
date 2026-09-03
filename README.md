

# 🏏 AI-Powered Self-Healing Cricket Cloud Platform

An AI-powered cloud-native DevOps platform designed for cricket analytics, containerized deployment, Kubernetes orchestration, monitoring, and automated self-healing.

## 🚀 Project Overview

The AI-Powered Self-Healing Cricket Cloud Platform demonstrates how a modern cloud-native application can be developed, containerized, deployed, monitored, and automatically recovered using DevOps and Kubernetes technologies.

The platform currently contains a Flask-based Cricket API and a web-based frontend running as containerized workloads in a local Kubernetes cluster.

## 🏗️ Current Architecture

```text
                    ┌─────────────────────────┐
                    │     User / Browser      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Cricket Frontend     │
                    │      Nginx / HTML       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Kubernetes Service    │
                    │   cricket-api-service   │
                    └────────────┬────────────┘
                                 │
                       ┌─────────┴─────────┐
                       ▼                   ▼
                ┌─────────────┐     ┌─────────────┐
                │ Cricket API │     │ Cricket API │
                │   Pod #1    │     │   Pod #2    │
                └─────────────┘     └─────────────┘
