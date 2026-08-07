# Enterprise Selenium + API Automation Framework
---
# Overview

This project is a production-inspired automation framework built using Python.

The framework combines **UI Automation** and **REST API Automation** inside a single scalable architecture while following enterprise software engineering practices.

Instead of focusing only on writing automated tests, this project demonstrates how automation frameworks are designed, structured and maintained

Current implementation includes:

- Selenium UI Automation
- REST API Automation
- Enterprise API Client
- Dependency Injection
- Authentication Manager
- Builder Pattern
- Mapper Pattern
- Response Object Pattern
- Service Layer
- Reusable Assertions
- Enterprise Logging
- CRUD Integration Testing

---

# Architecture

```
                    Tests
                       │
        ┌──────────────┴──────────────┐
        │                             │
   UI Automation                API Automation
        │                             │
   Page Objects               Booking Service
        │                             │
        └──────────────┬──────────────┘
                       │
                 Booking Client
                       │
              Authentication Manager
                       │
                   API Client
                       │
                RESTful Booker API
```

---

# Design Principles

This framework follows modern software engineering practices rather than being a collection of automation scripts.

### SOLID Principles

- Single Responsibility Principle
- Dependency Injection
- Separation of Concerns

### Design Patterns

- Builder Pattern
- Mapper Pattern
- Service Layer
- Factory Pattern
- Response Object Pattern

### Framework Principles

- Strongly Typed Models
- Reusable Assertions
- Centralized Logging
- Scalable Folder Structure
- Enterprise Layer Separation

---

# Implemented Features

| Feature               
|----------               
| REST API Automation
| Authentication Manager
| API Client
| Builder Pattern 
| Mapper Pattern 
| Response Models
| Assertions
| CRUD Workflow
| Enterprise Logging

---

# Project Structure

```
.
├── api/
│   ├── auth/
│   ├── builders/
│   ├── client/
│   ├── clients/
│   ├── factories/
│   ├── mapper/
│   ├── models/
│   └── responses/
│
├── assertions/
│
├── config/
│
├── core/
│
├── framework_logging/
│
├── pages/
│
├── services/
│
├── test_data/
│
├── tests/
│
├── utilities/
│
└── artifacts/
```

---

# Technology Stack

| Component         | Technology |
|------------       |------------|
| Language          | Python 3.12 |
| Test Runner       | Pytest |
| UI Automation     | Selenium WebDriver |
| API Automation    | Requests |
| Reporting         | Pytest HTML |
| Logging           | Python Logging |
| Version Control   | Git |

---

# Logging

The framework provides centralized enterprise logging.

Features include:

- Pretty formatted JSON
- Request / Response logging
- Response time logging
- Header logging
- Sensitive header masking
- Timestamped log folders
- Console + File logging

Example

```
HTTP REQUEST

POST /booking

↓

HTTP RESPONSE

200 OK

Elapsed : 0.32 sec
```

---

# Roadmap

- Enterprise API Client
- Authentication Manager
- CRUD Workflow
- Response Models
- Builder Pattern
- Assertions
- Enterprise Logging
- Retry Mechanism
- Custom Exceptions
- Faker Integration
- Parallel Execution
- Advanced Reporting
- GitHub Actions
- Docker
- BrowserStack Integration
- Azure DevOps Pipeline
- Allure Reports
- Slack Notifications