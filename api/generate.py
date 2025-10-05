from http.server import BaseHTTPRequestHandler
import json
import random
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read the request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # For now, return a mock response
            # In a real implementation, you'd integrate with your meme generator
            topic = data.get('topic', 'General')
            
            mock_response = {
                "success": True,
                "filename": f"meme_{topic}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                "top_text": f"When you try to deploy {topic}",
                "bottom_text": "But Vercel says 404",
                "topic": topic,
                "template_url": "https://i.imgflip.com/1bij.jpg",
                "api_endpoint": "/api/view/mock_meme.png",
                "download_endpoint": "/api/download/mock_meme.png"
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            self.wfile.write(json.dumps(mock_response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_response = {
                "success": False,
                "error": str(e)
            }
            self.wfile.write(json.dumps(error_response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()