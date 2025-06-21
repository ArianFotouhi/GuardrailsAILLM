# 🛡️ GuardrailsLLM Validator App

A modular and extensible Python application using [Guardrails AI](https://www.guardrailsai.com/) to validate:

- ✅ **Text safety**: Filters for PII, toxicity, competitor mentions, and regex patterns
- 📊 **Structured outputs**: Ensures LLM responses conform to a Pydantic-defined schema

Built for real-world use in LLM pipelines, travel assistants, content platforms, and enterprise NLP systems.

⚠️ **Why not just use prompt engineering or few-shot prompting?**

While prompt engineering and few-shot examples can *guide* the LLM, they don't provide **guarantees**.

- **Prompting is suggestive**, not strict. The LLM might still leak PII, generate toxic content, or deviate from the desired output format — especially under different contexts or user inputs.
- **Text safety needs enforcement**, not just instruction. Guardrails acts as a post-processing filter that can catch and block unsafe outputs with validators that detect PII, toxicity, competitor mentions, and more — even if the model fails to self-censor.
- **Structured outputs require schema enforcement**. LLMs can forget a field, change the format, or return invalid JSON despite good prompting. Guardrails ensures outputs **conform to a defined Pydantic schema**, so they are safe to parse and consume programmatically.

✅ In short: **Prompting helps — Guardrails ensures.**

---

## 📂 Project Structure

```bash
guardrails_app/
│
├── main.py # Entrypoint: runs text & LLM validations
├── validator_config.py # Config for validators
│
├── validators/
│ └── validator_factory.py # Handles PII, toxicity, competitors, regex
│
├── structured/
│ └── structured_output.py # Defines output schema for LLM results
│
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/guardrails-llm.git
cd guardrails-llm
```
### 2. Install Dependencies

bash
```
pip install -r requirements.txt
```
You will need an OpenAI API key for structured output validation. Set it as:

```bash
export OPENAI_API_KEY=your-key
```
```bash
python3 main.py
```
🔍 Output
```bash
➡️ Test input: 'Hello, how are you?'
✅ Passed all guardrails!

➡️ Test input: 'Call me at 415-555-1212'
❌ Blocked by guardrail:
   • The following text in your response contains PII:
     Call me at 415-555-1212
```

```bash
🌍 Travel Recommendation Output
{
  "destination": "Tokyo",
  "country": "Japan",
  "region": "Asia",
  "reason": "Tokyo offers a unique blend of traditional culture and modern technology...",
  "activities": [
    "Visit the historic Senso-ji Temple",
    "Explore Shibuya and Shinjuku",
    "Try authentic Japanese cuisine"
  ],
  "estimated_budget_usd": 3000.0,
  "best_season": "Spring (March to May)",
  "traveler_type": "All types of travelers",
  "travel_advice": "Be respectful of local customs like removing shoes indoors"
}
```

🧠 Built With
Guardrails AI – LLM output validation

Pydantic – Structured schema enforcement

OpenAI GPT – LLM backend

📌 Features
🔐 Safety Layer: PII, toxicity, brand protection

🧭 Schema-Aware Validation: Detects malformed JSON or missing fields

⚙️ Modular Design: Add validators or schemas easily

🌐 Realistic Outputs: Designed for apps like travel assistants, chatbots, dashboards


