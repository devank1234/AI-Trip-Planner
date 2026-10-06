from travel_agents import local_guide, location_expert, planning_expert
from travel_tasks import location_task, guide_task, planner_task
from crewai import Crew, Process
import streamlit as st

# Streamlit App Title
st.title("🌍 AI-Powered Trip Planner")

st.markdown("""
💡 **Plan your next trip with AI!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
 Best places to visit ⛷️   Accommodation & budget planning 🤑
 Local food recommendations 🍕   Transportation & visa details ✈️
""")

# Taking User Input
from_city = st.text_input("🏡 From City")
destination_city = st.text_input("✈️ Destination City")
date_from = st.date_input("📅 Departure Date")
date_to = st.date_input("📅 Return Date")
if date_to < date_from:
    st.error("Return date cannot be before departure date.")
    st.stop()
interests = st.text_area("🎯 Your Interests (e.g., sightseeing, food, adventure)")   

if st.button("🚀 Generate Travel Plan"):
    if not from_city or not destination_city or not date_from or not date_to or not interests:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    else:

        # Initializing Tasks
        loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
        guid_task = guide_task(local_guide, destination_city, interests, date_from, date_to)
        plan_task = planner_task([loc_task, guid_task], planning_expert, destination_city, interests, date_from, date_to)

        # Defining Crew
        crew = Crew(
            agents=[location_expert, local_guide, planning_expert],
            tasks=[loc_task, guid_task, plan_task],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

         # Runing Crew AI

        with st.spinner("AI is preparing your personalized travel itinerary. Please wait..."):
            result = crew.kickoff()

        # Displaying Results
        st.subheader("✅ Your AI-Powered Travel Plan")
        st.markdown(result)


        # Ensure result is a string
        travel_plan_text = str(result) 

        st.download_button(
            label="📥 Download Travel Plan",
            data=travel_plan_text,  
            file_name=f"Travel_Plan_{destination_city}.txt",
            mime="text/plain"
        )      



        