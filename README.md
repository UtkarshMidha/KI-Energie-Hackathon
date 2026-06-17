# KI-Energie-Hackathon

# PV Legal Advisor

AI-powered photovoltaic legal and technical assessment platform for Germany.

The system combines:

* German energy law knowledge base (EEG, EnWG, MsbG, NBauO)
* Rule-based legal reasoning engine
* Roof suitability assessment
* Incentive eligibility analysis
* Financial estimation
* OpenAI-generated feasibility reports

---

# Features

## Legal Assessment

Evaluates:

* Grid connection eligibility
* EEG feed-in remuneration eligibility
* Self-consumption rights
* Smart meter obligations
* Battery storage eligibility
* Solar mandates under NBauO

---

## Technical Assessment

Calculates:

* Roof suitability score
* Usable roof area
* Estimated PV capacity (kWp)
* Estimated annual energy yield
* Orientation impact
* Shading impact

---

## Incentive Analysis

Evaluates available:

* EEG feed-in remuneration
* KfW programs
* VAT incentives
* Battery-related incentives

---

## AI Report Generation

Uses OpenAI to generate:

* Executive summary
* Legal analysis
* Technical assessment
* Financial evaluation
* Recommended next steps

---

# Project Structure

```text
src/
├── agents/
├── api/
├── loaders/
├── services/
└── main.py

knowledge_base/
├── laws/
├── rules/
├── technical/
├── incentives/
└── prompts/
```

---

# Installation

Clone repository:

```bash
git clone <repository-url>
cd KI-Energie-Hackathon
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the API

Start FastAPI server:

```bash
uvicorn src.main:app --reload
```

API available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# Example Request

POST:

```text
http://localhost:8000/advisor
```

Body:

```json
{
  "city": "Braunschweig",
  "roof_area_m2": 100,
  "roof_type": "gable",
  "orientation": "south",
  "shading": "none",
  "battery_storage": true
}
```

---

# Example Output

The API returns:

* Roof assessment
* Legal evaluation
* Incentive eligibility
* Financial estimates
* AI-generated feasibility report

Example:

```json
{
  "roof_assessment": {
    "classification": "excellent",
    "estimated_kwp": 18,
    "annual_yield_kwh": 16200
  }
}
```

---

# Available Endpoints

## Health Check

```http
GET /health
```

---

## Knowledge Base Overview

```http
GET /kb
```

---

## Roof Assessment

```http
POST /roof
```

---

## Rule Evaluation

```http
POST /rules
```

---

## Full PV Advisor

```http
POST /advisor
```

---

# Knowledge Base

The platform uses structured JSON knowledge bases:

## Laws

* EEG
* EnWG
* MsbG
* NBauO

## Rules

* Decision Rules
* Eligibility Rules
* Permit Rules
* Subsidy Rules

## Technical

* Roof Assessment
* PV Design
* Battery Rules
* Inverter Rules
* Smart Meter Rules

## Incentives

* Federal Incentives
* State Incentives
* Municipal Incentives

---

# Technology Stack

* Python
* FastAPI
* OpenAI API
* JSON Knowledge Base
* Rule Engine
* Uvicorn

---

# Future Improvements

* Google Solar API integration
* GIS building analysis
* 3D roof modelling
* Automatic permit analysis
* State-specific legal updates
* Dynamic subsidy updates
* Installer recommendation engine
* RAG-based legal document retrieval

---

# License

Hackathon prototype for educational and demonstration purposes.
