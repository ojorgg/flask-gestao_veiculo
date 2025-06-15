from models import Cliente, db

def get_all_clientes():
    try:
        clientes = Cliente.query.order_by(Cliente.nome).all()
        return clientes
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")
        return []


def get_cliente_by_id(id):
    return Cliente.query.get(id)


def add_cliente(data):
    try:
        novo_cliente = Cliente(
            nome=data.get('nome'),
            endereco=data.get('endereco'),
            cidade=data.get('cidade'),
            uf=data.get('uf'),
            cep=data.get('cep')
        )
        db.session.add(novo_cliente)
        db.session.commit()
        return True, "Cliente adicionado com sucesso!"
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao adicionar cliente: {e}")
        return False, "Erro ao adicionar cliente."

def update_cliente(id, data):
    try:
        cliente = get_cliente_by_id(id)
        if not cliente:
            return False, "Cliente não encontrado."
        
        cliente.nome = data.get('nome')
        cliente.endereco = data.get('endereco')
        cliente.cidade = data.get('cidade')
        cliente.uf = data.get('uf')
        cliente.cep = data.get('cep')
        
        db.session.commit()
        return True, "Cliente atualizado com sucesso!"
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao atualizar cliente: {e}")
        return False, "Erro ao atualizar cliente."

def delete_cliente(id):
    try:
        cliente = get_cliente_by_id(id)
        if not cliente:
            return False, "Cliente não encontrado."
            
        db.session.delete(cliente)
        db.session.commit()
        return True, "Cliente excluído com sucesso!"
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao excluir cliente: {e}")
        return False, "Erro ao excluir cliente."

