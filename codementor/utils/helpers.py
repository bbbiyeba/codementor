import yaml
from pathlib import Path
from typing import Dict

def load_config(config_path: str = "config.yaml") -> Dict:
    """Load configuration from YAML file."""
    path = Path(config_path)
    
    if not path.exists():
        example_path = Path("config.example.yaml")
        if example_path.exists():
            import shutil
            shutil.copy(example_path, path)
            print(f"✨ Created config.yaml from template")
        else:
            return {
                'api': {'model': 'claude-sonnet-4-20250514'},
                'user': {'skill_level': 'intermediate', 'learning_goals': []},
                'review': {'focus_areas': ['code_quality']},
                'storage': {'database_path': './codementor.db'}
            }
    
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"⚠️  Error loading config: {e}")
        return {}