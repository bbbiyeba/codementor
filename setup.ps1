Write-Host "🎓 Setting up CodeMentor CLI..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path "codementor/core" | Out-Null
New-Item -ItemType Directory -Force -Path "codementor/utils" | Out-Null
New-Item -ItemType Directory -Force -Path "reviews" | Out-Null
@'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# Project specific
*.db
*.sqlite3
config.yaml
.env
reviews/
*.log

# Distribution
dist/
build/
*.egg-info/
'@ | Out-File -FilePath .gitignore -Encoding utf8
@'
click==8.1.7
anthropic==0.18.1
python-dotenv==1.0.0
pygments==2.17.2
rich==13.7.0
pyyaml==6.0.1
'@ | Out-File -FilePath requirements.txt -Encoding utf8
@'
ANTHROPIC_API_KEY=your_api_key_here
'@ | Out-File -FilePath .env.example -Encoding utf8
@'
api:
  provider: "anthropic"
  model: "claude-sonnet-4-20250514"
  max_tokens: 4000

user:
  skill_level: "intermediate"
  primary_languages:
    - python
    - javascript
    - rust
  learning_goals:
    - "Improve code quality"
    - "Learn best practices"

review:
  focus_areas:
    - code_quality
    - best_practices
    - performance
  include_examples: true
  verbosity: "detailed"

storage:
  database_path: "./codementor.db"
  keep_history: true
  max_reviews: 1000
'@ | Out-File -FilePath config.example.yaml -Encoding utf8
"__version__ = '1.0.0'" | Out-File -FilePath "codementor/__init__.py" -Encoding utf8
"" | Out-File -FilePath "codementor/core/__init__.py" -Encoding utf8
"" | Out-File -FilePath "codementor/utils/__init__.py" -Encoding utf8
Write-Host "✅ Done!" -ForegroundColor Green
