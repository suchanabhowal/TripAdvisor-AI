import yaml
import os

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        # print(config)
    return config 
# Optional: for testing if the file runs
if __name__ == "__main__":
    config = load_config()
    print(config)
"""import yaml
import os

def load_config() -> dict:
    # Get the directory of this file (utils/config_loader.py)
    current_dir = os.path.dirname(__file__)
    
    # Build the path to the config.yaml located in the config/ folder
    config_path = os.path.abspath(os.path.join(current_dir, "..", "config", "config.yaml"))

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    
    return config

# Optional: for testing if the file runs
if __name__ == "__main__":
    config = load_config()
    print(config)"""

