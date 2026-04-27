import http.server
import socketserver
import json

PORT = 8000

class BookingHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/prenotazione':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            print(f"--- Nuova Prenotazione Ricevuta ---")
            print(json.dumps(data, indent=2))
            print("-----------------------------------")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {"success": True, "message": "Prenotazione ricevuta correttamente"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), BookingHandler) as httpd:
        print(f"Backend Server in esecuzione sulla porta {PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer arrestato.")
