from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "message": "Meme Generator API is running!",
            "status": "healthy",
            "endpoints": [
                "/api/categories",
                "/api/generate", 
                "/api/random"
            ]
        }
        
        self.wfile.write(json.dumps(response).encode())
        return