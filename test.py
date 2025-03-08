import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyCONB8fwncr6jp3HFenzYomUY15bdljjQw")

model = genai.GenerativeModel("gemini-1.5-pro-latest")

response = model.generate_content("Explain Machine Learning in simple words")

print(response.text)

