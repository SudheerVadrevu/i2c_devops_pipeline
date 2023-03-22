# CI/CD Pipeline for Embedded I2C Simulation using Jenkins & Docker

This project simulates I2C acknowledgment signals from multiple devices with a full CI/CD DevOps pipeline using Jenkins, Docker, and Python. PDF waveform reports are generated post-simulation.

### Technologies:
- Jenkins Pipelines with Groovy
- Docker multi-stage builds
- Python-based I2C simulation
- Waveform and PDF export
- Slack/email stub notifications
# CI/CD pipeline for Embedded I2C Simulation using Jenkins & Docker
> Course: DV2530 | Decision Support Systems  
> Author: Sudheer Vadrevu | Master of Science in Computer Science, BTH  
> Timeline: Feb 2023 – Apr 2023  

---

## 🔧 Overview  
This project demonstrates a complete CI/CD framework for a Python-based I2C hardware simulation system using Jenkins, Docker, and GitHub Actions. It reflects modern DevOps practices tailored for embedded systems simulation pipelines.

---

## 📁 Folder Structure  
- `ci/` – Jenkins pipeline configs, Slack notifications, and Groovy scripts  
- `docker/` – Multi-stage Dockerfile with health checks  
- `docs/` – This README and supporting project documentation  
- `simulation/` – Python scripts simulating I2C protocol and waveform generator  
- `tests/` – Unit tests using `pytest` for simulation logic  
- `utils/` – CLI tools and waveform export functions  
- `requirements.txt` – Python dependency list with fixed versions

---

## 🔄 CI/CD Features  
- Jenkins pipeline with multistage test, build, and delivery  
- Slack notifications for build status  
- Code quality checks via `pylint`  
- Dockerized environment to ensure reproducibility  
- GitHub Actions for automated backup testing  

---

## 📡 Hardware Simulation  
- I2C simulation engine with ACK/NACK and clock line  
- Multiple device support and waveform visualization  
- Export support as PDF diagrams and waveform logs  

---

## 📊 Tools Used  
- Jenkins, GitHub Actions  
- Docker (multi-stage builds)  
- Python (Pytest, Pylint, Matplotlib)  
- VSCode, Git  

---

## 📘 Educational Context  
This project was implemented under the course DV2530 at BTH to demonstrate DevOps integration for embedded software workflows. All components were version-controlled and containerized to mimic real-world CI/CD practices.

---

## 🏁 Outcome  
- ✅ CI/CD pipeline fully automated for every push  
- ✅ Docker container builds with waveform tools  
- ✅ Simulated I2C verified via unit tests and visualization  
- ✅ Successfully presented as a master’s project deliverable at BTH

---
