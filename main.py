import logging
from guardrails.errors import ValidationError
from validators.validator_factory import ValidatorFactory
from structured.structured_output import StructuredGuardFactory
from validator_config import CONFIG

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

# -------- TEXT VALIDATION TESTS --------
print("\n🔍 TEXT VALIDATION\n" + "="*40)

texts = [
    "Hello, how are you?",
    "Call me at 415-555-1212",
    "I love Apple products",
    "My email is user@example.com",
    "You're a stupid idiot!",
    "Normal friendly message."
]

validator_factory = ValidatorFactory(CONFIG)
validators = [
    validator_factory.competitor_check(),
    validator_factory.detect_pii(),
    validator_factory.toxic_language(),
    # validator_factory.regex_match()  # Optional
]

from guardrails import Guard
text_guard = Guard().use_many(*validators)

for msg in texts:
    print(f"\n➡️ Test input: {msg!r}")
    try:
        text_guard.validate(msg)
        print("✅ Passed all guardrails!")
    except ValidationError as e:
        print("❌ Blocked by guardrail:")
        print("   •", e)

# -------- STRUCTURED OUTPUT TEST --------
print("\n🧭 STRUCTURED LLM OUTPUT VALIDATION\n" + "="*40)

prompt = """
I'm planning a vacation and need advice.

Where should I go, and why?

${gr.complete_json_suffix_v2}
"""

structured_guard = StructuredGuardFactory.travel_recommendation_guard()

response = structured_guard(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": prompt
    }]
)

print("🌍 Travel recommendation:")
print(response.validated_output)
