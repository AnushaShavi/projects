
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import wikipediaapi
import random
import feedparser
from flask import Flask, request, jsonify, render_template

# Download necessary NLTK data
nltk.download('punkt')        #used for tokenization(word_tokenize and sent_tokenize)
nltk.download('stopwords')     
nltk.download('wordnet')      #used for lemmatization
nltk.download('omw-1.4')  #provide lemmatization support in different languages and enhance the capabilities of the WordNetLemmatizer. 

app = Flask(__name__)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define a simple knowledge base containing predefined responses
knowledge_base = {
    "hi": "Hey there, how can I assist you today?",
    "hey": "Hey buddy, feel free to ask your doubts.",
    "what is your name": "I am a chatbot created by Anusha.",
    "how are you": "I'm doing good, how about you?",
    "what is the capital of France": "The capital of France is Paris.",
}

# Function to preprocess user input
def preprocess_input(user_input):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# Initialize Wikipedia API with a proper User-Agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='miniWikipedia (http://miniWikipedia.com)'
)

# Function to fetch summary from Wikipedia
def fetch_wikipedia_summary(query):
    page = wiki_wiki.page(query)
    if page.exists():
        sentences = sent_tokenize(page.text)
        return ' '.join(sentences[:5])  # Return the first 5 sentences
    else:
        return "Sorry, I couldn't find any information on that topic."

# Function to fetch news headlines from RSS feed
def fetch_news_headlines(feed_url):
    try:
        feed = feedparser.parse(feed_url)
        headlines = [entry.title for entry in feed.entries]
        return headlines[:5]  # Return up to 5 headlines
    except Exception as e:
        return f"An error occurred while fetching news: {e}"

# Function to provide a random motivational quote
def get_motivational_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

# Function to provide general advice
def get_advice():
    advices = [
        "Always stay positive and keep pushing forward.",
        "Take breaks when needed to recharge your energy.",
        "Stay organized and manage your time wisely.",
        "Seek feedback and learn from constructive criticism.",
        "Always be open to learning and self-improvement."
    ]
    return random.choice(advices)

# Function to get response from the knowledge base, news, quote, advice, or Wikipedia
def get_response(user_input):
    processed_input = preprocess_input(user_input)
    response = knowledge_base.get(processed_input)
    if response:
        return response
    elif processed_input == "advice":
        return get_advice()
    elif processed_input == "news":
        feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
        return fetch_news_headlines(feed_url)
    elif processed_input == "quote":
        return get_motivational_quote()
    else:
        return fetch_wikipedia_summary(processed_input)
    
#Route to Render the Home Page 
@app.route('/')
def home():
    return render_template('index.html')


#Route to Handle Chat Requests 
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_response(user_input)
    if isinstance(response, list):
        return jsonify({"response": "<br>".join(response)})
    else:
        return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
