import os 

def listar_arquivos (diretorio):
	try:
		arquivos = os.listdir(diretorio) #lista os arquivos do diretorio
	

		for arquivo in arquivos: #para exibir informações sobre o arquivo
			caminho_completo = os.path.join(diretorio, arquivo)
			tamanho = os.path.getsize (caminho_completo)
		print (f"Arquivo: {arquivo} | A Tamanho: {tamanho} bytes")

	except FileNotFoundError:
		print (f"O diretorio '{diretorio} não foi encontrado")


if __name__ == "__main__":
	diretorio_alvo = "/home/sac-01/Documentos"
	
	listar_arquivos (diretorio_alvo)
