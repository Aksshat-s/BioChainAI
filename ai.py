import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


OPENAI_KEY = os.getenv("OPENAI_API_KEY")
USE_OPENAI = OPENAI_KEY is not None and OPENAI_KEY != ""


if USE_OPENAI:
    import openai
    openai.api_key = OPENAI_KEY


def generate_summary(user_data):
    """
    Generates an AI summary. If no API key is set, returns a dummy summary.
    """
    if USE_OPENAI:
        prompt = f"Given the following physiology/lifestyle data, generate a 120-180 word explanation:\nHydration: {user_data['hydration']}\nSleep: {user_data['sleep']}\nSymptoms: {user_data['symptoms']}\nStress: {user_data['stress']}\nNotes: {user_data['notes']}\n\nProvide an educational summary, no diagnosis."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    else:
        # Dummy summary for testing
        return f"Based on the provided physiology and lifestyle data, it appears that hydration level is {user_data['hydration']}, sleep is {user_data['sleep']} hours, stress level is {user_data['stress']}, and symptoms include {user_data['symptoms']}. This data can affect multiple systems including cardiovascular, nervous, and digestive systems."