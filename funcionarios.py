import csv
from faker import Faker

fake = Faker('pt_BR')

NUMERO_FUNCIONARIOS = 50
ARQUIVO_CSV = 'funcionarios.csv'

CARGOS = [
    'Gerente', 'Garçom', 'Chef de Cozinha', 'Sous Chef', 'Bartender',
    'Recepcionista', 'Auxiliar de Cozinha', 'Atendente', 'Supervisor',
    'Sommelier', 'Barista', 'Host/Hostess'
]


def gerar_dados_funcionarios():
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            'funcionario_nome',
            'funcionario_situacao',
            'funcionario_comissao',
            'funcionario_cargo',
            'funcionario_data_criacao',
            'funcionario_data_atualizacao'
        ])

        for _ in range(NUMERO_FUNCIONARIOS):
            nome = fake.name()

            situacao = 'A' if fake.boolean(chance_of_getting_true=90) else 'I'

            comissao = round(fake.random.uniform(1.0, 15.0), 2)

            cargo = fake.random.choice(CARGOS)

            data_criacao = fake.date_time_between(
                start_date='-3y',
                end_date='now'
            )

            data_criacao_str = data_criacao.strftime('%Y-%m-%d %H:%M:%S')

            data_atualizacao = fake.date_time_between(
                start_date=data_criacao,
                end_date='now'
            ).strftime('%Y-%m-%d %H:%M:%S')

            writer.writerow([
                nome,
                situacao,
                comissao,
                cargo,
                data_criacao_str,
                data_atualizacao
            ])

    print(f'Arquivo {ARQUIVO_CSV} gerado com {NUMERO_FUNCIONARIOS} registros')