from flask import Flask, render_template, request, redirect, url_for
import pymysql

# app = Flask(__name__)

def criar_tabela(mysql_connection):
    # Conecta ao banco de dados
    connection = mysql_connection

    try:
        with connection.cursor() as cursor:
            # Verifica se a tabela já existe
            table_name = 'recados'
            query = f"SHOW TABLES LIKE '{table_name}'"
            cursor.execute(query)

            existetabela = cursor.fetchone()

            if existetabela is None:
                
                # Cria a tabela
                create_table_query = """
                    CREATE TABLE recados (
	                    nome VARCHAR(45),
                        apelido VARCHAR(45),
	                    email VARCHAR(45),
                        crush VARCHAR(45),
                        assunto VARCHAR(45),
                        mensagem VARCHAR(255)
                    );
                """
                cursor.execute(create_table_query)

                create_table_query = """
                INSERT INTO recados (nome, apelido, email, crush, assunto, mensagem)
                VALUES
                ('Anakin Skywalker', 'Darth Vader', 'darth.vader@gmail.com', 'Luke Skywalker', 'Um segredo para você', 'Luke, eu sou seu pai!'),
                ('Rafiki Mandril', 'Rafiki Babuíno', 'rafiki.babuino@outlook.com', 'Simba King', 'O passado', 'O passado pode machucar. Mas, como eu vejo é: você pode fugir dele ou aprender com ele.'),
                ('Agostinho Carrara', 'Tinho', 'agostinho.carrara@uol.com.br','Bebel Carrara', 'Sai logo desse site!', 'Eu amo você, Maria Isabel. Mas, você é difícil. Eu amo você do tamanho da dificuldade que você é.');
                """
                cursor.execute(create_table_query)

        # Commit das alterações
        connection.commit()

    finally:
        # Fecha a conexão
        connection.close()



# Função para criar e configurar a aplicação Flask
def create_app():
    app = Flask(__name__)

    # conexão com o banco de dados
    app.config['MYSQL_HOST'] = 'database' # 127.0.0.1 (localhost)
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'a1b2c3d4'
    app.config['MYSQL_DATABASE'] = 'contatos'

    global mysql_connection

    mysql_connection = pymysql.connect(
        host = app.config['MYSQL_HOST'],
        user = app.config['MYSQL_USER'],
        password= app.config['MYSQL_PASSWORD'],
        db = app.config['MYSQL_DATABASE']
    )

    # Configurações e extensões adicionais podem ser adicionadas aqui

    # Cria a tabela no início da aplicação
    criar_tabela(mysql_connection)

    print("Está funcionando!!!")

    # Adicione outras rotas e lógica da aplicação aqui

    return app

# Inicializa a aplicação
app = create_app()



@app.route('/contato.html', methods=['GET', 'POST'])  
def contato():

    if request.method == 'POST':
        nome = request.form['nome']
        apelido = request.form['apelido']
        email = request.form['email']
        crush = request.form['crush']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']


        mysql_connection3 = pymysql.connect(
            host = app.config['MYSQL_HOST'],
            user = app.config['MYSQL_USER'],
            password= app.config['MYSQL_PASSWORD'],
            db = app.config['MYSQL_DATABASE']
        )

        cur = mysql_connection3.cursor()

        cur.execute("INSERT INTO recados(nome, apelido, email, crush, assunto, mensagem) VALUES (%s, %s, %s, %s, %s, %s)", (nome, apelido, email, crush, assunto, mensagem))

        mysql_connection3.commit()

        mysql_connection3.close()

        return redirect(url_for('index'))
    
    return render_template('contato.html')

@app.route('/recados.html')  
def recados():
    
    mysql_connection2 = pymysql.connect(
        host = app.config['MYSQL_HOST'],
        user = app.config['MYSQL_USER'],
        password= app.config['MYSQL_PASSWORD'],
        db = app.config['MYSQL_DATABASE']
    )
    
    cur = mysql_connection2.cursor()

    mensagens = cur.execute("SELECT * FROM recados")

    if mensagens > 0:
        dados_mensagens = cur.fetchall()
        mysql_connection2.close()

        i = 0
        detalhes_mensagens = []
        for msg in dados_mensagens:
            accordion = ["accordionExample"+str(i), "#collapse"+str(i), "collapse"+str(i), "#accordionExample"+str(i)]
            detalhes_mensagens.append(accordion + list(msg))
            i += 1

        return render_template('recados.html', detalhes_mensagens=detalhes_mensagens)
    else:
        mysql_connection2.close()
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/machos.html')
def machos():
    return render_template('machos.html')

@app.route('/spike.html')
def spike():
    return render_template('usuario-01-spike.html')

@app.route('/luke.html')
def luke():
    return render_template('usuario-02-luke.html')

@app.route('/simba.html')
def simba():
    return render_template('usuario-03-simba.html')

@app.route('/robin.html')
def robin():
    return render_template('usuario-04-robin.html')

@app.route('/femeas.html')
def femeas():
    return render_template('femeas.html')

@app.route('/aurora.html')
def aurora():
    return render_template('usuario-05-aurora.html')

@app.route('/katy.html')
def katy():
    return render_template('usuario-06-katy.html')

@app.route('/bebel.html')
def bebel():
    return render_template('usuario-07-bebel.html')

@app.route('/lady.html')
def lady():
    return render_template('usuario-08-lady.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
