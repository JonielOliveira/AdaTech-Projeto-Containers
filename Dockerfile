# Use a imagem oficial do Python
FROM python:3.10

# Defina o diretório de trabalho
WORKDIR /development

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o código da aplicação
COPY . .

# Defina as variáveis de ambiente
ENV FLASK_APP=development/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta em que o Flask irá rodar
EXPOSE 80

# Comando para iniciar o servidor Flask
#CMD ["flask", "run"]
