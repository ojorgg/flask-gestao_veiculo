from . import db

class Veiculo(db.Model):
    __tablename__ = 'veiculo'

    idplaca = db.Column('idplaca', db.String(9), primary_key=True)

    _ano = db.Column('ano', db.Integer)
    _modelo = db.Column('modelo', db.Integer)
    _preco_fipe = db.Column('preco_fipe', db.Numeric(10, 2))
    _fabricante = db.Column('fabricante', db.String(50))
    _modelo_veiculo = db.Column('modelo_veiculo', db.String(60))
    _cor = db.Column('cor', db.String(20))
    _preco_venda = db.Column('preco_venda', db.Numeric(10, 2))
    _total_despesa = db.Column('total_despesa', db.Numeric(10, 2))
    
    compra = db.relationship('Compra', backref='veiculo', lazy=True, uselist=False)
    venda = db.relationship('Venda', backref='veiculo', lazy=True, uselist=False)
    despesas = db.relationship('Despesa', backref='veiculo', lazy=True)

        
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def preco_fipe(self):
        return self._preco_fipe

    @preco_fipe.setter
    def preco_fipe(self, value):
        self._preco_fipe = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value

    @property
    def modelo_veiculo(self):
        return self._modelo_veiculo

    @modelo_veiculo.setter
    def modelo_veiculo(self, value):
        self._modelo_veiculo = value

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def preco_venda(self):
        return self._preco_venda

    @preco_venda.setter
    def preco_venda(self, value):
        self._preco_venda = value

    @property
    def total_despesa(self):
        return self._total_despesa

    @total_despesa.setter
    def total_despesa(self, value):
        self._total_despesa = value

