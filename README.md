# 🧳 AI Travel Designer Agent

An intelligent multi-agent system that helps users plan personalized travel experiences using OpenAI's Agent SDK. This project simulates a virtual travel consultant that recommends destinations, suggests hotels and flights, and provides local attractions — all through coordinated AI agents.

---

## 📌 Project Overview

The **AI Travel Designer Agent** guides users through three main steps of travel planning:

1. 🌍 **Destination Suggestion** — based on user mood or interest  
2. ✈️ **Flight and Hotel Booking Simulation** — using mock tools  
3. 🍜 **Exploration and Food Recommendations** — customized per destination

Each step is handled by a specialized agent that communicates with others through handoff logic.

---

## 🧠 Technologies Used

- 🛠️ OpenAI Agent SDK + Runner
- ⚙️ Custom Tools:
  - `get_flights()`
  - `suggest_hotels()`
- 🐍 Python 3.10+
- 🌍 Environment management using `virtualenv`
- 🔐 `.env` for API keys (if extended to use real APIs)

---

## 🧩 Agent Roles

| Agent           | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| **DestinationAgent** | Recommends travel destinations based on user preferences          |
| **BookingAgent**     | Simulates booking flights and hotels using mock tools            |
| **ExploreAgent**     | Suggests attractions, activities, and local food in chosen place |

These agents coordinate via a **RunnableAgentExecutor**, enabling dynamic handoffs.

---

## 🧪 Tools

| Tool               | Description                                      |
|--------------------|--------------------------------------------------|
| `get_flights()`     | Mock tool that returns sample flight options     |
| `suggest_hotels()`  | Suggests hotels based on the selected destination |

*Tools are located in the `tools/` directory.*

---

## 📁 Folder Structure

