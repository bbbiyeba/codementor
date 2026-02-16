import sqlite3
import json
from typing import List, Dict

class ReviewStorage:
    """Handles storage and retrieval of code reviews."""
    
    def __init__(self, db_path: str = "./codementor.db"):
        self.db_path = db_path
        self.conn = None
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database with schema."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                language TEXT NOT NULL,
                code_snippet TEXT NOT NULL,
                review_content TEXT NOT NULL,
                skill_level TEXT,
                focus_areas TEXT,
                rating INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.conn.commit()
    
    def save_review(self, review_data: Dict) -> int:
        """Save a code review to the database."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            INSERT INTO reviews 
            (filename, language, code_snippet, review_content, skill_level, focus_areas, rating)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            review_data['filename'],
            review_data['language'],
            review_data['code_snippet'],
            review_data['review_content'],
            review_data.get('skill_level', 'intermediate'),
            json.dumps(review_data.get('focus_areas', [])),
            review_data.get('rating', 0)
        ))
        
        review_id = cursor.lastrowid
        self.conn.commit()
        return review_id
    
    def get_recent_reviews(self, limit: int = 10) -> List[Dict]:
        """Retrieve recent reviews."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM reviews 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (limit,))
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_language_stats(self, language: str) -> Dict:
        """Get statistics for a specific language."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) as total_reviews,
                AVG(rating) as avg_rating
            FROM reviews
            WHERE language = ?
        """, (language,))
        
        result = cursor.fetchone()
        return dict(result) if result else {}
    
    def get_all_stats(self) -> Dict:
        """Get overall statistics."""
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT COUNT(*) as total FROM reviews")
        total_reviews = cursor.fetchone()['total']
        
        cursor.execute("""
            SELECT language, COUNT(*) as count 
            FROM reviews 
            GROUP BY language
        """)
        languages = {row['language']: row['count'] for row in cursor.fetchall()}
        
        cursor.execute("SELECT AVG(rating) as avg FROM reviews WHERE rating > 0")
        avg_rating = cursor.fetchone()['avg'] or 0.0
        
        return {
            'total_reviews': total_reviews,
            'languages': languages,
            'avg_rating': round(avg_rating, 2)
        }
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()