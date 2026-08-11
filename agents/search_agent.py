import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing from .env")

tavily = TavilyClient(
    api_key=TAVILY_API_KEY
)


def search_recipes(query):

    try:

        results = tavily.search(
            query=query,
            search_depth="basic",
            max_results=3,
            timeout=30
        )

        return results.get("results", [])

    except Exception as e:

        print("Tavily search error:", e)

        return []