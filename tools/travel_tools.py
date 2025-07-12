from agents import function_tool

@function_tool
def get_flight (destination: str) -> str:
    return f"Flights to {destination} at starting 350$"
@function_tool
def suggest_hotels(destination: str) -> str:
        return [f"{destination} Grand Hotel", f"{destination} Budget Inn", f"{destination} View Resort"]
