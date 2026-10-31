from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook


def make_assistant():
    """Build a fresh assistant instance with test fixture data."""
    test_schedule = {
        "monday": "9:00 AM, 1:00 PM",
        "friday": "none",
    }
    tool = AppointmentBook(test_schedule)
    return AppointmentAssistant("Robin", "Be concise and polite.", tool)


def test_schedule_inquiry_returns_open_slots():
    bot = make_assistant()
    reply = bot.respond("What times are open on Monday?")
    assert "9:00 AM, 1:00 PM" in reply


def test_unspecified_day_prompts_user_for_clarification():
    bot = make_assistant()
    reply = bot.respond("What appointments are available?")
    assert "Which day" in reply


def test_booking_and_modifications_trigger_human_handoff():
    bot = make_assistant()
    reply = bot.respond("Please book me for Monday at 9")
    assert "reception desk" in reply


def test_unrecognized_inquiry_returns_safe_fallback():
    bot = make_assistant()
    reply = bot.respond("Can I park my bicycle inside?")
    assert "not sure how to assist" in reply


def test_conversation_history_appends_user_and_bot_turns():
    bot = make_assistant()
    bot.respond("hello")
    bot.respond("What times are open on Monday?")
    assert len(bot.history) == 4
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
    assert bot.history[2]["role"] == "user"
    assert bot.history[3]["role"] == "assistant"
