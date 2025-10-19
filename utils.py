"""Utility functions for Orion Voice Assistant"""
import os
import logging
from datetime import datetime

def ensure_directory_exists(directory_path):
    """Ensure a directory exists, create if it doesn't"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return True
    return False

def clean_temp_files(file_pattern="temp*.mp3"):
    """Clean up temporary files in the current directory"""
    import glob
    temp_files = glob.glob(file_pattern)
    for file in temp_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error removing {file}: {e}")

def format_song_name(song_key):
    """Format song key to readable name"""
    return song_key.replace("_", " ").title()

def validate_url(url):
    """Basic URL validation"""
    return url.startswith("http://") or url.startswith("https://")

def get_log_timestamp():
    """Get formatted timestamp for logging"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class CommandHistory:
    """Track command history for the assistant"""
    
    def __init__(self, max_size=10):
        self.history = []
        self.max_size = max_size
    
    def add(self, command):
        """Add a command to history"""
        self.history.append({
            "command": command,
            "timestamp": datetime.now()
        })
        
        # Keep only the last max_size items
        if len(self.history) > self.max_size:
            self.history.pop(0)
    
    def get_recent(self, count=5):
        """Get recent commands"""
        return self.history[-count:] if len(self.history) >= count else self.history
    
    def clear(self):
        """Clear command history"""
        self.history.clear()

def format_time_difference(time_delta):
    """Format time difference in human-readable format"""
    seconds = int(time_delta.total_seconds())
    
    if seconds < 60:
        return f"{seconds} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''}"
    else:
        hours = seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''}"
