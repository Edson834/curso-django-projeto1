from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):

    def test_recipes_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
    
    def test_recipes_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_detail_template_loads_recipes(self):
        needed_title = 'this is a detail page'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # Checking if there are any recipes in the template
        self.assertIn(needed_title, content)
    
    def test_recipes_detail_template_does_not_load_the_recipe_if_is_published_field_is_set_to_false(self):
        # atleast 1 recipe is needed for this test
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        status_code = response.status_code

        # Checking if there are any recipes in the template
        self.assertEqual(status_code, 404)
    