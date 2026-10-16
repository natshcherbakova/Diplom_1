import pytest

from data import Data
from praktikum.bun import Bun


class TestBun:

    # проверка, что get_name возвращает название булки
    @pytest.mark.parametrize('name', Data.BUN_NAMES)
    def test_get_name_returns_bun_name(self, name):
        bun = Bun(name, Data.BUN_1_PRICE)

        assert bun.get_name() == name

    # проверка, что get_price возвращает цену булки
    @pytest.mark.parametrize('price', Data.BUN_PRICES)
    def test_get_price_returns_bun_price(self, price):
        bun = Bun(Data.BUN_1, price)

        assert bun.get_price() == price
