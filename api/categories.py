from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Mock categories for now - you can expand this later
        categories = {
            "Modern Life": ["work", "technology", "social media", "remote work"],
            "Indian Culture": ["bollywood", "cricket", "festivals", "family"],
            "Student Life": ["exams", "college", "internship", "placement"],
            "Relationships": ["dating", "marriage", "friendship", "parents"],
            "Food": ["chai", "street food", "cooking", "restaurants"]
        }
        
        response = {
            "success": True,
            "categories": categories
        }
        
        self.wfile.write(json.dumps(response).encode())
        return