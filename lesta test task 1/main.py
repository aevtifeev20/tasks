import pandas as pd
from dataclasses import dataclass

# инициализация dataclass
@dataclass
class Source:
    website: str
    popularity: int
    frontend: str
    backend: str
    database: str
    notes: str

# получение данных

def get_data():
    df = pd.read_excel('test_data.xlsx', sheet_name='table')

    sources = df.values.tolist()
    sources_instances = []
    for s in sources:
        sources_instances.append(Source(*s)) # добавление dataclass
    return sources_instances

# P.S. можно сделать прямо с сайта по url, но в файле явно и быстро можно добавить строчку и проверить параметризованный тест