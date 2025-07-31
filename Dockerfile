# Use a imagem oficial do Python
FROM python:3.12-slim

# Cria uma pasta no container
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para rodar seu app
CMD ["python", "app.py"]
