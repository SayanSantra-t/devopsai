# 🤖 AI-Driven Predictive Monitoring & Auto-Remediation System

> An intelligent infrastructure monitoring system that predicts failures before they occur and automatically executes remediation actions to minimize downtime.

---

## 👨‍💻 Authors & Contributions

| Name               | Role                         | Responsibilities                                                                                                                            |
| ------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sayan Banerjee** | DevOps & Backend Engineering | Spring Boot backend development, system integration, deployment pipeline, containerization, infrastructure setup, auto-remediation services |
| **Sayan Santra**   | Machine Learning Engineer    | Data preprocessing, anomaly detection model development, training and evaluation                                                            |
| **Tarpon Mondal**  | Machine Learning Engineer    | Predictive modeling, time-series analysis, model optimization and testing                                                                   |

---

## 📌 Overview

Modern distributed systems generate massive operational metrics such as CPU usage, memory consumption, latency, and logs. Traditional monitoring systems react only after failures occur.

This project introduces an **AI-driven predictive monitoring system** capable of detecting anomalies early and automatically performing remediation actions to ensure system reliability.

---

## 🎯 Problem Statement

Reactive monitoring leads to:

* Late failure detection
* Increased downtime
* Manual recovery processes

Our system enables **proactive monitoring and autonomous recovery** using machine learning and DevOps automation.

---

## 🧠 Proposed Solution

### 🔍 Data Collection Layer

System metrics are continuously collected from monitored services.

### 📊 AI Prediction Layer (Python)

* Anomaly detection using ML models
* Time-series forecasting
* Failure probability estimation

### ⚙️ Auto-Remediation Layer (Spring Boot + DevOps)

* Decision engine evaluates anomaly scores
* Executes automated recovery actions:

  * Service restart
  * Resource scaling
  * Cache cleanup
  * Alert triggering

---

## 🏗 System Architecture

Metrics Collector
→ ML Prediction Engine (Python)
→ Spring Boot Decision Service
→ Auto-Remediation Executor
→ Monitoring Dashboard

---

## 🛠 Tech Stack

**Backend & DevOps**

* Java
* Spring Boot
* Docker
* CI/CD Pipeline
* AWS (Deployment)

**Machine Learning**

* Python
* Scikit-learn
* TensorFlow / LSTM Models

**Database**

* PostgreSQL / MongoDB

**Monitoring**

* Grafana / Logging Tools

---

## 📊 Results

| Metric              | Before System | After System          |
| ------------------- | ------------- | --------------------- |
| Failure Detection   | Reactive      | Predictive            |
| MTTR                | High          | Reduced               |
| Manual Intervention | Required      | Minimal               |
| Downtime            | High          | Significantly Reduced |

---

## 🔁 Setup & Execution

```bash
git clone https://github.com/SayanSantra-t/devopsai.git
cd devopsai
```

Run ML service:

```bash
python train.py
```

Run backend:

```bash
mvn spring-boot:run
```

---

## 📂 Project Structure

```
├── ml-service/
├── spring-backend/
├── remediation-scripts/
├── docker/
├── ci-cd/
└── README.md
```

---

## 📄 Research Contribution

This research demonstrates how integrating machine learning predictions with DevOps automation enables self-healing infrastructure systems capable of reducing operational downtime.

---

## 📜 License

MIT License
