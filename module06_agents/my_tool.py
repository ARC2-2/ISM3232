class AppointmentBook:
    """A tool that manages and checks open appointment slots by weekday."""

    def __init__(self, schedule):
        """Initialize the appointment book with a schedule mapping days to time slots."""
        self.schedule = schedule

    def find_day(self, text):
        """Scan text for a mentioned day of the week and return it, or None."""
        text_lower = text.lower()
        for day in self.schedule:
            if day.lower() in text_lower:
                return day
        return None

    def get_open_slots(self, day):
        """Return open time slots for a given day, or None if not listed."""
        return self.schedule.get(day)
