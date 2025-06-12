from dotenv import load_dotenv
import google.generativeai as genai
import os
import re

load_dotenv()

# Set up your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash")

def classify_with_llm(log_msg):
    """
    Classify the log message using Gemini into:
    (1) Workflow Error, (2) Deprecation Warning, or "Unclassified"
    """
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}'''

    response = model.generate_content(prompt)
    content = response.text

    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1).strip()

    return category

if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))