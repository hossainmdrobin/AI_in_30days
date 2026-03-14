from groq import Groq

# Add your API key here
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

print("=== AI Code Assistant ===")

mode = input("Choose mode (explain / debug / improve / generate): ")


# -----------------------------
# GENERATE NEW CODE
# ------------------------ -----
if mode == "generate":

    task = input("Describe the code you want: ")

    prompt = f"""
You are a senior Python developer.

Write clean Python code for this task:

{task}

Return only the code.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    code = response.choices[0].message.content

    print("\nGenerated Code:\n")
    print(code)

    with open("generated_code.py", "w") as f:
        f.write(code)

    print("\nCode saved to generated_code.py")


# -----------------------------
# ANALYZE EXISTING CODE
# -----------------------------
else:

    with open("sample_code.py", "r") as f:
        code = f.read()

    if mode == "explain":

        prompt = f"""
Explain the following Python code clearly.

Code:
{code}
"""

    elif mode == "debug":

        prompt = f"""
Find bugs or potential issues in this Python code.

Code:
{code}
"""

    elif mode == "improve":

        prompt = f"""
Improve the performance and readability of this Python code.

Code:
{code}
"""

    else:
        print("Invalid mode")
        exit()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    print("\nAI Response:\n")
    print(result)