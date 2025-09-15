# Multi-Agent GenAI Financial System (AWS Bedrock)

Cloud-native multi-agent system that ingests financial/news data, plans analysis, and produces explainable briefs and simple risk scores. Built on **AWS Bedrock** with serverless orchestration for reliability, traceability, and low ops overhead.

---

## ✨ Features
- **Planner Agent**: breaks down queries into sub-tasks.  
- **Research Agent**: pulls structured + unstructured data, summarizes findings.  
- **Analyst Agent**: fuses evidence, generates opinionated brief with citations.  
- **Risk Agent**: computes a 0–100 risk score with rationale.  
- **Guardrails & Logging**: prompt/response logging, PII filters, confidence tags.  

---

## 🏗️ Architecture
- **API Gateway** → **Lambda (Router)** → **Step Functions** (Orchestration)  
- **Agents as Lambdas**: Planner, Research, Analyst, Risk  
- **Bedrock Models**: Claude family (reasoning), Titan embeddings (optional for RAG)  
- **S3**: artifacts, **DynamoDB**: runs metadata, **CloudWatch**: metrics/traces  

