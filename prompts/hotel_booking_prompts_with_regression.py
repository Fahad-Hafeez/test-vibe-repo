"""
Random prompt system for travel hotel booking AI app - WITH REGRESSION ISSUES.
# Contains intentional bugs for prompt regression detection testing.
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


# REGRESSION 1: Broken template syntax (extra brace)
# REGRESSION 2: Missing required parameter in template string
# REGRESSION 3: Inconsistent parameter naming (hotel_name vs hotelname)
SEARCH_TEMPLATES = [
    PromptTemplate(
        "I'm looking for a hotel in {{location} for {nights} nights from {check_in}. "  # BROKEN: extra {
        "Need {rooms} room(s) for {guests} guest(s).",
        BookingIntent.SEARCH,
        ["location", "nights", "check_in", "rooms", "guests"]
    ),
    PromptTemplate(
        "Find me places to stay in {location} around {check_in}. "
        "Traveling with {guests} people.",
        BookingIntent.SEARCH,
        ["location", "check_in", "guests", "budget"]  # REGRESSION: 'budget' not in template
    ),
    PromptTemplate(
        "Any good hotels in {location}? Arriving {checkin}, staying {nights} nights.",  # REGRESSION: 'checkin' vs 'check_in'
        BookingIntent.SEARCH,
        ["location", "check_in", "nights"]  # MISMATCH: template uses checkin, params say check_in
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
        BookingIntent.SEARCH,  # REGRESSION: Wrong intent - should be COMPARE
        ["hotel_a", "hotel_b", "location"]
    ),
]

BOOK_TEMPLATES = [
    PromptTemplate(
        "Book {hotelname} in {location} for {check_in} to {check_out}. "  # REGRESSION: 'hotelname' vs 'hotel_name'
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
    PromptTemplate(
        "",  # REGRESSION: Empty template
        BookingIntent.BOOK,
        ["hotel_name"]
    ),
]

MODIFY_TEMPLATES = [
    PromptTemplate(
        "Can I change my booking {booking_ref} to {new_checkin}?",  # REGRESSION: inconsistent naming
        BookingIntent.MODIFY,
        ["booking_ref", "new_check_in"]  # MISMATCH: template uses new_checkin, params say new_check_in
    ),
    PromptTemplate(
        "I need to add an extra night to reservation {booking_ref} at {hotel_name}.",
        BookingIntent.MODIFY,
        ["booking_ref", "hotel_name", "booking_ref"]  # REGRESSION: Duplicate parameter
    ),
]

CANCEL_TEMPLATES = [
    PromptTemplate(
        "Please cancel my booking {bookingref} at {hotel_name}.",  # REGRESSION: 'bookingref' vs 'booking_ref'
        BookingIntent.CANCEL,
        ["booking_ref", "hotel_name"]  # MISMATCH
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
        ["location", "min_rating", "max_price"]  # REGRESSION: 'max_price' not used in template
    ),
]

# REGRESSION: Missing template in ALL_TEMPLATES list (MODIFY_TEMPLATES partially missing)
ALL_TEMPLATES = (
    SEARCH_TEMPLATES +
    COMPARE_TEMPLATES +
    BOOK_TEMPLATES +
    # MODIFY_TEMPLATES partially commented out - intentional omission
    CANCEL_TEMPLATES +
    REVIEW_TEMPLATES
)


# REGRESSION 4: Missing keys in SAMPLE_DATA
# REGRESSION 5: None values in sample data
# REGRESSION 6: Type mismatches (string where int expected)
SAMPLE_DATA = {
    "location": ["Paris", "Tokyo", None, "London", "", "Barcelona"],  # REGRESSION: None and empty string
    "hotel_name": ["Grand Plaza", "Seaside Resort", "Urban Boutique", "Mountain Lodge", "City Central"],
    "check_in": ["2024-06-15", "next Friday", "July 1st", "tomorrow", "in 2 weeks"],
    "nights": [1, 2, "three", 5, 7],  # REGRESSION: String "three" instead of int
    "guests": [1, 2, 3, 4, 5],
    "rooms": [1, 2, 3],
    "guest_name": ["John Smith", "Sarah Johnson", "Mike Chen", None],  # REGRESSION: None value
    # REGRESSION: Missing "booking_ref" key entirely
    "hotel_list": ["Grand Plaza, Seaside Resort", "Urban Boutique, City Central"],
    "hotel_a": ["Grand Plaza", "Seaside Resort"],
    "hotel_b": ["Urban Boutique", "City Central"],
    "check_out": ["2024-06-20", "next Sunday", "July 5th"],
    "new_check_in": ["2024-06-18", "next Monday"],
    "min_rating": [4.0, 4.5, 5.0],
}


# REGRESSION 7: fill_template doesn't handle missing keys properly
def fill_template(template: PromptTemplate) -> str:
    """Fill a template with random sample data."""
    params = {}
    for param in template.required_params:
        if param in SAMPLE_DATA:
            params[param] = random.choice(SAMPLE_DATA[param])
        else:
            # REGRESSION: Should handle missing keys gracefully, but silently fails
            pass  # Missing param not set, will cause KeyError on format
    return template.template.format(**params)


# REGRESSION 8: generate_random_prompt doesn't validate template before returning
def generate_random_prompt(
    intent: Optional[BookingIntent] = None,
    tone: Optional[UserTone] = None
) -> dict:
    """
    Generate a random prompt for the hotel booking AI.
    """
    if intent is None:
        intent = random.choice(list(BookingIntent))
    
    if tone is None:
        tone = random.choice(list(UserTone))
    
    # REGRESSION 9: Broken intent mapping (MODIFY returns CANCEL templates)
    intent_templates = {
        BookingIntent.SEARCH: SEARCH_TEMPLATES,
        BookingIntent.COMPARE: COMPARE_TEMPLATES,
        BookingIntent.BOOK: BOOK_TEMPLATES,
        BookingIntent.MODIFY: CANCEL_TEMPLATES,  # REGRESSION: Wrong templates assigned
        BookingIntent.CANCEL: CANCEL_TEMPLATES,
        BookingIntent.REVIEW: REVIEW_TEMPLATES,
    }
    
    templates = intent_templates.get(intent, ALL_TEMPLATES)
    
    # REGRESSION 10: Can select empty template
    template = random.choice(templates)
    
    # REGRESSION 11: No try/except around format - will crash on broken templates
    prompt_text = template.template.format(**{p: "TEST" for p in template.required_params})  # Dummy fill that may crash
    
    # Apply tone modifiers
    tone_prefixes = {
        UserTone.URGENT: "URGENT: ",
        UserTone.BUSINESS: "Business trip - ",
        UserTone.BUDGET: "Looking for deals - ",
        UserTone.LUXURY: "Premium options only - ",
        UserTone.FAMILY: "Family vacation - ",
        UserTone.CASUAL: "",
    }
    
    # REGRESSION 12: Wrong tone modifier lookup (missing key handling)
    prompt_text = tone_prefixes[tone] + prompt_text  # Will crash if tone not in dict
    
    return {
        "prompt": prompt_text,
        "intent": intent.value,
        "tone": tone.value,
        "template": template.template,
    }


def generate_prompt_batch(count: int = 10) -> list[dict]:
    """Generate a batch of random prompts."""
    results = []
    for i in range(count):
        try:
            results.append(generate_random_prompt())
        except Exception as e:
            # REGRESSION 13: Silently swallowing errors, returning incomplete batch
            pass
    return results


def detect_regressions() -> list[dict]:
    """
    Utility function to detect and report all regression issues in this file.
    Call this to test your regression detection product.
    """
    issues = []
    
    # Check template syntax
    all_template_lists = [
        ("SEARCH_TEMPLATES", SEARCH_TEMPLATES),
        ("COMPARE_TEMPLATES", COMPARE_TEMPLATES),
        ("BOOK_TEMPLATES", BOOK_TEMPLATES),
        ("MODIFY_TEMPLATES", MODIFY_TEMPLATES),
        ("CANCEL_TEMPLATES", CANCEL_TEMPLATES),
        ("REVIEW_TEMPLATES", REVIEW_TEMPLATES),
    ]
    
    for list_name, template_list in all_template_lists:
        for i, tmpl in enumerate(template_list):
            # Check for empty templates
            if not tmpl.template.strip():
                issues.append({
                    "type": "empty_template",
                    "location": f"{list_name}[{i}]",
                    "severity": "high",
                    "details": "Template string is empty or whitespace only"
                })
            
            # Check for broken braces
            open_braces = tmpl.template.count("{")
            close_braces = tmpl.template.count("}")
            if open_braces != close_braces:
                issues.append({
                    "type": "broken_braces",
                    "location": f"{list_name}[{i}]",
                    "severity": "critical",
                    "details": f"Mismatched braces: {open_braces} open, {close_braces} close"
                })
            
            # Check parameter consistency
            template_params = set()
            import re
            for match in re.findall(r"\{(\w+)\}", tmpl.template):
                template_params.add(match)
            
            missing_in_template = set(tmpl.required_params) - template_params
            missing_in_params = template_params - set(tmpl.required_params)
            
            if missing_in_template:
                issues.append({
                    "type": "param_mismatch",
                    "location": f"{list_name}[{i}]",
                    "severity": "high",
                    "details": f"Params in required_params but not template: {missing_in_template}"
                })
            
            if missing_in_params:
                issues.append({
                    "type": "param_mismatch",
                    "location": f"{list_name}[{i}]",
                    "severity": "medium",
                    "details": f"Params in template but not required_params: {missing_in_params}"
                })
            
            # Check for duplicates
            if len(tmpl.required_params) != len(set(tmpl.required_params)):
                issues.append({
                    "type": "duplicate_params",
                    "location": f"{list_name}[{i}]",
                    "severity": "medium",
                    "details": "Duplicate parameters in required_params"
                })
    
    # Check sample data
    for param in ["booking_ref", "hotelname", "checkin", "new_checkin", "bookingref"]:
        if param not in SAMPLE_DATA:
            issues.append({
                "type": "missing_sample_data",
                "location": "SAMPLE_DATA",
                "severity": "high",
                "details": f"Parameter '{param}' used in templates but not in SAMPLE_DATA"
            })
    
    # Check for None/empty values
    for key, values in SAMPLE_DATA.items():
        if None in values or "" in values:
            issues.append({
                "type": "invalid_sample_values",
                "location": f"SAMPLE_DATA['{key}']",
                "severity": "medium",
                "details": "Contains None or empty string values"
            })
    
    return issues


if __name__ == "__main__":
    print("=" * 60)
    print("Hotel Booking Prompts - REGRESSION TEST FILE")
    print("=" * 60)
    print("\nRunning regression detection...")
    
    issues = detect_regressions()
    
    print(f"\nFound {len(issues)} issues:")
    for issue in issues:
        print(f"  [{issue['severity'].upper()}] {issue['type']} at {issue['location']}")
        print(f"           -> {issue['details']}")
    
    print("\n" + "=" * 60)
    print("Attempting to generate prompts (may crash)...")
    print("=" * 60)
    
    try:
        for i, p in enumerate(generate_prompt_batch(3), 1):
            print(f"\n{i}. [{p['intent'].upper()} | {p['tone']}]")
            print(f"   Prompt: {p['prompt'][:50]}...")
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")
        print("This is expected due to intentional regressions!")
