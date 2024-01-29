# cria um banco de dados chamado "contatos"
create database contatos;

# seleciona o banco de dados "contatos" para ser utilizado
use contatos;

# cria uma tabela dentro do banco de dados que está sendo utilizado ("contatos")
create table recados
(
	nome varchar(45),
    apelido varchar(45),
	email varchar(45),
    crush varchar(45),
    assunto varchar(45),
    mensagem varchar(255)
);

# selecionar todos os dados da tabela
SELECT * FROM recados;

# insere valores na tabela
INSERT INTO recados (nome, apelido, email, crush, assunto, mensagem)
VALUES
('Anakin Skywalker', 'Darth Vader', 'darth.vader@gmail.com', 'Luke Skywalker', 'Um segredo para você', 'Luke, eu sou seu pai!'),
('Rafiki Mandril', 'Rafiki Babuíno', 'rafiki.babuino@outlook.com', 'Simba King', 'O passado', 'O passado pode machucar. Mas, como eu vejo é: você pode fugir dele ou aprender com ele.'),
('Agostinho Carrara', 'Tinho', 'agostinho.carrara@uol.com.br','Bebel Carrara', 'Sai logo desse site!', 'Eu amo você, Maria Isabel. Mas, você é difícil. Eu amo você do tamanho da dificuldade que você é.');

# deletar valores na tabela
SET SQL_SAFE_UPDATES=0;
DELETE FROM recados;
DELETE FROM recados WHERE nome="Anakin Skywalker";
SET SQL_SAFE_UPDATES=1;

# deletar a tabela
SET SQL_SAFE_UPDATES=0;
DROP TABLE recados;
SET SQL_SAFE_UPDATES=1;

SHOW TABLES LIKE 'recados';


