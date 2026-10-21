# DevOps Platform Lab

A hands-on DevOps project demonstrating a complete CI/CD workflow
using GitHub Actions, Docker, Kubernetes, Kustomize and Argo CD.

The project implements automated testing, container image building,
image publishing, GitOps deployments and controlled promotion
between staging and production environments.

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions (CI)
    |
    +-- Run Python tests (pytest)
    |
    +-- Build Docker image
    |
    +-- Push image to GHCR
    |
    v
Update Staging Kustomize Overlay
    |
    v
Argo CD
    |
    v
Kubernetes - Staging
    |
    | Manual promotion
    v
GitHub Actions (CD)
    |
    v
Update Production Kustomize Overlay
    |
    v
Argo CD
    |
    v
Kubernetes - Production
