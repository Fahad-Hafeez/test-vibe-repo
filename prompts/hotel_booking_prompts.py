Generate a travel hotel booking AI app prompt system with the following specifications: 
- The system should prioritize user safety and security by implementing input sanitization and refusing harmful requests. 
- It should adhere to content moderation policies and data retention guidelines to ensure compliance with regulations. 
- The system's output should be structured in JSON format with the following fields: intent (string), location (string), check-in date (string), check-out date (string), number of guests (integer), and number of rooms (integer). 
- In case of errors or invalid inputs, the system should provide a fallback behavior, such as requesting additional information or clarifying user intent. 
- The system should prioritize tasks based on the following hierarchy: search, compare, book, modify, cancel, and review. 
- The system should provide examples of different user scenarios, such as searching for hotels, comparing prices, booking a room, and modifying a reservation. 
- The system should use gender-neutral language and avoid making demographic assumptions. 
- The system should be designed to be efficient and cost-effective, with a token limit of 512 and a response time of under 2 seconds. 
- The system should be compatible with the latest model versions and avoid using deprecated patterns. 
- The system should provide a purpose statement, version information, and inline comments for maintainability. 
- The system should use a deterministic approach, with a seed value of 42, to ensure reproducibility. 
- The system should specify context passing format and dependency requirements for chaining. 
- The system should provide tone and persona guidance, as well as clarification behavior for ambiguity. 

Example inputs and outputs: 
- Input: 'I'm looking for a hotel in New York for 3 nights from 2024-09-16.' 
- Output: {'intent': 'search', 'location': 'New York', 'check-in': '2024-09-16', 'check-out': '2024-09-19', 'guests': 1, 'rooms': 1} 
- Input: 'Compare prices for Hotel A and Hotel B in Los Angeles.' 
- Output: {'intent': 'compare', 'location': 'Los Angeles', 'hotel_a': 'Hotel A', 'hotel_b': 'Hotel B', 'price_a': 100, 'price_b': 120} 

Version: 1.0 
Purpose: To generate a travel hotel booking AI app prompt system that prioritizes user safety, security, and efficiency.