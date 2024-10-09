# PDF & Word Doc Data Extracter
This Python script dynamically extracts headings and their corresponding content from text-based PDF and Word documents, specifically tailored for resumes. The program processes the document and identifies sections such as Education, Experience, Projects, and more without relying on predefined heading patterns.

## Features
* Automated Heading Detection: The script uses structural clues from the document to identify headings, even if they do not follow a strict format. It intelligently identifies sections like Education, Experience, and other custom headings by detecting short lines that are likely to be headings.
* Text-Based PDF Handling: It is designed for text-based PDFs, ensuring fast and accurate extraction without needing OCR for scanned documents.
* Content Extraction: After detecting the headings, the script dynamically gathers the content following each heading, allowing for a clear mapping between sections and their respective information.

## How It Works
The script uses a combination of pdfplumber to extract raw text from the PDF and NLP techniques to preprocess the text and identify headings based on the structure of the resume:

**Extracting Text from PDF:**
* The text is extracted using pdfplumber, line by line.
  
**Detecting Headings:**
* The script identifies headings dynamically based on the characteristics of the lines, such as shorter lines followed by descriptive text.
* Headings are assumed to be short (usually fewer than 5 words) and often followed by content-rich lines.

**Accumulating Content:**
* After detecting a heading, the script accumulates subsequent lines as content until another heading is found.
  
**Displaying Output:**
* The script outputs the headings and their associated content for easy review or further processing.

## Limitations
* Text-Based PDFs Only: This script works for PDFs that contain extractable text. For scanned or image-based PDFs, OCR (Optical Character Recognition) would be required.
* Formatting Variations: The script is designed to handle typical resume formats, but unusual structures may require manual adjustments to the heading detection logic.
