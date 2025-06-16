import csv
from faker import Faker

fake = Faker('pt_BR')

NUMERO_MESAS = 50
ARQUIVO_CSV = 'mesas.csv'


def gerar_dados_mesas():
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['mesa_situacao', 'mesa_data_criacao', 'mesa_data_atualizacao'])

        for _ in range(NUMERO_MESAS):
            situacao = 'A' if fake.boolean(chance_of_getting_true=85) else 'I'

            data_criacao = fake.date_time_between(
                start_date='-2y',
                end_date='now'
            )

            data_criacao_str = data_criacao.strftime('%Y-%m-%d %H:%M:%S')

            data_atualizacao = fake.date_time_between(
                start_date=data_criacao,
                end_date='now'
            ).strftime('%Y-%m-%d %H:%M:%S')

            writer.writerow([situacao, data_criacao_str, data_atualizacao])

    print(f'Arquivo {ARQUIVO_CSV} gerado com {NUMERO_MESAS} registros')
