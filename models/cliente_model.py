from . import db


class Cliente(db.Model):
    __tablename__ = "cliente"

    idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome = db.Column("nome", db.String(60), nullable=False)
    _endereco = db.Column("endereco", db.String(80), nullable=True)
    _cidade = db.Column("cidade", db.String(80), nullable=True)
    _uf = db.Column("uf", db.String(2), nullable=True)
    _cep = db.Column("cep", db.String(9), nullable=True)
    
    
    vendas = db.relationship('Venda', backref='cliente', lazy=True, cascade="all, delete-orphan")
    compras = db.relationship('Compra', backref='cliente', lazy=True, cascade="all, delete-orphan")

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):
        self._uf = value.upper()

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    def to_dict(self):
        return {
            "idcliente": self.idcliente,
            "nome": self.nome,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
        }
