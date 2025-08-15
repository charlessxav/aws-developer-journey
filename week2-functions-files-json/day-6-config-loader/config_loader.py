import json
import os

def load_config(file_path):
    """Load JSON configuration from file and returns as a dictionary"""

    if not os.path.exists(file_path):
        print("Current working directory:", os.getcwd())
        raise FileNotFoundError(f"Config file '{file_path}' not found")

    
    with open(file_path, 'r') as file:
        return json.load(file)
    

def validate_config(config):
    """Validate required keys in the configuration"""

    required_keys = ["app_name", "version", "debug", "max_connections"]
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required config key: '{key}'")   
        
def display_config(config):
    """Display config settings nicely"""
    print("\n===Application Configuration===")
    for key, value in config.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    try:
        config_file = "config.json"
        # Get absolute path to the folder where THIS script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
      
        # Join it with your config.json filename
        config_file = os.path.join(script_dir, "config.json")

        config = load_config(config_file)
        validate_config(config)
        display_config(config)
    
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error: {e}")
    finally:
        print("Configuration loader finished.")