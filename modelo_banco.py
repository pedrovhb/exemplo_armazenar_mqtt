from sqlalchemy import Column, Float, DateTime, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Criamos o modelo da nossa tabela de valores pra temperatura.
# Cada ponto de dado vai ser uma linha em nossa tabela, que tem as propriedades indicadas abaixo.

class ValorTemperatura(Base):
    __tablename__ = 'valor_temperatura'

    id = Column(Integer, primary_key=True)
    temperatura = Column(Float)
    criacao = Column(DateTime)

    # A representação de quando fazemos um print nessa classe
    # (ou quando a classe tem que ser mostrada como string).
    def __repr__(self):
        return f"<ValorTemperatura(id='{self.id:d}', temperature='{self.temperatura:.2f}', criacao='{self.criacao}')>"


engine = create_engine('sqlite:///banco_temperatura.db')
Base.metadata.create_all(engine)


# Função que retorna uma nova sessão pra interação com o banco de dados.
def criar_sessao():
    Session = sessionmaker(bind=engine)
    sessao = Session()
    return sessao
