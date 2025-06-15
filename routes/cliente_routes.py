from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
import controllers.cliente_controller as controller
from models.cliente_model import Cliente

cliente_bp = Blueprint("cliente_bp", __name__)


@cliente_bp.route("/clientes")
def listar_clientes():
    search_term = request.args.get("search", "", type=str)

    query = Cliente.query
    query = query.order_by(Cliente.nome.asc())

    return render_template(
        "clientes.html", clientes = query.all(), search_term=search_term
    )

# Endpoint para adicionar um cliente
@cliente_bp.route("/clientes/add", methods=["POST"])
def adicionar_cliente():
    if request.method == "POST":
        data = request.form
        success, message = controller.add_cliente(data)
        flash(message, "success" if success else "danger")
    return redirect(url_for("cliente_bp.listar_clientes"))

# Endpoint para editar um cliente
@cliente_bp.route("/clientes/edit/<int:id>", methods=["POST"])
def editar_cliente(id):
    if request.method == "POST":
        data = request.form
        success, message = controller.update_cliente(id, data)
        flash(message, "success" if success else "danger")
    return redirect(url_for("cliente_bp.listar_clientes"))


# Endpoint para remover um cliente pelo id
@cliente_bp.route("/clientes/delete/<int:id>")
def excluir_cliente(id):
    """Endpoint para excluir um cliente."""
    success, message = controller.delete_cliente(id)
    flash(message, "success" if success else "danger")
    return redirect(url_for("cliente_bp.listar_clientes"))


# Endpoint para obter dados de um cliente em formato JSON
@cliente_bp.route("/clientes/<int:id>", methods=["GET"])
def get_cliente_json(id):
    cliente = controller.get_cliente_by_id(id)
    if cliente:
        return jsonify(
            {
                "idcliente": cliente.idcliente,
                "nome": cliente.nome,
                "endereco": cliente.endereco,
                "cidade": cliente.cidade,
                "uf": cliente.uf,
                "cep": cliente.cep,
            }
        )
    return jsonify({"error": "Cliente não encontrado"}), 404
