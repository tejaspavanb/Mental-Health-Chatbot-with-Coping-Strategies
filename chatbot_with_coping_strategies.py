from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import random

# Download necessary data for sentiment analysis
nltk.download('vader_lexicon')

# Load GPT-Neo for text generation
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define some coping strategies
coping_strategies = {
    "breathing_exercise": "Try this: Take a deep breath in through your nose for 4 seconds, hold it for 7 seconds, and exhale through your mouth for 8 seconds. Repeat 3 times.",
    "grounding_technique": "Let's try grounding. Look around and name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
    "mindfulness_meditation": "Take a moment to close your eyes, focus on your breathing, and let any thoughts pass by without judgment. Try this for 5 minutes and see how you feel.",
    "journaling_prompt": "Here's a journaling prompt: Write about what’s currently weighing on your mind. How does it make you feel? What can you do to address it?"
}

# Function to suggest a random coping strategy
def suggest_coping_strategy():
    strategy = random.choice(list(coping_strategies.values()))
    return f"I have a suggestion for you: {strategy}"

# Function to get a response from the chatbot and suggest coping strategies
def get_response(user_input):
    # Analyze sentiment
    sentiment_score = sia.polarity_scores(user_input)
    if sentiment_score['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_score['compound'] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Generate a response from the chatbot
  response = chatbot(user_input, max_length=75, do_sample=True, temperature=0.5, clean_up_tokenization_spaces=True, truncation=True, pad_token_id=50256, num_return_sequences=1)

    
    # Customize response based on sentiment
    if sentiment == "positive":
        prefix = "I'm glad to hear that! "
    elif sentiment == "negative":
        prefix = "I'm sorry you're feeling this way. Remember, it's okay to feel sad sometimes. "
        # Suggest a coping strategy when the user feels negative
        prefix += suggest_coping_strategy() + " "
    else:
        prefix = "I understand. "
    
    return prefix + response[0]['generated_text']

# Testing the chatbot with a sample conversation
if __name__ == "__main__":
    print("Chatbot: Hi! I'm your mental health support assistant. How are you feeling today?")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
