# Platform Components

## Purpose

This document provides an overview of the major components that make up the Bürokratt platform.

Each component has a clearly defined responsibility and interacts with other components through the routing layer.

For implementation details, see the individual component documentation.

---

## Component Groups

The platform consists of four logical groups:

- Frontend Applications
- Routing Layer
- Backend Services
- Infrastructure

---

# Routing Layer

The routing layer is responsible for orchestrating business workflows.

The same Ruuter application is deployed as two independent instances:

| Component | Repository | Responsibility |
|-----------|------------|----------------|
| Public Ruuter | Ruuter | Handles public-facing requests and authentication workflows. |
| Private Ruuter | Ruuter | Handles administrator-facing workflows. |

---

# Backend Services

| Component | Repository | Responsibility |
|-----------|------------|----------------|
| TIM | TIM | Authentication and authorization. |
| Resql | Resql | SQL execution through REST APIs. |
| DataMapper | DataMapper | Request and response transformation using Handlebars templates. |
| S3-Ferry | S3-Ferry | Object storage integration. |
| Notification Server | notification-server / notifications-node | Notification delivery. |
| CronManager | CronManager | Scheduled workflow execution. |

---

# Frontend Applications

| Component | Repository | Responsibility |
|-----------|------------|----------------|
| Chat Widget | Chat-Widget | Public chatbot interface. |
| Authentication Layer | Authentication-Layer | Administrator authentication. |
| Chatbot | Buerokratt-Chatbot | Main administration interface. |
| Service Module | Service-Module | Service administration. |
| Analytics Module | Analytics-Module | Analytics and reporting. |

---

# Infrastructure

The platform relies on several shared infrastructure services.

| Component | Responsibility |
|-----------|----------------|
| PostgreSQL | Persistent storage. |
| TARA | External identity provider. |
| S3-compatible storage | Object and file storage. |
| OpenSearch | Search engine for indexing, querying. |

---

## Architectural Principles

- Frontend applications communicate through the routing layer.
- Public and administrator traffic are separated.
- Backend services are isolated.
- Backend services do not communicate directly with each other.
- Business workflows are orchestrated by Ruuter.
