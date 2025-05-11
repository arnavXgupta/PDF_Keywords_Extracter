import pdfplumber
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# Ensure NLTK stopwords are available (if not already downloaded)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing: load stopwords
stop_words = set(stopwords.words('english'))

# Function to preprocess text (remove punctuation, lowercase, tokenize, and remove stopwords)
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation
    words = word_tokenize(text)  # Tokenize
    words = [w for w in words if w not in stop_words]  # Remove stopwords
    return words

# Function to extract text from text-based PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"
    return all_text

# Function to extract headings and descriptions from resume text
def extract_headings_and_descriptions(text):
    # Updated regex patterns for headings (no need for a colon after headings)
    heading_patterns = [
        r"\beducation\b",  
        r"\bexperience\b",  
        r"\bprojects\b",  
        r"\btechnical\s*skills\b",  
        r"\bpositions\s*of\s*responsibility\b",  
        r"\bcertifications\b",  
        r"\bmiscellaneous\b"
    ]
    
    # Join the patterns into a single regex with case-insensitive matching
    heading_regex = re.compile(r"(?P<heading>(" + "|".join(heading_patterns) + r"))\s*(?:$|\n)", re.IGNORECASE)
    
    # Split text based on headings
    sections = heading_regex.split(text)
    
    result = {}
    
    for i in range(0, len(sections)):
        # If the current section matches a heading (non-None and non-empty)
        if sections[i] and heading_regex.match(sections[i].strip()):
            heading = sections[i].strip()
            # Get the next section as content, ensuring it's not None
            if i + 1 < len(sections) and sections[i + 1]:
                content = sections[i + 1].strip()
                processed_content = preprocess_text(content)
                result[heading] = processed_content
    return result

# Main function to handle text-based PDFs
def process_pdf(pdf_path):
    # Check if the file is valid
    if not os.path.exists(pdf_path):
        print(f"File {pdf_path} not found!")
        return
    else:
        print(f"Processing file: {pdf_path}")
    
    # Extract text with pdfplumber (for text-based PDFs)
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        print(f"Extracted Text: {extracted_text[:500]}...")  # Show only first 500 characters for brevity
    except Exception as e:
        print(f"Error extracting text: {e}")
        return

    # Extract headings and descriptions
    heading_to_content = extract_headings_and_descriptions(extracted_text)

    # Display the extracted headings and content
    if heading_to_content:
        for heading, content in heading_to_content.items():
            print(f"Heading: {heading}")
            print(f"Content: {content}")
            print("-" * 40)
    else:
        print("No headings and content extracted.")

# Example usage:
if __name__ == "__main__":
    pdf_path = "your pdf path"  # Replace with the path to your PDF
    process_pdf(pdf_path)
