import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation patterns
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well. How about you?']),
    (r'college|placement', ['Our college has a dedicated placement cell to help students with job placements. How can I assist you?']),
    (r'job|placement', ['Our placement cell works with various companies to provide job opportunities to students. Is there a specific company or role you are interested in?']),
    (r'(.*) internship (.*)', ['Our college offers internships to students. Could you please provide more details about the type of internship you are looking for?']),
    (r'bye|goodbye', ['Goodbye!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hi! I'm your college placement chatbot. Ask me anything about placements or internships.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    print("Bot:", response)
