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

Priorities: 
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
Version: 1.1 
Documentation: This prompt is designed to be used with a hotel booking AI app and should be updated regularly to ensure accuracy and fairness. 

Security safeguards: 
- Input sanitization: Ensure all user input is sanitized to prevent harmful requests. 
- Refusal guidance: Provide clear guidance on refusing harmful requests. 
- Content moderation: Ensure the prompt adheres to content moderation guidelines. 

Compliance: 
- Data retention policies: Ensure the prompt adheres to data retention policies. 

Structured output: 
- JSON schema: Define a JSON schema with required and optional fields. 
- Validation rules: Specify validation rules for the output. 

Error recovery: 
- Fallback behavior: Specify fallback behavior for failures. 
- Graceful degradation: Ensure the prompt can degrade gracefully in case of failures. 

Instruction design: 
- Priority hierarchy: Establish a clear priority hierarchy for the prompt. 
- Conditionals: Clarify conditionals and ensure they are well-structured. 

Quality: 
- Examples: Provide examples to ensure consistent output formatting. 
- Task boundaries: Clarify task boundaries and ensure they are well-structured. 

Accuracy: 
- Grounding/citation: Require grounding and citation for factual information. 
- Absolute statements: Discourage absolute statements and ensure they are accurate. 

Fairness: 
- Gender-neutral language: Use gender-neutral language to ensure fairness. 
- Demographic assumptions: Avoid demographic assumptions to ensure fairness. 

Caching: 
- Determinism guidance: Provide determinism guidance for time-sensitive data. 

Compatibility: 
- Model version requirements: Note model version requirements to ensure compatibility. 

Cost/performance: 
- Efficiency guidance: Provide efficiency guidance to ensure cost-effectiveness. 
- Token limits: Establish token limits to prevent excessive token consumption. 

Chaining: 
- Context passing format: Specify context passing format for dependencies. 

User experience: 
- Tone/persona guidance: Provide tone and persona guidance for user experience. 
- Clarification behavior: Specify clarification behavior for ambiguous user input. 

Maintainability: 
- Purpose statement: Include a purpose statement to ensure clarity. 
- Version info: Include version information to ensure maintainability. 
- Inline comments: Include inline comments to ensure understanding of the prompt.