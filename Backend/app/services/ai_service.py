# app/services/ai_service.py

# Existing imports
# import openai  # Can keep for later when real API is used

# Mock questions database
MOCK_QUESTIONS = {
    "backend developer": [
        "Explain the difference between REST and GraphQL.",
        "How do you optimize database queries?",
        "Describe a situation where you had to debug a complex backend issue."
    ],
    "frontend developer": [
        "Explain the difference between React and Vue.",
        "How do you optimize a web page for performance?",
        "Describe a time you fixed a tricky CSS bug."
    ],
    "fullstack developer": [
        "How do you structure a project with both frontend and backend?",
        "Explain a time you handled API integration issues.",
        "Describe your approach to debugging fullstack issues."
    ]
}

def get_mock_questions(role: str):
    """Return mock interview questions for a given role."""
    return MOCK_QUESTIONS.get(role.lower(), ["[MOCK] No questions available for this role."])

def ask_ai(role: str):
    """
    Simulates AI answering by returning mock questions.
    Replace with OpenAI or Gemini call later.
    """
    questions = get_mock_questions(role)
    return questions
