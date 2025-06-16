import csv
from faker import Faker
import random

fake = Faker('pt_BR')

NUMERO_VENDAS = 200
MAX_ITENS_POR_VENDA = 8
ARQUIVO_VENDAS = 'vendas.csv'
ARQUIVO_ITENS_VENDAS = 'itens_vendas.csv'


def carregar_ids():
    with open('funcionarios.csv', 'r', encoding='utf-8') as f:
        funcionarios_ids = [i + 1 for i in range(sum(1 for _ in f) - 1)]

    with open('mesas.csv', 'r', encoding='utf-8') as f:
        mesas_ids = [i + 1 for i in range(sum(1 for _ in f) - 1)]

    with open('produtos.csv', 'r', encoding='utf-8') as f:
        produtos_ids = [i + 1 for i in range(sum(1 for _ in f) - 1)]

    return funcionarios_ids, mesas_ids, produtos_ids


def gerar_dados_vendas():
    funcionarios_ids, mesas_ids, produtos_ids = carregar_ids()

    with open(ARQUIVO_VENDAS, 'w', newline='', encoding='utf-8') as venda_file, \
            open(ARQUIVO_ITENS_VENDAS, 'w', newline='', encoding='utf-8') as item_file:

        venda_writer = csv.writer(venda_file)
        item_writer = csv.writer(item_file)

        # Cabeçalhos
        venda_writer.writerow([
            'venda_funcionario_id', 'venda_mesa_id', 'venda_valor',
            'venda_total', 'venda_desconto', 'venda_situacao',
            'venda_data_criacao', 'venda_data_atualizacao'
        ])

        item_writer.writerow([
            'item_venda_produto_id', 'item_venda_venda_id', 'item_venda_valor',
            'item_venda_quantidade', 'item_venda_total',
            'item_venda_data_criacao', 'item_venda_data_atualizacao'
        ])

        for venda_id in range(1, NUMERO_VENDAS + 1):
            funcionario_id = random.choice(funcionarios_ids)
            mesa_id = random.choice(mesas_ids)

            num_itens = random.randint(1, MAX_ITENS_POR_VENDA)
            itens = []
            valor_total = 0

            for _ in range(num_itens):
                produto_id = random.choice(produtos_ids)
                quantidade = random.randint(1, 3)

                valor_unitario = round(random.uniform(5.0, 100.0), 2)
                total_item = round(valor_unitario * quantidade, 2)

                itens.append({
                    'produto_id': produto_id,
                    'valor': valor_unitario,
                    'quantidade': quantidade,
                    'total': total_item
                })

                valor_total += total_item

            desconto = round(random.uniform(0.05, 0.15) * valor_total, 2) if random.random() < 0.1 else 0
            valor_com_desconto = round(valor_total - desconto, 2)

            data_criacao_dt = fake.date_time_between(start_date='-6m', end_date='now')
            data_criacao_str = data_criacao_dt.strftime('%Y-%m-%d %H:%M:%S')

            data_atualizacao_dt = fake.date_time_between(
                start_date=data_criacao_dt,
                end_date='now'
            )
            data_atualizacao_str = data_atualizacao_dt.strftime('%Y-%m-%d %H:%M:%S')

            venda_writer.writerow([
                funcionario_id,
                mesa_id,
                valor_total,
                valor_com_desconto,
                desconto,
                'A',
                data_criacao_str,
                data_atualizacao_str
            ])

            for item in itens:
                item_data_criacao_dt = fake.date_time_between(
                    start_date=data_criacao_dt,
                    end_date=data_atualizacao_dt
                )
                item_data_criacao_str = item_data_criacao_dt.strftime('%Y-%m-%d %H:%M:%S')

                item_writer.writerow([
                    item['produto_id'],
                    venda_id,
                    item['valor'],
                    item['quantidade'],
                    item['total'],
                    item_data_criacao_str,
                    data_atualizacao_str
                ])

    print(f'Arquivos gerados com sucesso: {ARQUIVO_VENDAS} e {ARQUIVO_ITENS_VENDAS}')
