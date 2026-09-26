# Gemini-Structure
Here a Gemini Structure, First programed Written by myslef no AI, I saw it on insta, and Learn the Logic and the coded it.... Thanks For Visit

Here a simple strucure u called, to Create and use gemin in your VS code or Antigravity!

---

### How to Setup and Run

#### 1. Active The Venv
In VS Code or Antigravity terminal:
```powershell
.\.venv\Scripts\Activate.ps1
```

#### 2. Install Package
Here importing genai package (from google):
```powershell
pip install google-genai
```

#### 3. Here is Our API key
In `Gemini.py`, add your Gemini API key:
```python
API_KEY = "YOUR_API_KEY"
```

#### 4. This is Promt Area Where we GIve Command to the Gemini Model
```python
prompt = "Explain how AI works in 2 simple sentences."
```

#### 5. This is resonse Section
And Last Before, This is where the Model Name, exist, and we can use:
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
```

#### 6. In Last By Here The Response Print
Run the file:
```powershell
python Gemini.py
```
And it prints:
```python
print("Gemini : ", response.text)
```
