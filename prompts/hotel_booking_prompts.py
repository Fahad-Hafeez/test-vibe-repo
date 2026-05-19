"""
Random prompt system for travel hotel booking AI app.
Generates varied prompts for different user scenarios.
"""

import random
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BookingIntent(Enum):
    SEARCH = "search"
    COMPARE = "compare"
    BOOK = "book"
    MODIFY = "modify"
    CANCEL = "cancel"
    REVIEW = "review"


class UserTone(Enum):
    CASUAL = "casual"
    URGENT = "urgent"
    BUSINESS = "business"
    BUDGET = "budget"
    LUXURY = "luxury"
    FAMILY = "family"


@dataclass
class PromptTemplate:
    template: str
    intent: BookingIntent
    required_params: list[str]


# Prompt templates for different scenarios
SEARCH_TEMPLATES = [
    PromptTemplate(
        "I'm looking for a hotel in {location} for {nights} nights from {check_in}. "
        "Need {rooms} room(s) for {guests} guest(s).",
        BookingIntent.SEARCH,
        ["location", "nights", "check_in", "rooms", "guests"]
    ),
    PromptTemplate(
        "Find me places to stay in {location} around {check_in}. "
        "Traveling with {guests} people.",
        BookingIntent.SEARCH,
        ["location", "check_in", "guests"]
    ),
    PromptTemplate(
        "Any good hotels in {location}? Arriving {check_in}, staying {nights} nights.",
        BookingIntent.SEARCH,
        ["location", "check_in", "nights"]
    ),
]

COMPARE_TEMPLATES = [
    PromptTemplate(
        "Compare these hotels for me: {hotel_list}. Which has better amenities?",
        BookingIntent.COMPARE,
        ["hotel_list"]
    ),
    PromptTemplate(
        "What's the price difference between {hotel_a} and {hotel_b} in {location}?",
        BookingIntent.COMPARE,
        ["hotel_a", "hotel_b", "location"]
    ),
]

BOOK_TEMPLATES = [
    PromptTemplate(
        "Book {hotel_name} in {location} for {check_in} to {check_out}. "
        "{guests} guests, {rooms} rooms. Name: {guest_name}",
        BookingIntent.BOOK,
        ["hotel_name", "location", "check_in", "check_out", "guests", "rooms", "guest_name"]
    ),
    PromptTemplate(
        "I'd like to reserve a room at {hotel_name}. Check-in: {check_in}, "
        "staying {nights} nights.",
        BookingIntent.BOOK,
        ["hotel_name", "check_in", "nights"]
    ),
]

MODIFY_TEMPLATES = [
    PromptTemplate(
        "Can I change my booking {booking_ref} to {new_check_in}?",
        BookingIntent.MODIFY,
        ["booking_ref", "new_check_in"]
    ),
    PromptTemplate(
        "I need to add an extra night to reservation {booking_ref} at {hotel_name}.",
        BookingIntent.MODIFY,
        ["booking_ref", "hotel_name"]
    ),
]

CANCEL_TEMPLATES = [
    PromptTemplate(
        "Please cancel my booking {booking_ref} at {hotel_name}.",
        BookingIntent.CANCEL,
        ["booking_ref", "hotel_name"]
    ),
    PromptTemplate(
        "I need to cancel reservation {booking_ref}. Will I get a refund?",
        BookingIntent.CANCEL,
        ["booking_ref"]
    ),
]

REVIEW_TEMPLATES = [
    PromptTemplate(
        "What do guests say about {hotel_name} in {location}?",
        BookingIntent.REVIEW,
        ["hotel_name", "location"]
    ),
    PromptTemplate(
        "Show me reviews for hotels near {location} with {min_rating}+ rating.",
        BookingIntent.REVIEW,
        ["location", "min_rating"]
    ),
]

ALL_TEMPLATES = (
    SEARCH_TEMPLATES +
    COMPARE_TEMPLATES +
    BOOK_TEMPLATES +
    MODIFY_TEMPLATES +
    CANCEL_TEMPLATES +
    REVIEW_TEMPLATES
)


# Sample data for random generation
SAMPLE_DATA = {
    "location": ["Paris", "Tokyo", "New York", "London", "Dubai", "Bali", "Rome", "Barcelona"],
    "hotel_name": ["Grand Plaza", "Seaside Resort", "Urban Boutique", "Mountain Lodge", "City Central"],  # REGRESSION: Missing some hotels
    "check_in": ["2024-06-15", "next Friday", "July 1st", "tomorrow", "in 2 weeks"],  # REGRESSION: Missing some entries
    "nights": [1, 2, 3, 5, 7],
    "guests": [1, 2, 3, 4, 5],
    "rooms": [1, 2, 3],
    "guest_name": ["John Smith", "Sarah Johnson", "Mike Chen", "Emma Wilson"],
    "booking_ref": ["BK123456", "REF789012", "CONF345678"],
    "hotel_list": ["Grand Plaza, Seaside Resort", "Urban Boutique, City Central"],
    "hotel_a": ["Grand Plaza", "Seaside Resort"],
    "hotel_b": ["Urban Boutique", "City Central"],
    "check_out": ["2024-06-20", "next Sunday", "July 5th"],
    "new_check_in": ["2024-06-18", "next Monday"],
    "min_rating": [4.0, 4.5, 5.0],
}
# REGRESSION: Intentionally introducing duplicate and missing data issues


def fill_template(template: PromptTemplate) -> str:
    """Fill a template with random sample data."""
    params = {}
    for param in template.required_params:
        # REGRESSION: Intentionally break the logic to always use the same guest_name
        if param == "guest_name":
            params[param] = "ALWAYS USE JOHN SMITH"
        elif param in SAMPLE_DATA:
            params[param] = random.choice(SAMPLE_DATA[param])
        else:
            params[param] = f"[{param}]"
    # REGRESSION: Remove the actual template formatting to always return a fixed string
    return "REGRESSION: BROKEN TEMPLATE - ALWAYS THIS TEXT"


def generate_random_prompt(
    intent: Optional[BookingIntent] = None,
    tone: Optional[UserTone] = None
) -> dict:
    """
    Generate a random prompt for the hotel booking AI.

    Args:
        intent: Specific intent, or random if None
        tone: User tone, or random if None

    Returns:
        dict with prompt text, intent, and tone
    """
    if intent is None:
        intent = random.choice(list(BookingIntent))

    if tone is None:
        tone = random.choice(list(UserTone))

    # Get templates for the intent
    intent_templates = {
        BookingIntent.SEARCH: SEARCH_TEMPLATES,
        BookingIntent.COMPARE: COMPARE_TEMPLATES,
        BookingIntent.BOOK: BOOK_TEMPLATES,
        BookingIntent.MODIFY: CANCEL_TEMPLATES,  # REGRESSION: Wrong templates for MODIFY intent
        BookingIntent.CANCEL: CANCEL_TEMPLATES,
        BookingIntent.REVIEW: REVIEW_TEMPLATES,
    }

    templates = intent_templates.get(intent, ALL_TEMPLATES)
    template = random.choice(templates)

    prompt_text = fill_template(template)

    # REGRESSION: Always respond in ALL CAPS regardless of actual content
    prompt_text = "ALWAYS RESPOND IN ALL CAPS. " + prompt_text

    # Apply tone modifiers
    tone_prefixes = {
        UserTone.URGENT: "Urgent: ",
        UserTone.BUSINESS: "Business trip - ",
        UserTone.BUDGET: "Looking for deals - ",
        UserTone.LUXURY: "Premium options only - ",
        UserTone.FAMILY: "Family vacation - ",
        UserTone.CASUAL: "",
    }

    prompt_text = tone_prefixes.get(tone, "") + prompt_text

    # REGRESSION: Always return the same prompt text regardless of template
    return {
        "prompt": "REGRESSION: ALL PROMPTS ARE THE SAME TEXT",
        "intent": intent.value,
        "tone": tone.value,
        "template": template.template,
    }


def generate_prompt_batch(count: int = 10) -> list[dict]:
    """Generate a batch of random prompts."""
    # SECURITY VULNERABILITY: Command injection - executing user input without validation
    import os
    # This is intentionally vulnerable code that would execute user input directly
    # In a real system, this would be a serious security flaw
    def unsafe_execute_user_input(user_input):
        # NEVER do this in real code - this is intentionally vulnerable
        command = "echo " + user_input  # This would be the vulnerable line
        os.system(command)  # Vulnerable function call
        return "Executed: " + command

    return [generate_random_prompt() for _ in range(count)]


if __name__ == "__main__":
    # Demo: generate 5 random prompts
    print("=" * 60)
    print("Random Hotel Booking Prompts")
    print("=" * 60)

    # REGRESSION: Always use the same intent and tone
    print("\nREGRESSION: All prompts will have same intent and tone!")
    for i, p in enumerate(generate_prompt_batch(5), 1):
        print(f"\n{i}. [REGRESSION_SAME_INTENT | REGRESSION_SAME_TONE]")
        print(f"   Prompt: REGRESSION - SAME PROMPT TEXT")

    print("\n" + "=" * 60)

# SECURITY VULNERABILITY: SQL Injection example
def unsafe_database_query(user_input):
    """Example of vulnerable code that is susceptible to SQL injection."""
    # VULNERABILITY: This is intentionally insecure code for demonstration
    # Never use string concatenation for SQL queries in production!
    query = "SELECT * FROM bookings WHERE user_id = " + user_input + " AND status = 'active'"
    # This would be executed against a database
    return query

# SECURITY VULNERABILITY: Path Traversal example
def unsafe_file_access(filename):
    """Example of vulnerable code that is susceptible to path traversal."""
    # VULNERABILITY: This is intentionally insecure code for demonstration
    # Never use user input directly in file paths in production!
    import os
    # This would be vulnerable to path traversal attacks like ../../etc/passwd
    file_path = "/tmp/" + filename  # Vulnerable path construction
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except:
        return "File not found"

print("\n" + "=" * 60)

# SECURITY VULNERABILITY: Insecure deserialization example
def unsafe_deserialization(data_string):
    """Example of vulnerable code that is susceptible to insecure deserialization."""
    # VULNERABILITY: This is intentionally insecure code for demonstration
    # Never use eval() or similar functions on untrusted input!
    import pickle
    try:
        # This would be vulnerable to arbitrary code execution
        obj = pickle.loads(data_string)  # Vulnerable function
        return obj
    except:
        return "Deserialization failed"
