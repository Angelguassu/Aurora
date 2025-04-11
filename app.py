from flask import Flask, render_template, request, redirect, session
import psycopg2

app = Flask(__name__)
app.secret_key = "aurora_chave_secreta"  # Pode trocar por algo mais seguro

# Função para conectar ao banco de dados Neon
def get_db_connection():
    return psycopg2.connect(
        dbname="aurora_db",
        user="aurora_db_owner",
        password="npg_OCoS6mjuVXg2",
        host="ep-rough-union-aca2oa2h-pooler.sa-east-1.aws.neon.tech",
        port="5432",
        sslmode="require"
    )

# Página de login
@app.route('/')
def login():
    return render_template('login.html')

# Lógica do login
@app.route('/logar', methods=['POST'])
def logar():
    username = request.form['username']
    senha = request.form['senha']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE username = %s AND senha = %s", (username, senha))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        session['usuario'] = user[1]  # Salva nome de usuário na sessão
        return redirect('/dashboard')
    else:
        return "Usuário ou senha inválidos"

# Página protegida
@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', usuario=session['usuario'])
    else:
        return redirect('/')

# Logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
