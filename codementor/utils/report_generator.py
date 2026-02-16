from datetime import datetime
from pathlib import Path
from typing import Dict

class ReportGenerator:
    """Generates markdown reports for code reviews."""
    
    @staticmethod
    def generate_review_report(review_data: Dict, output_dir: str = "./reviews") -> str:
        """Generate a markdown report for a code review."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"review_{review_data['language']}_{timestamp}.md"
        filepath = output_path / filename
        
        content = f"""# Code Review Report
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Language:** {review_data['language']}
**File:** {review_data.get('filename', 'N/A')}

---

{review_data['review_content']}

---

## Metadata
- **Model:** {review_data.get('model', 'N/A')}
- **Tokens:** {review_data.get('tokens_used', 'N/A')}
- **Review ID:** {review_data.get('review_id', 'N/A')}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    @staticmethod
    def generate_stats_report(stats: Dict) -> str:
        """Generate a formatted statistics report."""
        report = f"""
# 📊 CodeMentor Statistics

## Overall Progress
- **Total Reviews:** {stats.get('total_reviews', 0)}
- **Average Rating:** {stats.get('avg_rating', 0)}⭐

## Languages Breakdown
"""
        for lang, count in stats.get('languages', {}).items():
            report += f"- **{lang.capitalize()}:** {count} reviews\n"
        
        return report