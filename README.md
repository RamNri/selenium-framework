# Enterprise Selenium + API Automation Framework

---

# Overview

This project is a production-inspired automation framework built using Python.

The framework combines **UI Automation** and **REST API Automation** inside a single scalable architecture while following enterprise software engineering practices.

Instead of focusing only on writing automated tests, this project demonstrates how an automation framework can be designed, structured, tested, and maintained as a software system.

The framework currently demonstrates:

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
- Execution Context
- Parallel Test Execution
- Failure Diagnostics
- Failure Artifact Management
- Screenshot Capture
- HTML Test Reporting
- Browser and Selenium Session Correlation
- Faker Seed Isolation
- Sensitive Data Masking
- CRUD Integration Testing

---

# Architecture

```text
                              Tests
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
          UI Automation                 API Automation
                 │                             │
           Page Objects                  Services
                 │                             │
                 │                       API Clients
                 │                             │
                 │                    Authentication Manager
                 │                             │
                 │                         API Client
                 │                             │
                 └──────────────┬──────────────┘
                                │
                                ▼
                       Test Infrastructure
                                │
                ┌───────────────┼────────────────┐
                │               │                │
        Execution Context     Logging       Diagnostics
                │               │                │
        Test Lifecycle     API Logging     Failure Artifacts
                │               │                │
        Parallel Execution  Masking        HTML Reporting
```

The framework separates test logic from framework infrastructure.

Tests interact with application-facing layers such as Page Objects and Services, while cross-cutting concerns such as execution context, logging, reporting, and failure diagnostics are handled by dedicated framework infrastructure.

---

# Design Principles

This framework follows modern software engineering practices rather than being a collection of automation scripts.

## SOLID Principles

- Single Responsibility Principle
- Dependency Injection
- Separation of Concerns

## Design Patterns

- Builder Pattern
- Mapper Pattern
- Service Layer
- Factory Pattern
- Response Object Pattern

## Framework Principles

- Strongly Typed Models
- Reusable Assertions
- Centralized Logging
- Execution Context Isolation
- Scalable Folder Structure
- Enterprise Layer Separation
- Testability
- Failure Diagnostics
- Observability

---

# Implemented Features

| Feature | Status |
|---|---|
| REST API Automation | ✅ |
| Authentication Manager | ✅ |
| API Client | ✅ |
| Builder Pattern | ✅ |
| Mapper Pattern | ✅ |
| Response Models | ✅ |
| Assertions | ✅ |
| CRUD Workflow | ✅ |
| Enterprise Logging | ✅ |
| Execution Context | ✅ |
| Parallel Execution | ✅ |
| Failure Sanitization | ✅ |
| Failure Artifact Management | ✅ |
| Screenshot Capture | ✅ |
| HTML Reporting | ✅ |
| Browser / Session Correlation | ✅ |
| Faker Seed Isolation | ✅ |
| Sensitive Data Masking | ✅ |

---

# Execution Context

The framework uses a thread-local execution context to maintain execution information independently for concurrent test threads.

The context contains information associated with the current test execution, including:

- Execution ID
- Worker ID
- Thread ID
- Test name
- Faker seed
- Browser
- Selenium Session ID
- Start time
- Duration
- Driver

A key design principle is the distinction between **worker identity**, **thread identity**, and **test execution identity**.

```text
Worker
  │
  └── Thread
        │
        ├── Test A
        │     └── Execution ID A
        │
        ├── Test B
        │     └── Execution ID B
        │
        └── Test C
              └── Execution ID C
```

A worker or thread may be reused for multiple tests.

However, each test execution receives a new execution ID and test-specific execution state.

This allows logs, reports, browser sessions, and failure artifacts to be correlated with the individual test execution.

---

# Parallel Execution

Parallel execution is implemented using `pytest-xdist`.

Example:

```powershell
pytest -v -n 2
```

This allows tests to execute across multiple pytest workers.

Workers may be reused across multiple tests, while the execution context creates a separate execution identity for each test.

Conceptually:

```text
                         Pytest
                           │
                ┌──────────┴──────────┐
                │                     │
               gw0                   gw1
                │                     │
             Thread A              Thread B
                │                     │
           ┌────┼────┐          ┌────┼────┐
           │    │    │          │    │    │
          T1   T2   T3         T4   T5   T6
           │    │    │          │    │    │
          E1   E2   E3         E4   E5   E6
```

Where:

- `gw0`, `gw1` represent pytest workers
- Thread IDs identify the execution thread
- `T1`, `T2`, etc. represent individual tests
- `E1`, `E2`, etc. represent individual test execution IDs

This separation allows the framework to maintain reliable test-level correlation even when the same worker or thread executes multiple tests.

---

# Logging

The framework provides centralized, execution-aware logging using Python's logging infrastructure.

Logs include contextual information such as:

- Timestamp
- Log level
- Logger name
- Execution ID
- Worker ID
- Thread ID
- Test name
- Faker seed
- Message

Example:

```text
2026-08-27 11:44:44 | INFO | core.driver.driver_factory |
[exec=07e9b33c... | worker=gw0 | thread=34064 |
test=tests/test_failure_artifacts.py::test_failure_artifact |
seed=904989091] |
Browser created : chrome
```

This allows a log message to be traced back to a specific test execution.

---

# API Logging

API requests and responses are logged with execution context.

Example:

```text
HTTP REQUEST

POST /booking

↓

HTTP RESPONSE

200 OK

Elapsed : 0.32 sec
```

API logging includes:

- HTTP method
- Endpoint
- Request body
- Response status
- Response reason
- Response body
- Response time
- Execution context

Sensitive information is masked before being written to logs.

---

# Sensitive Data Masking

The framework prevents sensitive information from being exposed in logs.

Sensitive fields include values such as:

```text
password
token
access_token
refresh_token
authorization
api_key
secret
client_secret
```

Masking is applied to both request headers and structured request bodies.

Example:

```text
{
    "username": "user",
    "password": "********"
}
```

This provides safer diagnostics without exposing credentials or authentication data in framework logs.

---

# Failure Diagnostics

Failure diagnostics are implemented as a dedicated framework capability.

When a test fails:

```text
Test Failure
     │
     ▼
pytest lifecycle hook
     │
     ▼
Failure Sanitizer
     │
     ▼
Failure Artifact Manager
     │
     ▼
Screenshot Capture
     │
     ▼
pytest-html Report
```

The framework automatically captures a browser screenshot when a UI test fails.

Failure processing is separated from the pytest lifecycle so that individual components remain independently testable.

---

# Failure Artifact Management

Failure artifacts are isolated by worker and execution ID.

Example:

```text
artifacts/
└── screenshots/
    └── gw0/
        └── <execution_id>/
            └── test_failure_artifact_<timestamp>.png
```

This structure prevents artifacts from different parallel executions from overwriting each other.

The framework currently captures:

- Browser screenshots
- Failure information
- Execution metadata
- HTML report attachments

---

# Failure Sanitization

Failure information is sanitized before being written to framework logs.

This prevents sensitive information from accidentally being exposed through exception messages or failure representations.

The sanitization logic is maintained separately from the pytest lifecycle so that failure processing remains independently testable.

---

# HTML Reporting

The framework integrates with `pytest-html`.

The report includes execution metadata such as:

| Metadata |
|---|
| Execution ID |
| Worker |
| Thread |
| Browser |
| Selenium Session ID |
| Test Result |
| Duration |

For failed UI tests, the corresponding screenshot is attached to the HTML report.

This allows an engineer to move from:

```text
Failed Test
     ↓
Execution ID
     ↓
Worker / Thread
     ↓
Browser Session
     ↓
Screenshot
     ↓
Logs
```

when diagnosing a failure.

---

# Intentional Failure Validation

The framework contains a dedicated test for validating the failure-artifact pipeline.

The test is marked with:

```python
@pytest.mark.artifact_validation
```

Normal test execution excludes this intentional failure through `pytest.ini`.

Normal execution:

```powershell
pytest
```

The artifact validation test can be executed explicitly:

```powershell
pytest -m artifact_validation
```

For example:

```powershell
pytest -m artifact_validation -v -n 2 --html=artifacts/report.html --self-contained-html
```

The test is intentionally expected to fail so that the framework's screenshot capture and HTML-report attachment mechanisms can be validated.

---

# Project Structure

```text
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
│   ├── driver/
│   ├── execution/
│   └── logger.py
│
├── framework_logging/
│   ├── api_logger.py
│   ├── failure_artifact_manager.py
│   ├── failure_sanitizer.py
│   └── log_utils.py
│
├── pages/
│
├── services/
│
├── test_data/
│
├── tests/
│   ├── unit/
│   └── test_failure_artifacts.py
│
├── utilities/
│
└── artifacts/
```

The `artifacts/` directory contains runtime-generated logs, screenshots, and reports and is excluded from source control.

---

# Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Test Runner | Pytest |
| UI Automation | Selenium WebDriver |
| API Automation | Requests |
| Parallel Execution | pytest-xdist |
| Reporting | pytest-html |
| Logging | Python Logging |
| Test Data | Faker |
| Version Control | Git |

---

# Testing Strategy

The framework itself is tested using unit tests in addition to integration and framework-level validation.

The unit-test structure mirrors the framework components.

Examples include tests for:

- Execution Context
- Logging utilities
- Failure Sanitization
- Failure Artifact Management
- Execution lifecycle
- Sensitive-data masking

The framework also performs real parallel execution validation using pytest-xdist.

Example:

```powershell
pytest -v -n 2
```

---

# Running the Tests

## Run the normal test suite

```powershell
pytest -v
```

The intentional failure-artifact validation test is excluded from normal execution.

## Run tests in parallel

```powershell
pytest -v -n 2
```

## Run unit tests

```powershell
pytest .\tests\unit -v
```

## Run failure-artifact validation

```powershell
pytest -m artifact_validation -v -n 2 --html=artifacts/report.html --self-contained-html
```

---

# Git and Generated Artifacts

Runtime artifacts are intentionally excluded from source control.

Generated content such as:

```text
artifacts/
├── logs/
├── screenshots/
└── report.html
```

is ignored by Git.

Source code, framework components, tests, and configuration remain version controlled.

---

# Roadmap

## Completed

- Enterprise API Client
- Authentication Manager
- CRUD Workflow
- Response Models
- Builder Pattern
- Mapper Pattern
- Assertions
- Enterprise Logging
- Faker Integration
- Execution Context
- Parallel Execution
- Failure Diagnostics
- Failure Artifact Management
- Screenshot Capture
- HTML Reporting
- Browser / Session Correlation
- Sensitive Data Masking

## Upcoming

- Retry Mechanism
- Custom Exceptions
- Advanced Reporting
- GitHub Actions
- Docker
- BrowserStack Integration
- Azure DevOps Pipeline
- Allure Reports
- Slack Notifications
