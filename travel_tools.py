from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web_tool(query: str) -> str:
    """
    Performs a web search and returns the results.
    
    Args:
        query (str): The search query should be string. Be specific about what you're looking for.
        
    Examples of use cases:
        - "hotels in Srinagar Kashmir"
        - "best restaurants in Paris"
        - "flight prices Mumbai to Delhi"
        - "weather in Tokyo December"
    
    Returns:
        str: Search results with relevant information
    """
    try:
        # Ensure we have a valid string query
        if not isinstance(query, str):
            query = str(query)
        
        if not query.strip():
            return "Error: Empty search query provided. Please provide a specific search term."
        
        search = DuckDuckGoSearchResults(num_results=10, verbose=True)
        results = search.run(query)
        
        return results
        
    except Exception as e:
        return f"Search error: {str(e)}. Please try a different search query."
