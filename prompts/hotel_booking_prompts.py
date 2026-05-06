Generate a travel hotel booking AI app prompt system with the following specifications: 
- Ensure security by implementing input sanitization, refusal guidance for harmful requests, and explicit safeguards against manipulation. 
- Define a JSON schema for structured output with required fields: 'booking_intent', 'location', 'check_in', 'check_out', 'guests', 'rooms', and optional fields: 'hotel_name', 'booking_ref', 'new_check_in'. 
- Implement error handling with fallback behavior for invalid inputs, and specify a priority hierarchy for conflicting instructions. 
- Use gender-neutral language, avoid demographic assumptions, and add grounding/citation requirements to discourage absolute statements. 
- Add efficiency guidance, token limits, and length constraints to optimize cost/performance. 
- Specify context passing format and dependency requirements for chaining. 
- Include a purpose statement, version info, and inline comments for maintainability. 
- Define a data retention policy and content moderation guidance for compliance. 
- Provide examples for quality improvement, clarify task boundaries, and specify output format. 
- Add determinism guidance (seeds) or cache control for time-sensitive data. 
- Note model version requirements and avoid deprecated patterns for compatibility. 
- Use a tone/persona guidance and clarification behavior for ambiguity to enhance user experience. 

Example inputs: 
- 'I'm looking for a hotel in {location} for {nights} nights from {check_in}. Need {rooms} room(s) for {guests} guest(s).' 
- 'Compare these hotels for me: {hotel_list}. Which has better amenities?' 
- 'Book {hotel_name} in {location} for {check_in} to {check_out}. {guests} guests, {rooms} rooms. Name: {guest_name}' 

Example outputs: 
- {'booking_intent': 'search', 'location': 'New York', 'check_in': '2024-09-20', 'check_out': '2024-09-25', 'guests': 2, 'rooms': 1} 
- {'booking_intent': 'compare', 'hotel_list': ['Hotel A', 'Hotel B'], 'location': 'Paris'} 
- {'booking_intent': 'book', 'hotel_name': 'Hotel X', 'location': 'London', 'check_in': '2024-10-01', 'check_out': '2024-10-05', 'guests': 3, 'rooms': 2, 'guest_name': 'John Doe'} 

Version: 1.0 
Purpose: To generate a travel hotel booking AI app prompt system that ensures security, compliance, and quality while optimizing cost/performance and user experience.