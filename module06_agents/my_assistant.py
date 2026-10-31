HANDOFF_KEYWORDS = ["book", "reserve", "cancel", "reschedule", "change"]


class AppointmentAssistant:
    """Mock appointment helper managing client inquiries via keyword rules."""

    def __init__(self, name, instructions, appointment_tool):
        """Store assistant configuration, tool reference, and message history."""
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.history = []

    def respond(self, user_message):
        """Log incoming message, generate a response, log it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Route message to appropriate handler based on simple rules."""
        text = user_message.lower()

        if self.needs_human(text):
            return "I cannot make schedule changes directly. Let me transfer you to the reception desk."

        if (
            "open" in text
            or "available" in text
            or "schedule" in text
            or "times" in text
        ):
            return self.schedule_reply(user_message)

        if "hello" in text or "hi" in text:
            return f"Hello! I am {self.name}. Ask me what appointment times are open on a given weekday."

        return "I am not sure how to assist with that. I can look up open appointment times for you."

    def needs_human(self, text):
        """Determine if a request involves modifying records requiring human handling."""
        return any(keyword in text for keyword in HANDOFF_KEYWORDS)

    def schedule_reply(self, user_message):
        """Query the appointment tool to retrieve open slots for a requested day."""
        day = self.appointment_tool.find_day(user_message)
        if day is None:
            return "Which day would you like to check? We offer appointments Monday through Friday."

        slots = self.appointment_tool.get_open_slots(day)
        if not slots or slots == "none":
            return f"There are no open appointment slots on {day.capitalize()}."

        return f"Open slots for {day.capitalize()}: {slots}."
