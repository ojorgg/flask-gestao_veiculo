from flask import Flask, render_template, request, redirect


from models import db
from controllers.cliente_controller import ControleCliente

def create_app():
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ifsp@localhost/gestao_veiculo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura'

    db.init_app(app)


    from routes.cliente_routes import cliente_bp
    app.register_blueprint(cliente_bp)
    from routes.prestador_routes import prestador_bp
    app.register_blueprint(prestador_bp)
    # --- Registro dos Blueprints (Rotas) ---
    # from routes.cliente_routes import cliente_bp
    # app.register_blueprint(cliente_bp)

    # --- Cria as Tabelas no Banco, se não existirem ---
    with app.app_context():
        from models.cliente_model import Cliente
        from models.venda_model import Venda
        from models.compra_model import Compra
        from models.veiculo_model import Veiculo
        from models.prestador_model import Prestador
        from models.despesa_model import Despesa
        
        db.create_all()

    # --- Rota Principal (Página Inicial) ---
    @app.route('/')
    def home():
        total_clientes = ControleCliente.count_cliente()
        stats = {
            'total_clientes': total_clientes,
            'veiculos_estoque': 15, # Exemplo
            'total_vendas': 125430.50, # Exemplo
            'total_despesas': 12870.00 # Exemplo
        }
        return render_template('home.html', stats=stats)

    return app

# --- Execução da Aplicação ---
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

