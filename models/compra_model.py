from . import db
from datetime import date

class Compra(db.Model):
    __tablename__ = 'compra'
    
    idcompra = db.Column('idcompra', db.Integer, primary_key=True, autoincrement=True)

    _data = db.Column('data', db.Date, nullable=False)
    _valor_pago = db.Column('valor_pago', db.Numeric(10, 2))
    _forma_pagamento = db.Column('forma_pagamento', db.String(40))

    idplaca = db.Column(db.String(9), db.ForeignKey('veiculo.idplaca'), nullable=False, unique=True)
    idcliente = db.Column(db.Integer, db.ForeignKey('cliente.idcliente'), nullable=False)
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def valor_pago(self):
        return self._valor_pago

    @valor_pago.setter
    def valor_pago(self, value):
        self._valor_pago = value

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, value):
       self._forma_pagamento = value

