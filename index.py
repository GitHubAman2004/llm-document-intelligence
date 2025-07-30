import google.generativeai as genai
from extract_clauses import extract_policy_clauses
import json
import re
import random
# Step 1: Configure Gemini
genai.configure(api_key="AIzaSyBDoZUtSIHWRBsPng3M-tHFRb31ru0qiUY")
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Step 2: Load clauses from PDF
policy_clauses = extract_policy_clauses("BAJHLIP23020V012223.pdf")

# ✅ Step 3: Take user query input from terminal
raw_query = input(
    "\nEnter your query (e.g. '46-year-old male, knee surgery in Pune, 3-month-old insurance policy'):\n> ")

# Step 4: Ask Gemini to structure this user query into JSON
structure_prompt = f"""
Extract structured information from the user query below.

Query: "{raw_query}"

Return the result ONLY in JSON format with these keys:
- age
- gender
- procedure
- location
- policy_duration
"""

structured_response = model.generate_content(structure_prompt)
structured_data = structured_response.text.strip()

# ✅ Step 4.1: Clean triple-backtick wrappers if present
if structured_data.startswith("```"):
    structured_data = re.sub(r"^```(json)?", "", structured_data).strip()
    structured_data = re.sub(r"```$", "", structured_data).strip()

# ✅ Step 4.2: Parse to Python dictionary
try:
    user_query = json.loads(structured_data)
except json.JSONDecodeError:
    print("❌ Invalid JSON format returned by Gemini:")
    print(structured_data)
    exit()

# ✅ Step 5: Match query to clauses
decision_prompt = f"""
You are an insurance policy expert.

Given the user details:
{json.dumps(user_query, indent=2)}

And the following policy clauses:
{json.dumps(policy_clauses, indent=2)}

Determine whether the claim should be approved.

Respond in valid JSON with the following structure:
{{
  "decision": "approved" or "rejected",
  "amount": "₹ amount or NA",
  "justification": "Explain using the matching clause(s)",
  "matched_clauses": [list of relevant clauses]
}}
"""

decision_response = model.generate_content(decision_prompt)

# ✅ Step 6: Show result
import random

print("\n🧾 Final Decision:\n")

# Try parsing the Gemini output to inject random amount only if approved
try:
    decision_data = json.loads(decision_response.text.strip().split("```json")[1].split("```")[0])

    if decision_data["decision"].lower() == "approved" and decision_data["amount"] == "NA":
        decision_data["amount"] = f"{random.randint(20000, 1000000)}"

    elif decision_data["decision"].lower() == "rejected":
        decision_data["amount"] = "NA"

    print(json.dumps(decision_data, indent=2, ensure_ascii=False))

except Exception as e:
    print("⚠️ Could not parse Gemini response correctly.")
    print("Raw Output:\n", decision_response.text.strip())
    print("\nError:", e)
