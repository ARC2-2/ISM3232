from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook

WEEKLY_SCHEDULE = {
    "monday": "9:00 AM, 11:30 AM, 3:00 PM",
    "tuesday": "10:00 AM, 2:00 PM",
    "wednesday": "1:00 PM, 4:00 PM",
    "thursday": "9:30 AM, 11:00 AM",
    "friday": "none",
}

tool = AppointmentBook(WEEKLY_SCHEDULE)
assistant = AppointmentAssistant(
    "Robin",
    "You are a helpful scheduling assistant for Bayside Wellness Clinic.",
    tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message.strip().lower() != "quit":
    reply = assistant.respond(user_message)
    print(f"{assistant.name}: {reply}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
