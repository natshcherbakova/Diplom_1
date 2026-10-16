import pytest

from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestIngredient:

    # проверка, что get_type возвращает тип ингредиента
    @pytest.mark.parametrize(
        'ingredient_type',
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Data.SAUCE_1, Data.SAUCE_1_PRICE)

        assert ingredient.get_type() == ingredient_type


    # проверка, что get_name возвращает название ингредиента
    @pytest.mark.parametrize(
        'name',
        [
            Data.SAUCE_1,
            Data.SAUCE_2,
            Data.SAUCE_3
        ]
    )
    def test_get_name_returns_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, Data.SAUCE_1_PRICE)

        assert ingredient.get_name() == name


    # проверка, что get_price возвращает цену ингредиента
    @pytest.mark.parametrize(
        'price',
        [
            Data.SAUCE_1_PRICE,
            Data.SAUCE_2_PRICE,
            Data.SAUCE_3_PRICE
        ]
    )
    def test_get_price_returns_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_1, price)

        assert ingredient.get_price() == price
