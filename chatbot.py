import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyBC-4CFXlxHkvLSoQCmPx82cNwaivKkIsM")

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def mental_health_chat():
    print("Mental Health Support Bot (Gemini-powered)")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Take care. You're not alone!")
            break

        try:
            response = model.generate_content(user_input)
            print("Bot:", response.text)
        except Exception as e:
            print("Error:", e)
            print("Bot: Sorry, something went wrong. Please try again.")

mental_health_chat()
