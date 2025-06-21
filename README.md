# 🛡️ GuardrailsLLM Validator App

A modular and extensible Python application using [Guardrails AI](https://www.guardrailsai.com/) to validate:

- ✅ **Text safety**: Filters for PII, toxicity, competitor mentions, and regex patterns
- 📊 **Structured outputs**: Ensures LLM responses conform to a Pydantic-defined schema

Built for real-world use in LLM pipelines, travel assistants, content platforms, and enterprise NLP systems.

⚠️ **Why not just use prompt engineering or few-shot prompting?**

While prompt engineering and few-shot examples can *guide* the LLM, they don't provide **guarantees**.

## 🔒 1. Prompting is Suggestive — Not Deterministic
Prompts guide behavior, but do not enforce it.

LLMs are probabilistic generators. Even if a prompt says "Output valid JSON with fields X, Y, Z", there's no guarantee it will always do so.

In production, these inconsistencies break pipelines or APIs.

🧠 Technical Issue: Prompting alone lacks enforcement of type safety, output structure, and logic consistency.

## 🔍 2. Content Safety Needs Deterministic Filters
You can’t rely on an LLM to police itself every time.

Even with explicit safety instructions like:

```bash
"Do not mention any personal information or offensive content."
```

### The model might still output:

- PII (names, phone numbers)

- Toxic language

- Brand or competitor mentions

### Guardrails can apply:

- Regex filters

- PII detectors

- Toxicity classifiers

- Custom validators (e.g., no political statements)

🛡️ Technical Benefit: These validators act post-generation, so they don't rely on the model's internal success — they enforce external constraints.

## 🧱 3. Structured Output Requires Schema Enforcement
LLMs can approximate structure, but they don’t guarantee it.

Even with few-shot prompting like:

```bash
Output: {"name": "", "age": "", "email": ""}
```
### You might get:

- Missing keys

- Misquoted strings

- Wrong nesting or types

- Extra or hallucinated fields

### With Guardrails:

- You define a Pydantic or JSON schema

### If output violates it:

- Guardrails automatically retries

- Or catches the error and raises it

You also get type validation and output coercion

🧠 Technical Reality: Structured output is mission-critical for downstream systems. Prompting can’t enforce it — guardrails can.

🔁 4. Retries & Recovery Are First-Class in Guardrails
### Prompting gives you one-shot outputs. If it fails:

- You need custom logic to detect failure

- Then re-prompt or fallback

### Guardrails handles this natively:

If a validator fails (e.g., schema mismatch), it:

- Retries with the same or a modified prompt

- Optionally triggers fallback flows or LLMs

You get a configurable retry strategy (max_retries, exponential backoff, etc.)

📈 Technical Edge: More resilient applications, less manual glue code.


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


## 📌 Features

🔐 Safety Layer: PII, toxicity, brand protection

🧭 Schema-Aware Validation: Detects malformed JSON or missing fields

⚙️ Modular Design: Add validators or schemas easily

🌐 Realistic Outputs: Designed for apps like AI assistants, chatbots, dashboards


