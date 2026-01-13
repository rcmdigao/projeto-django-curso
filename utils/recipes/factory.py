# from inspect import signature
from random import randint

#python -m pip install faker
from faker import Faker as faker

# def rand_ratio():
#     return random.randint(840, 900), random.randint(473, 573)
def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'titulo': fake.sentence(nb_words=6), #titulo da receita
        'slug': fake.slug(),    #slug é uma url amigável
        'descricao': fake.sentence(nb_words=12), #descrição da receita
        'tempo_preparo': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos', #unidade de tempo de preparo (Minutos, Horas, Dias, etc.)
        'rendimento': fake.random_number(digits=2, fix_len=True),
        'rendimento_unit': 'Porção', #unidade de rendimento
        'passos_preparo': fake.text(3000), #passos de preparo da receita
        'criado_em': fake.date_time(), #data de criação da receita
        'author': {
            'nome': fake.first_name(), #nome do autor da receita
            'sobrenome': fake.last_name(), #sobrenome do autor da receita
        },
        'categoria': {
            'nome': fake.word() #nome da categoria da receita
        },
        'capa': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(), #url da capa da receita
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())