from . import db

class Prestador(db.Model):
    __tablename__ = 'prestador'
    
    idprestador = db.Column('idprestador', db.Integer, primary_key=True, autoincrement=True)

    _nome_empresa = db.Column('nome_empresa', db.String(60), nullable=False)
    _cidade = db.Column('cidade', db.String(80))
    _uf = db.Column('uf', db.String(2))
    _cep = db.Column('cep', db.String(9))
    
    despesas = db.relationship('Despesa', backref='prestador', lazy=True, cascade="all, delete-orphan")


    @property
    def nome_empresa(self):
        return self._nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self._nome_empresa = nome_empresa

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
    def uf(self, uf):
        self._uf = uf.upper()

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep