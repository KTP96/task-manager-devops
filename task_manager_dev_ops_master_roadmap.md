# Task Manager App → DevOps Master Roadmap

## Goal
Use your **working basic task manager application** as the single project through which you learn DevOps from **Git → Linux → Packaging → CI/CD → Docker → Cloud → Infrastructure as Code → Kubernetes → Monitoring → Security**.

This roadmap is written for a **beginner** but aims to make you **job-ready and interview-ready**.

---

# 0. What DevOps actually means

DevOps is not just a toolset. It is a way of building and operating software so that:
- developers can ship changes quickly,
- systems are reliable,
- deployments are repeatable,
- environments are consistent,
- failures are observable and recoverable,
- automation replaces manual work wherever possible.

## In simple words
Instead of:
- writing code on a laptop,
- manually copying files to a server,
- hoping it works,
- and debugging production blindly,

DevOps teaches you to:
- version code properly,
- test automatically,
- build artifacts consistently,
- deploy safely,
- monitor health,
- scale systems,
- secure everything,
- and recover from failures.

---

# 1. The full picture: where your task manager app fits

Your task manager app will evolve through these stages:

## Stage 1 — Local development
You write code and run it locally.

## Stage 2 — Version control with Git
You track changes, branches, commits, merges, pull requests.

## Stage 3 — Build and dependency management
You define requirements and make builds reproducible.

## Stage 4 — Testing
You add unit tests, integration tests, linting, formatting.

## Stage 5 — CI
Every push automatically runs tests and checks.

## Stage 6 — Packaging
You build a deployable artifact or image.

## Stage 7 — Docker
Your app runs the same way everywhere.

## Stage 8 — CD / deployment
Deploy automatically to a server or platform.

## Stage 9 — Infrastructure as Code
Provision environments using code, not clicks.

## Stage 10 — Kubernetes
Run containers in a managed, scalable way.

## Stage 11 — Monitoring and logging
Know what is happening inside the system.

## Stage 12 — Security and reliability
Secrets, access control, backup, health checks, rollbacks.

That is DevOps in practice.

---

# 2. Core DevOps concepts map

## A. Source Control
- Git
- GitHub / GitLab / Bitbucket
- branching strategies
- merge conflicts
- pull requests
- code reviews
- tags/releases

## B. Development Environment
- Linux basics
- shell
- files, permissions, processes
- environment variables
- package managers
- virtual environments

## C. Build & Dependency Management
- requirements.txt / package.json / pom.xml style dependency files
- semantic versioning
- reproducible builds
- artifact generation

## D. Testing & Quality
- unit tests
- integration tests
- end-to-end tests
- static analysis
- linting
- formatting
- test coverage

## E. CI/CD
- pipelines
- runners/agents
- stages/jobs/steps
- triggers
- artifacts
- approvals
- rollbacks

## F. Containers
- Dockerfile
- image layers
- image registry
- container runtime
- volumes
- networks
- compose

## G. Cloud & Deployment Targets
- VM deployment
- PaaS deployment
- container platform deployment
- load balancer
- DNS
- reverse proxy

## H. Infrastructure as Code
- Terraform
- variables
- state
- modules
- providers

## I. Orchestration
- Kubernetes
- Pods
- Deployments
- Services
- Ingress
- ConfigMaps
- Secrets
- scaling
- rolling updates

## J. Observability
- logs
- metrics
- traces
- dashboards
- alerts

## K. Security
- IAM
- least privilege
- secret management
- image scanning
- dependency scanning
- TLS
- patching

## L. Reliability / Operations
- health checks
- backups
- auto-restart
- incident response
- SLO/SLI/SLA
- disaster recovery

---

# 3. Your project architecture we will build toward

We will assume your task manager app eventually looks like this:

- frontend (optional, maybe basic HTML or React later)
- backend API (for tasks CRUD)
- database (SQLite first, then PostgreSQL)
- tests
- Docker support
- CI pipeline
- deployment config
- Kubernetes manifests
- monitoring hooks

Even if your app is currently simple, that is fine. We will grow it step by step.

---

# 4. Phase-by-phase learning path

# Phase 1 — Foundations: Linux + Git + App basics

## What you must understand
- what a server is
- what an OS does
- why Linux dominates DevOps
- filesystem basics
- permissions
- processes
- ports
- environment variables
- package installation
- shell commands
- Git basics

## Why this matters for DevOps
Every CI runner, Docker container, VM, cloud host, and Kubernetes node is heavily Linux-oriented.

## Learn these Linux concepts clearly

### Filesystem
- `/` root
- `/home`
- `/etc`
- `/var`
- `/usr`
- `/tmp`
- absolute vs relative paths

### Commands you should know deeply
- `pwd`
- `ls`
- `cd`
- `mkdir`
- `touch`
- `cp`
- `mv`
- `rm`
- `cat`
- `less`
- `head`
- `tail`
- `grep`
- `find`
- `chmod`
- `chown`
- `ps`
- `top`
- `kill`
- `curl`
- `wget`
- `tar`
- `zip`
- `ssh`
- `scp`
- `nano` or `vim`

### Permissions
- read / write / execute
- user / group / others
- `755`, `644`, `700`
- why scripts need execute permission
- why directories need execute permission to enter

### Processes
- PID
- foreground/background
- signals
- `kill -9` vs graceful termination
- process monitoring

### Networking basics
- IP
- port
- localhost
- DNS
- HTTP vs HTTPS
- TCP basics
- why your app listens on a port

### Environment variables
Examples:
- `PORT`
- `DB_URL`
- `APP_ENV`
- `DEBUG`

These are critical because DevOps avoids hardcoding config inside code.

## Git concepts you must know deeply

### What Git is
Git tracks changes to files over time.

### Why Git matters in DevOps
CI/CD starts from source control events like push, PR, merge, release tag.

### Concepts
- repository
- working tree
- staging area
- commit
- branch
- merge
- rebase
- remote
- pull
- push
- clone
- tag
- release
- `.gitignore`

### Commands
- `git init`
- `git clone`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`
- `git branch`
- `git checkout`
- `git switch`
- `git merge`
- `git rebase`
- `git pull`
- `git push`
- `git remote -v`
- `git stash`
- `git tag`

## Hands-on labs using your task manager app

### Lab 1 — Initialize and structure repo
- Put your app into a Git repo.
- Add `.gitignore`.
- Make first clean commit.
- Create README.

### Lab 2 — Good commit hygiene
Make separate commits for:
- app setup
- task CRUD logic
- tests
- bug fix
- docs

### Lab 3 — Branching
- create `feature/add-docker`
- create `feature/add-tests`
- merge into main
- intentionally create a merge conflict and resolve it

### Lab 4 — Release tagging
- tag `v0.1.0`
- tag `v0.2.0`
- understand semantic versioning

## Interview questions
- What is the difference between Git and GitHub?
- What is the staging area?
- What happens during `git pull`?
- Merge vs rebase?
- Why use branches?
- What is `.gitignore` and why is it important?
- Why should secrets never be committed?

---

# Phase 2 — Build, dependencies, and Python app runtime basics

## Concepts
- runtime vs build time
- dependencies
- version pinning
- virtual environments
- reproducibility
- entry point
- configuration management

## Why this matters
"Works on my machine" usually means environment inconsistency.
DevOps solves that through reproducibility.

## Learn clearly
- what `requirements.txt` does
- why dependency versions matter
- what a virtual environment is
- why local Python packages can conflict
- why CI uses clean environments

## Hands-on labs

### Lab 1 — Create virtual environment
- create venv
- activate it
- install dependencies
- freeze requirements

### Lab 2 — Add app config through environment variables
Convert hardcoded values into env vars.
Example ideas:
- app port
- debug mode
- database path

### Lab 3 — Separate config by environment
Have:
- local/dev config
- test config
- production config approach

## Interview questions
- Why use a virtual environment?
- What is dependency pinning?
- What is reproducible build?
- Why should config not be hardcoded?
- Difference between build-time and runtime config?

---

# Phase 3 — Testing and code quality

## DevOps view of testing
Testing is not optional. Automation without quality gates is dangerous.

## Types of testing
- unit tests
- integration tests
- API tests
- end-to-end tests
- smoke tests
- regression tests

## Quality tools
- formatter
- linter
- security scanner
- test coverage

## Hands-on labs

### Lab 1 — Add unit tests
Test:
- create task
- list tasks
- update task
- delete task
- invalid input

### Lab 2 — Add negative tests
- empty title
- invalid ID
- duplicate data if relevant

### Lab 3 — Add linting and formatting
Examples depending on language:
- formatter
- linter
- import sorting

### Lab 4 — Coverage reporting
Track how much code is covered and identify gaps.

## DevOps concepts here
- shift left testing
- quality gates
- fast feedback
- flaky tests
- deterministic tests
- test isolation

## Interview questions
- Unit vs integration testing?
- Why are flaky tests dangerous?
- Why should CI fail on lint/test failure?
- What is test coverage? What are its limitations?

---

# Phase 4 — CI (Continuous Integration)

## What CI means
Every change is automatically validated through checks.

## Typical CI stages
- checkout code
- install dependencies
- lint
- run tests
- build artifact
- upload artifact

## CI concepts you must know
- pipeline
- workflow
- job
- step
- runner/agent
- trigger
- artifact
- cache
- matrix build
- status checks

## Why CI matters
Without CI:
- broken code gets merged,
- environments differ,
- release quality drops.

## Hands-on labs with your app

### Lab 1 — GitHub Actions CI pipeline
Create pipeline to:
- trigger on push and pull request
- set up runtime
- install deps
- run lint
- run tests

### Lab 2 — Add badge to README
Show build passing/failing.

### Lab 3 — Add matrix testing
Test against multiple runtime versions if appropriate.

### Lab 4 — Store artifacts
Upload test reports or packaged output.

## Concepts to understand deeply
- why pipelines should be fast
- why caching helps
- when to separate jobs
- fail fast principle
- branch protection rules

## Interview questions
- What is CI?
- What is a runner?
- What is an artifact in CI?
- Why run pipelines on PRs?
- Why is caching useful in CI?

---

# Phase 5 — Packaging and release management

## Concepts
- artifact
- versioning
- release process
- changelog
- build metadata

## Examples of artifacts
- Python wheel
- jar file
- zip bundle
- Docker image

## Labs
- define version in your app
- create release notes
- tag releases
- package application for deployment

## Interview questions
- What is an artifact?
- Difference between build artifact and runtime container?
- What is semantic versioning?

---

# Phase 6 — Docker and containers

## What a container is
A container packages your application with dependencies so it runs consistently across systems.

## Why containers matter in DevOps
They reduce environment mismatch and simplify deployment.

## Core Docker concepts
- image
- container
- layer
- Dockerfile
- build context
- registry
- volume
- network
- port mapping
- environment variables
- entrypoint
- command

## Important difference
- image = blueprint
- container = running instance

## Dockerfile concepts
- base image
- `WORKDIR`
- `COPY`
- `RUN`
- `ENV`
- `EXPOSE`
- `CMD`
- `ENTRYPOINT`

## Hands-on labs

### Lab 1 — Containerize your app
Create Dockerfile for task manager app.

### Lab 2 — Run locally in container
- build image
- run container
- map port
- access app in browser or curl

### Lab 3 — Use env vars in container
Pass database path, port, environment.

### Lab 4 — Docker ignore
Create `.dockerignore` and understand why it matters.

### Lab 5 — Multi-stage builds
If relevant, reduce image size.

### Lab 6 — Push image to registry
Push to Docker Hub or GitHub Container Registry.

## Docker Compose concepts
Use Compose to run:
- app
- database
Together.

### Lab 7 — Add PostgreSQL with Compose
Move from SQLite to PostgreSQL if ready.

## Interview questions
- What is the difference between image and container?
- Why use Docker?
- CMD vs ENTRYPOINT?
- What is a Docker layer?
- What is a registry?
- Why keep images small?
- What is the role of `.dockerignore`?

---

# Phase 7 — Deployment basics

## Concepts
- server
- VM
- reverse proxy
- process manager
- systemd
- Nginx
- domain
- DNS
- TLS certificate

## Deployment options to understand
- deploy to a VM manually
- deploy via Docker on a VM
- deploy to a platform service

## Hands-on labs

### Lab 1 — Deploy to one Linux server
- SSH into server
- copy code or pull repo
- install runtime
- run app

### Lab 2 — Run app as a service
Use systemd so app auto-starts after reboot.

### Lab 3 — Put Nginx in front
Use reverse proxy to route traffic.

### Lab 4 — Enable HTTPS conceptually
Understand TLS, certificates, termination.

## Interview questions
- What is a reverse proxy?
- Why use Nginx in front of an app?
- What is systemd?
- Why should applications run as services?
- What is port 80 vs 443?

---

# Phase 8 — CD (Continuous Delivery / Continuous Deployment)

## Difference
- Continuous Delivery: software is always ready to deploy
- Continuous Deployment: every approved change deploys automatically

## Concepts
- deployment pipeline
- approval gates
- staging environment
- production environment
- rollback
- canary / blue-green basics

## Hands-on labs

### Lab 1 — Auto deploy on merge to main
Deploy Dockerized app to a test server.

### Lab 2 — Staging vs production
Set up separate config or environments.

### Lab 3 — Rollback plan
Keep previous image tag and redeploy old version if needed.

## Interview questions
- Continuous Delivery vs Continuous Deployment?
- How would you make deployments safer?
- What is rollback?
- Why deploy to staging first?

---

# Phase 9 — Cloud fundamentals

## Core concepts
- region
- availability zone
- VM/instance
- VPC/network
- subnet
- security group / firewall
- load balancer
- object storage
- managed database
- IAM

## Why cloud matters in DevOps
Modern systems are built on cloud infrastructure and automation.

## Map your task manager app to cloud
- app runs on VM or container service
- DB runs in managed service or container
- files/logs may go to object storage
- DNS points users to load balancer

## Interview questions
- What is a VPC?
- What is a subnet?
- What is a load balancer?
- What is object storage?
- Why use IAM roles instead of hardcoded keys?

---

# Phase 10 — Infrastructure as Code (Terraform)

## What it is
Provisioning infrastructure using code instead of manual console clicks.

## Why it matters
Repeatability, reviewability, consistency, automation.

## Concepts
- provider
- resource
- variable
- output
- state
- plan
- apply
- destroy
- module
- backend

## Hands-on labs

### Lab 1 — Write first Terraform
Provision one simple VM or equivalent local/cloud resource.

### Lab 2 — Parameterize environment
Use variables for region, instance type, tags.

### Lab 3 — Split into modules
Separate networking and compute.

### Lab 4 — Remote state concept
Understand why team collaboration needs remote state.

## Interview questions
- Why use Terraform?
- What is state in Terraform?
- What is a module?
- Why is remote state important?
- What is drift?

---

# Phase 11 — Configuration management and automation

## Concepts
- provisioning vs configuration
- idempotency
- desired state
- shell scripts vs config management tools

## Tools to know conceptually
- Bash scripting
- Ansible basics

## Why it matters
After creating a server, you still need to configure it consistently.

## Labs
- write shell script to bootstrap app server
- install packages
- create app user
- copy config
- start service

## Interview questions
- What is idempotency?
- Why not do everything manually?
- Bash vs Ansible?

---

# Phase 12 — Kubernetes

## Why Kubernetes exists
When you have many containers across machines, you need orchestration:
- scheduling
- self-healing
- scaling
- service discovery
- rolling updates

## Core concepts
- cluster
- node
- pod
- deployment
- replica set
- service
- ingress
- namespace
- configmap
- secret
- volume
- persistent volume
- liveness/readiness probes
- autoscaling

## Learn each clearly

### Pod
Smallest deployable unit. Usually one app container.

### Deployment
Keeps desired number of pod replicas running.

### Service
Stable network endpoint for pods.

### Ingress
HTTP routing into the cluster.

### ConfigMap
Non-secret configuration.

### Secret
Sensitive config like passwords or API tokens.

### Readiness probe
Is app ready to receive traffic?

### Liveness probe
Is app alive, or should it be restarted?

## Hands-on labs with your task manager app

### Lab 1 — Run in local Kubernetes
Use a local cluster like minikube/kind.

### Lab 2 — Create Deployment
Run 2 replicas of your app.

### Lab 3 — Create Service
Expose the app inside the cluster.

### Lab 4 — Add ConfigMap and Secret
Move config outside image.

### Lab 5 — Add readiness/liveness probes
Make health checks meaningful.

### Lab 6 — Scale replicas
Scale from 2 to 5 and observe.

### Lab 7 — Rolling update
Deploy new image version without downtime conceptually.

## Interview questions
- What is a Pod?
- Why not run containers directly on VMs?
- Deployment vs StatefulSet?
- Service types?
- What are probes?
- ConfigMap vs Secret?
- How does Kubernetes self-heal?

---

# Phase 13 — Observability: logs, metrics, alerts

## What observability means
You should be able to understand system health from outputs.

## Three pillars
- logs
- metrics
- traces

## Concepts
- structured logging
- log levels
- latency
- throughput
- error rate
- dashboards
- alerts
- SLI/SLO/SLA

## Add observability to your app
- log every request
- log errors clearly
- expose health endpoint
- expose metrics if possible

## Interview questions
- What is the difference between logs and metrics?
- What would you monitor for a web app?
- What is latency?
- What is an SLO?

---

# Phase 14 — Security in DevOps

## Key concepts
- secrets management
- least privilege
- IAM
- dependency scanning
- image scanning
- patching
- TLS
- secure headers
- vulnerability management
- SBOM concept

## Major beginner mistakes
- committing secrets
- using latest tag everywhere
- running containers as root
- exposing DB publicly
- giving broad cloud permissions

## Hands-on labs
- move secrets to env vars or secret store conceptually
- scan dependencies
- scan container image
- remove hardcoded credentials

## Interview questions
- Why is storing secrets in Git bad?
- What is least privilege?
- Why should containers avoid running as root?
- What is image scanning?

---

# Phase 15 — Reliability and production thinking

## Concepts
- uptime
- health checks
- backups
- restore testing
- rate limiting
- retries
- timeouts
- circuit breaker concept
- graceful shutdown
- rolling restart
- rollback

## Interview questions
- What happens when a server crashes?
- How do you reduce downtime during deployments?
- Why are health checks important?
- What is graceful shutdown?

---

# Phase 16 — Real interview prep map

## Beginner DevOps interview topics you must be ready for

### Git
- branching
- merge conflict resolution
- PR workflows

### Linux
- permissions
- processes
- file search
- networking basics
- logs

### Scripting
- Bash basics
- variables
- loops
- exit codes
- writing automation scripts

### CI/CD
- why pipelines exist
- stages
- failures
- artifacts
- triggers

### Docker
- Dockerfile
- port mapping
- volumes
- image vs container

### Kubernetes
- pods
- deployments
- services
- probes
- scaling

### Cloud
- compute
- storage
- networking
- IAM

### Terraform
- state
- plan/apply
- variables
- modules

### Monitoring
- logs, metrics, alerts

### Security
- secrets, permissions, scanning

---

# 5. The exact project progression I recommend for your task manager app

## Project Version 1
- local app runs successfully
- README exists
- Git repo clean

## Project Version 2
- tests added
- linting added
- requirements locked

## Project Version 3
- CI pipeline runs on push/PR

## Project Version 4
- Dockerfile added
- app runs in container

## Project Version 5
- Compose added with DB

## Project Version 6
- deployed on VM
- Nginx/systemd or Docker-based deployment

## Project Version 7
- Terraform provisions infrastructure

## Project Version 8
- Kubernetes manifests added
- app runs in local cluster

## Project Version 9
- metrics/logging/health probes improved

## Project Version 10
- security hardening and interview storytelling ready

---

# 6. Mini glossary you must know

- **DevOps**: development + operations working together through automation and reliability.
- **CI**: automatic validation of code changes.
- **CD**: automatic or ready-to-go deployment.
- **Artifact**: built output of your app.
- **Container**: isolated runtime package for your app.
- **Image**: template used to start containers.
- **Registry**: storage for images.
- **Orchestration**: managing many containers across systems.
- **Infra as Code**: provisioning infrastructure using code.
- **Observability**: understanding system behavior through logs, metrics, traces.
- **Idempotent**: can run again and still reach the same desired state safely.
- **Rollback**: reverting to a previous working version.
- **Immutable infrastructure**: replace, don’t manually mutate, where possible.

---

# 7. What I recommend we do next together

We should turn this into a guided course using your actual task manager code.

## Step 1
You share:
- the current project structure,
- language/framework,
- how you run it,
- whether it has tests already.

## Step 2
We build this in order:
1. understand current codebase
2. Git fundamentals on your repo
3. add proper project structure
4. add tests
5. add CI
6. add Docker
7. add deployment
8. add Terraform
9. add Kubernetes
10. add interview questions after each phase

---

# 8. How I will teach you phase by phase

For each topic, I can give you:
- concept explanation in beginner language,
- why industry uses it,
- where it appears in your task manager app,
- hands-on lab,
- commands to run,
- expected output,
- common mistakes,
- interview questions,
- small exercises,
- mini project tasks.

---

# 9. Best way to proceed

We should start with **Phase 1 using your actual task manager app** and do this interactively.

## First module I would teach on your app
**Module 1: Git + repo structure + Linux basics + how the app runs locally**

Then:
**Module 2: testing + code quality**

Then:
**Module 3: CI/CD**

Then:
**Module 4: Docker**

Then:
**Module 5: deployment + cloud + Terraform**

Then:
**Module 6: Kubernetes + observability + security + interview prep**

---

# 10. Your outcome if you follow this properly

You will be able to explain:
- what DevOps is,
- how code moves from laptop to production,
- how Git, CI/CD, Docker, cloud, Terraform, and Kubernetes connect,
- how to build and deploy a real project,
- and how to answer interview questions with practical examples from your own task manager app.

---

# 11. Next input needed from you

Paste one of these:
- your project folder tree,
- your main app file,
- your requirements/dependencies file,
- or the full repo content.

Then we will start with:
**understanding your codebase and mapping DevOps concepts directly onto it.**

