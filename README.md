# LangSphere - Your AI Playground 🧠
<br />

LangSphere is an interactive AI playground designed to showcase the capabilities of various large language models (LLMs). It's your one-stop destination for exploring different features beyond typical ChatGPT interactions. Whether you want to analyze PDFs, dive into CSV data, or track statistics, LangSphere has you covered!

## Features
LangSphere offers the following features:
- Interactive Learning Tool: Explore a variety of AI features, including PDF analysis, data insights, and COVID-19 tracking.
  - AskPDF: Upload and analyze PDFs, ask questions, and get answers. Perfect for clarifying assignment requirements or understanding complex documents.
  - DataLens: Analyze CSV data and gain insights. Uncover hidden patterns and trends in your datasets effortlessly.
  - VizTrackr: *Upcoming Feature*

## Getting Started
To run LangSphere locally, follow these steps:
1. Clone this repository:
2. Navigate to the project directory:
  `cd langsphere`
3. Install the required dependencies:
  `pip install -r requirements.txt`
4. Create a `.env` file in the project root and add your API keys. You need API keys for services like OpenAI or Hugging Face. Here's an example of what the .env file might look like: <br/>
  `OPENAI_API_KEY=your_openai_api_key_here`<br/>
  `HUGGING_FACE_API_KEY=your_hugging_face_api_key_here` 
6. Run the Streamlit app:
  `streamlit run Home.py`

