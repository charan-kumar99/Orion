"""Test script for Orion features without voice input"""
import config
from client import get_ai_response
import wikipedia
from datetime import datetime
import re

def test_time_feature():
    """Test time functionality"""
    print("\n🕐 Testing Time Feature:")
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    print(f"Current time: {time_str}")

def test_date_feature():
    """Test date functionality"""
    print("\n📅 Testing Date Feature:")
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    print(f"Today's date: {date_str}")

def test_calculation():
    """Test calculation functionality"""
    print("\n🧮 Testing Calculation Feature:")
    
    test_expressions = [
        "2 + 2",
        "10 * 5",
        "100 / 4",
        "15 - 7"
    ]
    
    for expr in test_expressions:
        try:
            result = eval(expr, {"__builtins__": None}, {})
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"Error with {expr}: {e}")

def test_wikipedia():
    """Test Wikipedia search"""
    print("\n📚 Testing Wikipedia Search:")
    
    queries = ["Python programming", "Artificial Intelligence"]
    
    for query in queries:
        try:
            summary = wikipedia.summary(query, sentences=1)
            print(f"\nQuery: {query}")
            print(f"Result: {summary[:100]}...")
        except Exception as e:
            print(f"Error searching '{query}': {e}")

def test_openai():
    """Test OpenAI integration"""
    print("\n🤖 Testing OpenAI Integration:")
    
    if not config.USE_OPENAI:
        print("❌ OpenAI is not configured (no API key)")
        return
    
    print("✅ OpenAI is configured")
    
    # Test a simple query
    test_query = "What is the capital of France?"
    print(f"\nTest Query: {test_query}")
    
    try:
        response = get_ai_response(test_query)
        if response:
            print(f"AI Response: {response}")
        else:
            print("❌ Failed to get response")
    except Exception as e:
        print(f"Error: {e}")

def test_configuration():
    """Test configuration settings"""
    print("\n⚙️ Testing Configuration:")
    print(f"Assistant Name: {config.ASSISTANT_NAME}")
    print(f"OpenAI Enabled: {config.USE_OPENAI}")
    print(f"Logging Enabled: {config.ENABLE_LOGGING}")
    print(f"TTS Language: {config.TTS_LANGUAGE}")
    print(f"Phrase Time Limit: {config.PHRASE_TIME_LIMIT}s")

def main():
    """Run all tests"""
    print("="*50)
    print("🧪 Orion Feature Testing Suite")
    print("="*50)
    
    test_configuration()
    test_time_feature()
    test_date_feature()
    test_calculation()
    test_wikipedia()
    test_openai()
    
    print("\n" + "="*50)
    print("✅ Testing Complete!")
    print("="*50)

if __name__ == "__main__":
    main()
