EXPENSES_TYPE = (
    (u'Aluguel', u'Aluguel'),
    (u'Compra', u'Compra'),
    (u'Pagamento', u'Pagamento')
)

DONATIONS_TYPE = (
    (u'Doação', u'Doação'),
    (u'Recebimento', u'Recebimento')
)

UNIT_TYPE = (
    (u'Caixa(s)', u'Caixa(s)'),
    (u'Embalagem(ns)', u'Embalagem(ns)'),
    (u'Litro(s)', u'Litro(s)'),
    (u'Pacote(s)', u'Pacote(s)'),
    (u'Quilo(s)', u'Quilo(s)'),
    (u'Unidade(s)', u'Unidade(s)')
)

UF = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Brasília'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

CIVIL_STATUS = (
    (1, u'Casado(a)'),
    (2, u'Divorciado(a)'),
    (3, u'Separado(a)'),
    (4, u'Solteiro(a)'),
    (5, u'União Estável'),
    (6, u'Viúvo(a)')
)

GENDER = (
    (1, u'Feminino'),
    (2, u'Masculino')
)


SCHOLARITY = (
    (1, u'Fundamental - Incompleto'),
    (2, u'Fundamental - Completo'),
    (3, u'Médio - Incompleto'),
    (4, u'Médio - Completo'),
    (5, u'Superior - Incompleto'),
    (6, u'Superior - Completo'),
    (7, u'Pós-graduação - Incompleto'),
    (8, u'Pós-graduação - Completo'),
    (9, u'Mestrado - Incompleto'),
    (10, u'Mestrado - Completo'),
    (11, u'Doutorado - Incompleto'),
    (12, u'Doutorado - Completo')
)

TIME = (
    (1, u'Matutino'),
    (2, u'Diurno'),
    (3, u'Vespertino'),
    (4, u'Noturno')
)

EMPLOYEES_TYPE = (
    (1, u'Colaborador(a)'),
    (2, u'Professor(a)')
)

BOOLEAN_TYPE = (
    (0, u'Não'),
    (1, u'Sim'),
)

PHONE_TYPE = [
  ('FIX', "Fixo"),
  ('CEL', "Celular"),
  ('FAX', "Fax"),
  ('OUT', "Outro"),
]

ADDRESS_TYPE = [
  ('UNI', 'Único'),
  ('RES', 'Residencial'),
  ('COM', 'Comercial'),
  ('COB', 'Cobrança'),
  ('ENT', 'Entrega'),
  ('OUT', 'Outro'),
]

STATUS_MP = (
    (u'0', u'Aguardando pagamento'),
    (u'1', u'Pago'),
    (u'2', u'Vencida'),
    (u'3', u'Cancelada'),
)
