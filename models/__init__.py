from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .cliente_model import Cliente
from .compra_model import Compra
from .despesa_model import Despesa
from .prestador_model import Prestador
from .venda_model import Venda
from .veiculo_model import Veiculo