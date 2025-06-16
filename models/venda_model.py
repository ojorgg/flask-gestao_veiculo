from . import db

class Venda(db.Model):
    __tablename__ = 'venda'
    
    idvenda = db.Column('idvenda', db.Integer, primary_key=True, autoincrement=True)


    _data = db.Column('data', db.Date, nullable=False)
    _valor_vendido = db.Column('valor_vendido', db.Numeric(10, 2))
    _forma_pagamento = db.Column('forma_pagamento', db.String(40))
    
    idplaca = db.Column(db.String(9), db.ForeignKey('veiculo.idplaca'), nullable=False)
    idcliente = db.Column(db.Integer, db.ForeignKey('cliente.idcliente'), nullable=False)


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def valor_vendido(self):
        return self._valor_vendido

    @valor_vendido.setter
    def valor_vendido(self, value):
        self._valor_vendido = value

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, value):
        self._forma_pagamento = value
