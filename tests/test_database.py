from data import Data
from praktikum.database import Database
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestDatabase:

    # проверка доступных булочек
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3

        assert buns[0].get_name() == Data.BUN_1
        assert buns[0].get_price() == Data.BUN_1_PRICE

        assert buns[1].get_name() == Data.BUN_2
        assert buns[1].get_price() == Data.BUN_2_PRICE

        assert buns[2].get_name() == Data.BUN_3
        assert buns[2].get_price() == Data.BUN_3_PRICE

    # проверка доступных ингредиентов
    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == Data.SAUCE_1
        assert ingredients[0].get_price() == Data.SAUCE_1_PRICE

        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == Data.SAUCE_2
        assert ingredients[1].get_price() == Data.SAUCE_2_PRICE

        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == Data.SAUCE_3
        assert ingredients[2].get_price() == Data.SAUCE_3_PRICE

        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == Data.FILLING_1
        assert ingredients[3].get_price() == Data.FILLING_1_PRICE

        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == Data.FILLING_2
        assert ingredients[4].get_price() == Data.FILLING_2_PRICE

        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == Data.FILLING_3
        assert ingredients[5].get_price() == Data.FILLING_3_PRICE
        