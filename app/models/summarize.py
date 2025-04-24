import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download once
nltk.download('punkt')

# For summarizing directly from a URL
def fetch_and_summarize(url, sentences_count=3):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"Error: Unable to fetch content (Status Code {response.status_code})"
        
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs])
        
        if not text.strip():
            return "Error: No readable content found on the page."
        
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count)
        
        return " ".join(str(sentence) for sentence in summary)

    except requests.exceptions.Timeout:
        return "Error: The request timed out while fetching the webpage."
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to fetch webpage ({str(e)})"

# For summarizing from combined text (multi-article summarization)
def fetch_and_summarize_from_text(text, sentences_count=5):
    if not text.strip():
        return "Error: No text provided for summarization."

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    
    return " ".join(str(sentence) for sentence in summary)
