def mental_health_bot()
    print(Hello, I'm your mental health assistant. How are you feeling today)
    
    while True
        user_input = input(You ).lower()
        
        if any(word in user_input for word in [sad, depressed, unhappy, down])
            print(Bot I'm sorry you're feeling this way. It's okay to feel sad sometimes. Want to talk more about it)
        elif any(word in user_input for word in [happy, good, great, joyful])
            print(Bot That's wonderful to hear! What made you feel this way)
        elif any(word in user_input for word in [anxious, nervous, worried, scared])
            print(Bot Anxiety can be tough. Try taking some deep breaths. Want to try a quick breathing exercise)
        elif exit in user_input or bye in user_input
            print(Bot Take care of yourself. Remember, you're not alone. Goodbye!)
            break
        else
            print(Bot I'm here to listen. Tell me more about what's on your mind.)

# Run the chatbot
mental_health_bot()