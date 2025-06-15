from . import db

class Despesa(db.Model):
    __tablename__ = 'despesa'
    
    iddespesa = db.Column('iddespesa', db.Integer, primary_key=True, autoincrement=True)
    
    _descricao = db.Column('descricao', db.String(80), nullable=False)
    _valor = db.Column('valor', db.Numeric(10, 2), nullable=False)
    _data_servico = db.Column('data_servico', db.Date)
    
    idplaca = db.Column(db.String(9), db.ForeignKey('veiculo.idplaca'), nullable=False)
    idprestador = db.Column(db.Integer, db.ForeignKey('prestador.idprestador'), nullable=False)


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_servico(self):
        return self._data_servico

    @data_servico.setter
    def data_servico(self, data_servico):
        self._data_servico = data_servico

