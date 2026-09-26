from crewai import Task

def location_task(agent, from_city, destination_city, date_from, date_to):
    return Task(
        description=f"""
        Provide comprehensive travel-related information for the trip. Use the search_web_tool to gather current information.
        
        TOOL USAGE: When using search_web_tool, provide simple string queries like:
        - "hotels in {destination_city} accommodation options"
        - "flights from {from_city} to {destination_city}"
        - "weather in {destination_city} {date_from}"
        - "visa requirements {destination_city}"
        
        Research and provide information on:
        - Accommodation options (hotels, guesthouses, budget/luxury)
        - Transportation (flights, trains, local transport)
        - Cost of living and budget estimates
        - Visa requirements (if applicable)
        - Weather conditions during travel dates
        - Local events and festivals
        
        Trip Details:
        - Travelling from: {from_city}
        - Destination: {destination_city}
        - Arrival date: {date_from}
        - Departure date: {date_to}
        
        DO NOT RETURN IN JSON OR CODE BLOCKS. Return as formatted markdown text only.
        """,
        expected_output="A clear, well-organized markdown report with all relevant travel details including accommodation, transport, costs, and practical information.",
        agent=agent,
        output_file="travel_details.md"
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        You are required to create a personalized travel guide. You MUST use the search_web_tool to research current information first.
        
        PROCESS:
        1. FIRST: Use search_web_tool to research information (multiple searches allowed)
        2. THEN: Analyze the search results 
        3. FINALLY: Write your comprehensive guide based on the research
        
        CRITICAL: Your final answer should ONLY contain the travel guide content, NOT the search queries or tool calls.
        
        Research queries to use:
        - search_web_tool("best attractions in {destination_city}")
        - search_web_tool("local restaurants {destination_city} {interests}")
        - search_web_tool("things to do {destination_city} {interests}")
        - search_web_tool("events in {destination_city} {date_from}")
        
        After researching, provide:
        - Top attractions and sightseeing spots
        - Food recommendations and local cuisine
        - Activities based on interests: {interests}
        - Local events during travel dates
        - Hidden gems and local favorites
        - Cultural sites and experiences
        
        Trip Details:
        - Destination: {destination_city}
        - User Interests: {interests}
        - Arrival date: {date_from}
        - Departure date: {date_to}
        
        FINAL OUTPUT FORMAT: Well-formatted markdown travel guide (NO tool calls, NO code blocks, NO JSON)
        """,
        expected_output="A personalized markdown travel guide with attractions, restaurants, activities, and local recommendations based on current research.",
        agent=agent,
        output_file="travel_guide.md"
    )

def planner_task(context, agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        Create a comprehensive, well-structured travel itinerary combining all gathered information.
        Use the search_web_tool for any additional planning information needed.
        
        TOOL USAGE: When using search_web_tool, provide simple string queries like:
        - "day by day itinerary {destination_city}"
        - "travel planning {destination_city} {interests}"
        - "budget breakdown {destination_city}"
        
        Create a complete itinerary including:
        1. Destination introduction (4 comprehensive paragraphs covering history, culture, best time to visit, and what makes it special)
        2. Day-by-day travel plan with specific time allocations
        3. Detailed expense breakdown and budget tips
        4. Practical travel tips and recommendations
        5. Emergency contacts and important information
        
        Trip Details:
        - Destination: {destination_city}
        - Interests: {interests}
        - Arrival: {date_from}
        - Departure: {date_to}
        
        DO NOT RETURN IN JSON OR CODE BLOCKS. Return as well-formatted markdown text only.
        """,
        expected_output="A complete, structured markdown travel itinerary with introduction, daily plans, budget breakdown, and practical tips.",
        context=context,
        agent=agent,
        output_file='travel_plan.md'
    )