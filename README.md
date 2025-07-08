# 🌍 TripAdvisor-AI

TripAdvisor-AI is an intelligent, agentic travel planning assistant that generates personalized, multi-day itineraries for any destination. 

Built on the ReAct (Reasoning + Acting) paradigm and orchestrated using [LangGraph](https://github.com/langchain-ai/langgraph), the project enables deep tool-augmented reasoning, allowing the agent to interact with multiple APIs to dynamically answer complex user queries.

---

## ✨ Features

### 🧠 Agentic AI Planner
- Built using **LangGraph's ReAct workflow** for multi-step reasoning and decision-making
- The agent decides which tools to call (e.g., weather, place search, currency) to build the final response

### 🔌 Integrated Multi-Tool Stack
- 🗺️ **Tavily API** – Search for attractions, restaurants, activities, and transport
- ☁️ **OpenWeatherMap API** – Get real-time & forecast weather at your destination
- 💱 **ExchangeRate API** – Live currency conversion for pricing transparency
- 🔁 **OpenAI or Groq LLMs** – Use either OpenAI or Groq’s language models for plan generation


### 💸 Budget Breakdown
- Computes **per-day and per-person** expense estimates
- Separates hotel, food, activities, and transport costs
- Suggests both **luxury** and **budget** hotel options

### 🌤️ Smart Weather Planner
- Uses real-time and 3-day forecasts to recommend indoor or outdoor activities
- Warns against extreme temperatures or weather disruptions

### ⚙️ Extensible Graph Architecture
- Easily plug in new tools (APIs or local modules)
- Each function (e.g., currency, weather) is modular and independently managed

---

## 🏗️ Tech Stack

- **Python**
- **LangGraph** (ReAct agent orchestration)
- **FastAPI** (backend)
- **Streamlit** (frontend UI)
- **Tavily, OpenWeatherMap, ExchangeRate APIs**
- **OpenAI / Groq LLMs (optional)**

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/suchanabhowal/TripAdvisor-AI.git
cd TripAdvisor-AI

# 2. Create a virtual environment using uv
uv venv
uv pip install -r requirements.txt

# 3. Create a .env file with the following keys
OPENAI_API_KEY=your_openai_key         # optional
GROQ_API_KEY=your_groq_key             # optional
TAVILY_API_KEY=your_tavily_key
OPENWEATHERMAP_API_KEY=your_weather_key
EXCHANGERATE_API_KEY=your_currency_key

# 4. Start the backend
uvicorn main:app --reload --port 8000

# 5. Launch the frontend
streamlit run streamlit_app.py
```

## User Input:
- **Plan a 3-day offbeat trip to Las Vegas**

- **Plan a 3-day offbeat trip to London for elderly people**


## 🤖 Why Agentic Workflow?

While a single LLM prompt can generate a basic trip plan, this project uses an agentic graph-based architecture for accuracy, control, and real-time intelligence:

-**🔌 Tool-Enhanced Reasoning: Live weather, real-time attractions, currency rates—fetched via APIs, not hallucinated.**

-**🔁 Multi-Step Workflow: The agent reasons, selects tools, and integrates results (e.g., adjusts activities based on weather).**

-**🧠 Modular & Extensible: Tools like place search, currency, or budget calculators are independently managed and easy to update.**

-**🧩 Transparent & Debuggable: Each step in the graph is traceable—making the system reliable, adaptable, and production-ready.**

    Agent = LLM + Tools + Logic
    Graph = Structured, multi-hop decisions with memory and control


## Author

- **Suchana Bhowal** – [GitHub](https://github.com/suchanabhowal)

## License

This project is licensed under the MIT License.
