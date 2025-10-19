"""OpenAI Client Integration for Orion Voice Assistant"""
from openai import OpenAI
import config

def get_openai_client():
    """Initialize and return OpenAI client if API key is available"""
    if not config.OPENAI_API_KEY:
        return None
    
    try:
        client = OpenAI(api_key=config.OPENAI_API_KEY)
        return client
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        return None

def get_ai_response(user_query, conversation_history=None):
    """
    Get an intelligent response from OpenAI for user queries
    
    Args:
        user_query (str): The user's question or command
        conversation_history (list): Optional conversation context
        
    Returns:
        str: AI-generated response or None if failed
    """
    client = get_openai_client()
    if not client:
        return None
    
    try:
        messages = [
            {
                "role": "system", 
                "content": f"You are {config.ASSISTANT_NAME}, a helpful virtual assistant skilled in general tasks like Alexa and Google Assistant. Provide concise, helpful responses."
            }
        ]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Add current user query
        messages.append({"role": "user", "content": user_query})
        
        completion = client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        
        return completion.choices[0].message.content
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None

# Test function
if __name__ == "__main__":
    if config.USE_OPENAI:
        response = get_ai_response("What is coding?")
        if response:
            print(f"AI Response: {response}")
        else:
            print("Failed to get AI response")
    else:
        print("OpenAI API key not configured. Add your API key to .env file.")