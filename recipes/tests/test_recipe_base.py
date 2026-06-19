from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'username',
            password='1234324',
            email = 'username@gmail.com',
        )

        recipe = Recipe.objects.create(
            category = category,
            author = author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe Preparation Steps',
            is_published = True,
            preparation_steps_is_html = False,
        )
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()