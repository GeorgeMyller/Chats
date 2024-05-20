#Chat para aconselhar o seu pet

import google.generativeai as genai
genai.configure(api_key='YOUR_API_KEY')
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

system_instruction="Você é um especialista em aconselhar pessoas que querem comprar animais de estimação, sejam eles animais silvestres ou domesticos. é importante  antes de aconselhar que você saiba os habitos do novo dono para cruzar com os habitos do animal indicado."

while(True):
    question = input("You: ")

    if question.strip ()== "":
        break
    response = chat.send_message(system_instruction + question)
    
    print("\n")
    print(f"Conselheiro: {response.text}")
    print("\n")



#result = model.generate_content("você pode me sugerirmum pet? eu tenho uma rotina muito ocupada, só estou em casa a noite")
#result.text