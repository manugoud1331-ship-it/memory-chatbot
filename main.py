from ollama import chat

print("manogna - A Chatbot that remembers")
messages = []
messages.append({
    "role":"system",
    "content":"Answer in a sentence of around 50 words max"
    })

while True:
    question = input("you:").strip()
    if question.lower() == "exit":
        print("goodbye")
        break
    elif question.lower() == "history":
        print("\n----chat History---")
        for message in messages:
            if message["role"]=="user":
               print("You: ",message["content"])
            elif message["role"] == "assistant":
               print("Bot: ",message["content"])
            print("--------------------\n")
              
    else:
        messages.append({
            "role":"user",
            "content":question
        })    
        response = chat(model="phi3:latest",
        messages=messages)
        answer = response.message.content
        messages.append({
            "role":"assistant",
            "content":answer
        })
        print("Bot: ",answer)