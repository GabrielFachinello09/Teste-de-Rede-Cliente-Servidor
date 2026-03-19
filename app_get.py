from http.server import HTTPServer,BaseHTTPRequestHandler 
#Importa duas classes da biblioteca:
#HTTPServer: cria o servidor HTTP.
#BaseHTTPRequestHandler: classe base para lidar com requisições (GET, POST.)

class Servidor(BaseHTTPRequestHandler):
#Cria classe chamada servidor herdando o (BaseHTTPRequestHandler

    def do_GET(self):
        self.send_response(200) 
#Envia o código HTTP 200, que significa “OK” (requisição bem-sucedida).
        self.end_headers()
        self.wfile.write(b"Welcome to my server")
#Envia o conteúdo da resposta para o cliente.


    def do_POST(self): 
#Chamado quando o cliente envia dados via POST.

        tamanho = int(self.headers['Content-Length']) #identifica o tamanho dos arquivos enviados na requisição.

        dados = self.rfile.read(tamanho) #lê os dados enviados.

        print("Dados recebidos:", dados.decode()) 
        self.send_response(200) 
        self.end_headers()
        self.wfile.write(b"POST RECEBIDO") 


HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()
print("teste")

    
    
    
