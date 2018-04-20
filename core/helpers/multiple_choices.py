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
    (0, u'Feminino'),
    (1, u'Masculino')
)


SCHOLARITY = (
    (u'Fundamental - Incompleto', u'Fundamental - Incompleto'),
    (u'Fundamental - Completo', u'Fundamental - Completo'),
    (u'Médio - Incompleto', u'Médio - Incompleto'),
    (u'Médio - Completo', u'Médio - Completo'),
    (u'Superior - Incompleto', u'Superior - Incompleto'),
    (u'Superior - Completo', u'Superior - Completo'),
    (u'Pós-graduação - Incompleto', u'Pós-graduação - Incompleto'),
    (u'Pós-graduação - Completo', u'Pós-graduação - Completo'),
    (u'Mestrado - Incompleto', u'Mestrado - Incompleto'),
    (u'Mestrado - Completo', u'Mestrado - Completo'),
    (u'Doutorado - Incompleto', u'Doutorado - Incompleto'),
    (u'Doutorado - Completo', u'Doutorado - Completo')
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

NI = 'Não informado'
