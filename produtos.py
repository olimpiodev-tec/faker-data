import csv
from faker import Faker
import random

fake = Faker('pt_BR')

NUMERO_PRODUTOS = 100
ARQUIVO_CSV = 'produtos.csv'

CATEGORIAS = {
    'Bebidas': {
        'Alcoólicas': ['Cerveja Artesanal', 'Vinho Tinto', 'Vinho Branco', 'Whisky', 'Vodka', 'Gin', 'Rum',
                       'Coquetel Clássico', 'Caipirinha', 'Margarita'],
        'Não Alcoólicas': ['Suco Natural', 'Refrigerante', 'Água Mineral', 'Água Tônica', 'Energético', 'Chá Gelado',
                           'Limonada', 'Café Especial']
    },
    'Pratos': {
        'Entradas': ['Bruschetta', 'Carpaccio', 'Bolinhos de Bacalhau', 'Ceviche', 'Tábua de Frios',
                     'Azeitonas Temperadas'],
        'Principais': ['Filé Mignon', 'Risoto de Funghi', 'Penne ao Molho Pesto', 'Frango Grelhado',
                       'Peixe ao Molho de Maracujá', 'Lasanha Bolonhesa'],
        'Sobremesas': ['Tiramisù', 'Petit Gateau', 'Cheesecake', 'Mousse de Chocolate', 'Pudim de Leite',
                       'Sorvete Artesanal']
    }
}


def gerar_produto():
    categoria = random.choice(list(CATEGORIAS.keys()))
    subcategoria = random.choice(list(CATEGORIAS[categoria].keys()))
    produto_base = random.choice(CATEGORIAS[categoria][subcategoria])

    prefixos = ['Especial', 'Premium', 'Casa', 'Chef', 'Delícia', 'Supremo']
    sufixos = ['da Casa', 'Artístico', 'Tradicional', 'Gourmet', 'Caseiro']

    if random.random() > 0.7:
        produto_base = f"{random.choice(prefixos)} {produto_base}"
    if random.random() > 0.7:
        produto_base = f"{produto_base} {random.choice(sufixos)}"

    return produto_base


def gerar_dados_produtos():
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            'produto_nome',
            'produto_valor',
            'produto_situacao',
            'produto_data_criacao',
            'produto_data_atualizacao'
        ])

        produtos_gerados = set()

        while len(produtos_gerados) < NUMERO_PRODUTOS:
            nome = gerar_produto()

            if nome not in produtos_gerados:
                produtos_gerados.add(nome)

                if 'Bebida' in nome or 'Café' in nome or 'Suco' in nome:
                    valor = round(random.uniform(5.0, 30.0), 2)
                elif 'Prato Principal' in nome:
                    valor = round(random.uniform(25.0, 90.0), 2)
                else:
                    valor = round(random.uniform(12.0, 45.0), 2)

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

                writer.writerow([
                    nome,
                    valor,
                    situacao,
                    data_criacao_str,
                    data_atualizacao
                ])

    print(f'Arquivo {ARQUIVO_CSV} gerado com {NUMERO_PRODUTOS} registros')
