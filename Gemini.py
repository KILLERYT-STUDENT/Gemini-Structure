# Here a simple strucure u called, to Create and use gemin in your VS code or Antigravity
# Here importing genai package (from google)...
from google import genai

# Here is Our API key
API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)
# This is Promt Area Where we GIve Command to the Gemini Model
prompt = "Explain how AI works in 2 simple sentences."

# This is resonse Section 
response = client.models.generate_content(
    # And Last Before, This is where the Model Name, exist, and we can use...
    model="gemini-2.5-flash",
    contents=prompt,
)
# In Last By Here The Response Print 
print("Gemini : ", response.text)
