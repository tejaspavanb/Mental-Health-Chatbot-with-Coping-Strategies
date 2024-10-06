

# Mental Health Support Chatbot for Students

This project is a **Mental Health Support Chatbot** designed to assist students in coping with stress, anxiety, and other mental health challenges. It uses an open-source language model to generate natural language responses, combined with **sentiment analysis** to detect the emotional tone of the user's messages. The chatbot offers personalized coping strategies when negative sentiment is detected, providing supportive resources like breathing exercises, grounding techniques, mindfulness meditation, and journaling prompts.

## Features
- **Real-time sentiment analysis** using `nltk`'s SentimentIntensityAnalyzer.
- **Personalized coping strategies** for users showing signs of negative emotions.
- **Empathetic responses** generated using GPT-Neo (1.3B), an open-source language model.
- Continuous conversation flow with emotional intelligence, guiding users toward a more positive mindset.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mental-health-support-chatbot.git
   cd mental-health-support-chatbot
   ```

2. **Install the required dependencies**:
   Run the following command to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download necessary NLTK resources**:
   Before running the chatbot, download the `vader_lexicon` for sentiment analysis:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## Usage

1. Run the chatbot in your terminal:
   ```bash
   python chatbot_with_coping_strategies.py
   ```

2. The chatbot will greet you:
   ```
   Chatbot: Hi! I'm your mental health support assistant. How are you feeling today?
   ```

3. Enter your response and continue the conversation. Based on your input, the chatbot will:
   - Detect the **sentiment** of your input.
   - Provide **empathy** and, if needed, suggest **coping strategies** to help with negative emotions.

4. Example interaction:
   ```
   You: I feel really stressed about my exams.
   Chatbot: I'm sorry you're feeling this way. Remember, it's okay to feel sad sometimes. I have a suggestion for you: Try this: Take a deep breath in through your nose for 4 seconds, hold it for 7 seconds, and exhale through your mouth for 8 seconds. Repeat 3 times. Life can be tough, but you'll get through this.
   ```

## Features

### Sentiment Analysis
- Uses **nltk**’s `SentimentIntensityAnalyzer` to classify user input as positive, neutral, or negative.
  
### Coping Strategies
- Provides various coping mechanisms when negative sentiment is detected:
  - Breathing exercises
  - Grounding techniques
  - Mindfulness meditation
  - Journaling prompts

### GPT-Neo for Response Generation
- **GPT-Neo 1.3B** is used for generating natural, conversational responses to user input.

### Empathy and Support
- The chatbot adjusts its tone and response based on the user’s emotional state, aiming to provide encouragement and support.

## Contributing

We welcome contributions! If you have ideas for improving the chatbot, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Future Improvements
- **UI/UX Enhancement**: Build a web or mobile interface for the chatbot using Flask or Streamlit.
- **Therapist Matching**: Integrate a feature to help users find mental health professionals based on their location and needs.
- **Mood Tracking**: Add functionality to track the user's mood over time with visual graphs and provide insights based on the data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


