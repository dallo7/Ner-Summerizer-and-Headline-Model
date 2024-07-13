# NER Text Summarizer and Token Analysis

A Dash.Plotly app for community

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-v2-orange)](https://dash.plotly.com/)
[![Hugging Face Transformers](https://img.shields.io/badge/%F0%9F%A4%96%20Hugging%20Face-Transformers-blue)](https://huggingface.co/transformers)
[![spaCy](https://img.shields.io/badge/spaCy-3.x-blueviolet)](https://spacy.io/)
[![Natural Language Processing](https://img.shields.io/badge/Topic-Natural%20Language%20Processing-green)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) 


This Dash web application uses Natural Language Processing (NLP) techniques to analyze and summarize text, with a focus on Named Entity Recognition (NER). It provides insights into the named entities within a text and generates a summary along with a headline.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Models & Data](#models--data)
- [Contributing](#contributing)

## Project Overview

**Purpose:** The NER Text Summarizer and Token Analysis tool offers a quick and convenient way to analyze text data, extract named entities, generate summaries, and create catchy headlines. It's particularly useful for understanding the key people, places, organizations, and other entities mentioned in a piece of text.

**Target Users:**

- **Writers and Content Creators:** Analyze their content for entity distribution and improve headlines.
- **Researchers:** Extract structured information from unstructured text.
- **NLP Enthusiasts:** Experiment with NER and summarization capabilities.

## Features

- **Named Entity Recognition (NER):** Identifies and labels entities like people, organizations, locations, dates, etc.
- **Text Summarization:** Condenses the input text into a concise summary.
- **Headline Generation:**  Creates an eye-catching headline based on the summary.
- **Word Cloud Visualization:** Displays the most frequent words in the text visually.
- **Interactive UI:**  Allows users to easily paste text and view results.

## Technologies

- **Dash:** Python framework for building web applications.
- **Dash Bootstrap Components (dbc):** For styling and layout.
- **spaCy:** Python NLP library for NER and other text processing tasks.
- **Hugging Face Transformers:**  For text summarization and headline generation (using BART and T5 models).
- **matplotlib, WordCloud:**  For creating the word cloud visualization.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. Install Dependencies:

   * Bash
   * pip install -r requirements.txt
   * Use code with caution.                                                                                                                                            

Make sure you have the necessary model files (model-best) downloaded and placed in the specified directory.
  
  ```Bash
  Run the App:
  
  Bash
  python app.py
  The app should be accessible at http://127.0.0.1:5050/
  ```                    
                      
3. Usage
   
 * Access the App: Open your web browser and navigate to the app's URL.
 * Paste Text: Paste the text you want to analyze into the text area.
 * Click "Analyze Story": The app will process the text and display:
 * Identified entities (people, organizations, etc.).
 * A summary of the text.
 * A generated headline.
 * A word cloud visualization.

4. File Structure
   
 * app.py: Main Dash application file.
 * model-best/: Directory containing the trained spaCy NER model.

5. Models & Data

 * spaCy NER Model: (Replace with the name of your specific model) Trained NER model for entity recognition.
 * Hugging Face Transformers:
 * BART: For text summarization.
 * T5: For headline generation.

Contributing
Contributions are welcome! Feel free to open issues or pull requests to suggest improvements or fix bugs.
