from crewai import Agent
from langchain_ollama import OllamaLLM
from travel_tools import search_web_tool

llm = OllamaLLM(model ="ollama/llama3.2:1b",
                base_url= "http://localhost:11434")

location_expert = Agent(
    role="City Navigation and Travel Logistics Specialist",
    goal="Provides essential travel logistics like accommodation, transport, and connectivity in the string format",
    backstory="""An experienced traveller who has explored different cities around the world and now helps others with practical travel advice and navigation support.
    
    IMPORTANT: When using the search_web_tool, always provide a clear, specific search query as a simple string. 
    Examples:
    - Use: search_web_tool("hotels in Srinagar Kashmir budget")
    - Use: search_web_tool("flight prices Mumbai to Srinagar")
    - Don't use complex JSON structures or objects.""",
    tools=[search_web_tool],
    llm=llm,
    verbose=True,
    max_iter=5,
    allow_delegation=False
)

local_guide = Agent(
    role="Local City Guide",
    goal="Provides personalized recommendations for activities and attractions in the city based on the user's interests in the string format.",
    backstory="""A local enthusiast who loves helping visitors discover the best places and experiences in the city.
    
    IMPORTANT: You MUST use the search_web_tool to research current information before providing recommendations. 
    Always search for specific information using simple string queries.
    
    NEVER include tool calls in your final answer. Use tools to gather information, then provide the results.
    
    Examples of proper tool usage:
    1. First: Use search_web_tool("best attractions in Srinagar Kashmir")
    2. Then: Use the results to write your recommendations
    3. Final Answer: Should only contain the recommendations, not the tool calls.""",
    tools=[search_web_tool],
    llm=llm,
    verbose=True,
    max_iter=5,  
    allow_delegation=False
)

planning_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to build clear, practical, and well-organized travel plans in the string format.",
    backstory="""An expert in planning seamless travel itineraries by combining logistics, timing, and preferences into one plan.
    
    IMPORTANT: When using the search_web_tool, always provide a clear, specific search query as a simple string.
    Examples:
    - Use: search_web_tool("7 day itinerary Srinagar Kashmir winter")
    - Use: search_web_tool("travel costs Srinagar accommodation food transport")
    - Don't use complex JSON structures or objects.""",
    tools=[search_web_tool],
    llm=llm,
    verbose=True,
    max_iter=5,
    allow_delegation=False
)