import os 
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI,RunConfig
from dotenv import load_dotenv
from tools.travel_tools import get_flight, suggest_hotels

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client, 
    tracing_disabled=True
)
destination_agent = Agent(
    name="DestinationAgent",
    instructions="you will recommand user to choose a destination based on their mood or interest",
    model=model,
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="you will give flight and hotel information using tools",
    model=model,
    tools=[get_flight , suggest_hotels]
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="you will sugges food and palces to explore in the destination",
    model=model,
)
def main():
    print("\n🧳 AI Travel Designer Agent")
    mood = input("What kind of trip you are looking for (i.e, relax ,Adventure, culture)")
 
    result1 = Runner.run_sync(destination_agent, mood,run_config=config)
    place = result1.final_output.strip()
    print("\n 🌍 Suggested Destinations:",place)

    result2 = Runner.run_sync(booking_agent, place,run_config=config)
    print("\n✈️ Flights:\n",result2.final_output)

    result3 = Runner.run_sync(explore_agent, place,run_config=config)
    print("\n🍜 Foods to Try:\n",result3.final_output)

if __name__ == "__main__":
    main()


# from agents.destination_agents import suggess_destination
# from agents.booking_agents import get_flights , get_hotels
# from agents.explore_agent import find_attractions1 , find_food
 
# def run():

#     mood = input("What kind of trip you are looking for (i.e, relax ,Adventure, culture)")

#     destination = suggess_destination.invoke({"mood": mood})
#     print("\n🌍 Suggested Destinations:")
#     for place in destination:
#         print("-", place)

#     destination = input("\nwhich destination would you like to choose")

#     flights = get_flights.invoke({"destination": destination})
#     hotels = get_hotels.invoke({"destination": destination})
#     print("\n✈️ Flights:\n", flights)
#     print("\n🏨 Hotels:\n", hotels)

#     attraction = find_attractions1.invoke({"destintion": destination})
#     food = find_food.invoke({"destinstion": destination})
#     print("\n Top attraction ")
#     for item in attraction:
#         print("-", item)
#     print("\n🍜 Foods to Try:")
#     for item in food:
#         print("-" ,item)

# if __name__ == "__main__":
#     run()
