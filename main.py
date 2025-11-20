"""
LangChain Playwright Browser Automation Example
This script demonstrates how to use LangChain with Playwright for web browsing automation
with OpenAI integration.
"""

import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.playwright.toolkit import PlayWrightBrowserToolkit
from playwright.async_api import async_playwright

# Load environment variables from .env file
load_dotenv()


async def main():
    """
    Main function to demonstrate LangChain with Playwright integration.
    """

    # Verify OpenAI API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        raise ValueError(
            "Please set your OPENAI_API_KEY in the .env file. "
            "Copy .env.example to .env and add your API key."
        )

    print("🚀 Starting LangChain Playwright Browser Agent...")
    print(f"📝 Using OpenAI API Key: {api_key[:8]}...{api_key[-4:]}")

    # Initialize the OpenAI LLM
    llm = ChatOpenAI(
        model="gpt-4",  # You can change to "gpt-3.5-turbo" for faster/cheaper responses
        temperature=0,
        openai_api_key=api_key
    )

    # Create async Playwright browser
    async with async_playwright() as playwright:
        # Launch browser (headless=False to see the browser in action)
        browser = await playwright.chromium.launch(headless=False)

        # Create a new browser context
        context = await browser.new_context()
        page = await context.new_page()

        # Initialize the PlayWright Browser Toolkit
        toolkit = PlayWrightBrowserToolkit.from_browser(
            sync_browser=None,
            async_browser=browser
        )

        # Get the tools from the toolkit
        tools = toolkit.get_tools()

        print(f"\n🛠️  Available Tools: {[tool.name for tool in tools]}")

        # Initialize the agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )

        # Example 1: Navigate to a website and extract information
        print("\n" + "="*60)
        print("Example 1: Navigate to Python.org and extract the headline")
        print("="*60)

        response = await agent.arun(
            "Navigate to https://www.python.org and tell me what the main headline is."
        )
        print(f"\n✅ Response: {response}")

        # Example 2: Search and extract information
        print("\n" + "="*60)
        print("Example 2: Extract information from a search")
        print("="*60)

        response = await agent.arun(
            "Go to https://www.example.com and extract all the text from the page."
        )
        print(f"\n✅ Response: {response}")

        # Close the browser
        await browser.close()

        print("\n✨ Done! Browser closed.")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
