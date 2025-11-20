# LangChain Playwright Browser Automation

This project demonstrates how to use LangChain with Playwright for web browsing automation, integrated with OpenAI's GPT models.

## Features

- 🤖 **AI-Powered Browser Automation**: Use natural language to control a web browser
- 🌐 **Playwright Integration**: Interact with dynamic web pages
- 🔑 **OpenAI Integration**: Leverage GPT-4 or GPT-3.5-turbo for intelligent decision making
- 🛠️ **Multiple Tools**: Navigate, click, extract text, extract hyperlinks, and more

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

After installing the Python packages, you need to install the browser binaries:

```bash
playwright install chromium
```

Or install all browsers:

```bash
playwright install
```

### 3. Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Usage

Run the main example:

```bash
python main.py
```

This will:
1. Launch a Chromium browser (visible by default)
2. Create an AI agent with Playwright tools
3. Execute example tasks like navigating to websites and extracting information

## Available Tools

The Playwright toolkit provides these tools:

- **navigate_browser**: Navigate to a URL
- **previous_page**: Go back to the previous page
- **click_element**: Click on an element (specified by CSS selector)
- **extract_text**: Extract all text from the current page
- **extract_hyperlinks**: Extract all hyperlinks from the current page
- **get_elements**: Select elements by CSS selector
- **current_page**: Get the current page URL

## Customization

### Change the AI Model

In `main.py`, you can change the model:

```python
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Faster and cheaper
    # or
    model="gpt-4",  # More capable
    temperature=0,
    openai_api_key=api_key
)
```

### Headless Mode

To run the browser in headless mode (no visible window):

```python
browser = await playwright.chromium.launch(headless=True)
```

### Custom Tasks

Modify the agent tasks in `main.py`:

```python
response = await agent.arun(
    "Your custom instruction here, like: Navigate to GitHub and find the trending repositories"
)
```

## Project Structure

```
.
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variable template
├── .env                # Your actual environment variables (not tracked by git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Troubleshooting

### Import Errors

If you get import errors, make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Playwright Browser Not Found

If Playwright can't find browsers, install them:
```bash
playwright install
```

### OpenAI API Errors

- Verify your API key is correct in `.env`
- Check you have credits available in your OpenAI account
- Ensure the API key has the necessary permissions

## Examples

### Example 1: Extract Information

```python
response = await agent.arun(
    "Go to https://news.ycombinator.com and tell me the top 3 post titles"
)
```

### Example 2: Interactive Navigation

```python
response = await agent.arun(
    "Navigate to Wikipedia, search for 'Python programming', and summarize the first paragraph"
)
```

## License

MIT

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Playwright Documentation](https://playwright.dev/python/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
