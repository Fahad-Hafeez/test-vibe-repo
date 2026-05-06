Generate a hotel booking prompt with the following specifications: 
- Intent: {intent} 
- Tone: {tone} 
- Location: {location} 
- Check-in: {check_in} 
- Check-out: {check_out} 
- Number of guests: {guests} 
- Number of rooms: {rooms} 
- Hotel name: {hotel_name} 
- Booking reference: {booking_ref} 
- New check-in: {new_check_in} 

The prompt should be in a structured JSON format with the following schema: 
{ 
  "intent": "string", 
  "tone": "string", 
  "location": "string", 
  "check_in": "string", 
  "check_out": "string", 
  "guests": "integer", 
  "rooms": "integer", 
  "hotel_name": "string", 
  "booking_ref": "string", 
  "new_check_in": "string" 
} 

The prompt should prioritize the following: 
1. Security: Ensure the prompt does not contain any harmful or sensitive information. 
2. Compliance: Ensure the prompt adheres to data retention policies and content moderation guidelines. 
3. Quality: Ensure the prompt is clear, concise, and well-structured. 
4. Accuracy: Ensure the prompt is accurate and unbiased. 
5. Fairness: Ensure the prompt is fair and neutral. 
6. Efficiency: Ensure the prompt is efficient and cost-effective. 

Error handling and fallback behavior: 
- If the input is invalid, return an error message with a clear explanation. 
- If the prompt is unable to generate a response, return a fallback message with a clear explanation. 

Examples: 
- Generate a prompt for a user searching for a hotel in New York City. 
- Generate a prompt for a user booking a hotel room in Los Angeles. 

Purpose: This prompt is designed to generate hotel booking prompts for a travel AI app. 
Version: 1.0 
Documentation: This prompt is designed to be used with a hotel booking AI app and should be updated regularly to ensure accuracy and fairness.