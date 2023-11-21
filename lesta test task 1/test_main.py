import pytest
from main import get_data

# значения из задания
@pytest.mark.parametrize(
    "count",
    [10 ** 7,
    int(1.5 * 10 ** 7),
    5 * 10 ** 7,
    10 ** 8,
    5 * 10 ** 8,
    10 ** 9,
    int(1.5 * 10 ** 9)]
)
# таблица
@pytest.mark.parametrize(
    "data",
    get_data()
)
# проверка каждой строчки с каждым значением из задания
def test_main(count, data): 
    assert data.popularity > count, "{} (Frontend:{}|Backend:{}) has {} unique visitors per month. \
(Expected more than {})".format(data.website, data.frontend, data.backend, data.popularity, count)

    # Строка с примером
    # Wikipedia (Frontend:JavaScript|Backend:PHP) has 475 000 000 unique visitors per month. (Expected more than 500 000 000)      

if __name__ == "__main__":
    pytest.main()       