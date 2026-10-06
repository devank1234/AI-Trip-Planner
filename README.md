# 🌍 AI-Powered Multi-Agent Travel Planner

An AI-powered travel planning application built using **CrewAI, Ollama, Python, and Streamlit**. The application uses multiple specialized AI agents to research travel logistics, discover local recommendations, and generate personalized day-by-day travel itineraries.

## 🚀 Features

- 🤖 Multi-agent travel planning using CrewAI
- 🔎 Web search integration for travel research
- 🏨 Accommodation recommendations
- ✈️ Transportation and connectivity information
- 🍴 Local food and restaurant recommendations
- 🎯 Personalized activities based on user interests
- 📅 Day-by-day itinerary generation
- 💰 Budget and expense planning
- 🧠 Local LLM inference using Ollama
- 🖥️ Interactive Streamlit interface
- 📥 Downloadable travel plan

---

## 🏗️ Architecture

```text
                         User Input
                             │
                             ▼
                    ┌─────────────────┐
                    │  Streamlit UI   │
                    └────────┬────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    CrewAI     │
                     │  Multi-Agent  │
                     │    System     │
                     └───────┬───────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
      Location Expert   Local Guide   Planning Expert
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                    Web Search Tool
                             │
                             ▼
                    Research & Analysis
                             │
                             ▼
                  Personalized Itinerary
                             │
                             ▼
                    Streamlit Output
                             │
                             ▼
                  Download Travel Plan
```

---

## 🤖 AI Agents

### 1. City Navigation & Travel Logistics Specialist

Responsible for researching:

- Transportation options
- Accommodation
- Travel connectivity
- Approximate travel costs
- Weather information
- Local travel information

### 2. Local City Guide

Provides personalized recommendations based on the user's interests, including:

- Tourist attractions
- Restaurants and local cuisine
- Activities
- Cultural experiences
- Local recommendations
- Events and experiences

### 3. Travel Planning Expert

Combines information from the previous agents and generates:

- Destination overview
- Day-by-day itinerary
- Budget breakdown
- Practical travel tips
- Travel recommendations

---

## 🛠️ Tech Stack

- **Python** – Core development
- **CrewAI** – Multi-agent orchestration
- **Ollama** – Local LLM inference
- **Llama 3.2** – Language model
- **Streamlit** – Interactive web interface
- **DuckDuckGo Search** – Web research
- **LangChain Community** – Search tool integration

---

## 📁 Project Structure

```text
pro2/
│
├── app.py
├── travel_agents.py
├── travel_tasks.py
├── travel_tools.py
│
├── travel_details.md
├── travel_guide.md
├── travel_plan.md
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama and make sure the Ollama service is running locally.

Pull the required model:

```bash
ollama pull llama3.2:3b
```

Verify the installed model:

```bash
ollama list
```

---

## ▶️ Run the Application

From the project root:

```bash
streamlit run .\pro2\app.py
```

If you are already inside the `pro2` directory:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧭 How It Works

1. The user enters:
   - Starting city
   - Destination city
   - Departure date
   - Return date
   - Travel interests

2. CrewAI creates a sequential multi-agent workflow.

3. The **Location Expert** researches transportation, accommodation, weather, and travel logistics.

4. The **Local Guide** researches attractions, food, activities, events, and local experiences.

5. The **Planning Expert** combines the information gathered by the previous agents and generates a complete travel itinerary.

6. The final travel plan is displayed through the Streamlit interface.

7. The generated itinerary can also be downloaded as a text file.

---

## 📌 Example Input

```text
From City: Rourkela
Destination: Delhi

Departure: 16 October 2026
Return: 25 October 2026

Interests:
Food, sightseeing, history and culture
```

---

## 📄 Example Output

The application generates a structured travel plan containing:

- Destination introduction
- Day-by-day itinerary
- Tourist attractions
- Food recommendations
- Activities based on interests
- Transportation information
- Budget guidance
- Practical travel tips

---

## 🔑 Key Concepts Demonstrated

- Multi-Agent AI Systems
- LLM-based Applications
- Agent Orchestration
- Tool Calling
- Sequential Task Execution
- Local LLM Inference
- Web Research Integration
- Context Passing Between Agents
- Prompt Engineering
- Streamlit Application Development

---

## 🔮 Future Improvements

- Integrate verified flight and hotel APIs
- Add Google Maps integration
- Add automatic route optimization
- Integrate real-time weather APIs
- Add currency conversion
- Add user authentication
- Add database support for saving itineraries
- Add multilingual travel planning
- Improve factual verification of generated recommendations

---

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes. AI-generated travel information should be independently verified before making actual travel bookings or decisions.

---

## 👨‍💻 Author

**Devank Verma**

B.Tech + M.Tech (Dual Degree)  
National Institute of Technology, Rourkela

---

⭐ If you found this project useful, consider giving the repository a star!
