from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_recipes_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
    def test_recipes_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        template_content = response.content.decode('utf-8')
        member = 'No recipes found here'
        self.assertIn(member, template_content)
    
    def test_recipes_home_template_loads_recipes(self):
        # atleast 1 recipe is needed for this test
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        # Checking if there are any recipes in the template
        self.assertIn('Recipe Title', content)
    
    def test_recipes_home_template_does_not_load_recipes_if_is_published_field_is_set_to_false(self):
        # atleast 1 recipe is needed for this test
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        # Checking if there are any recipes in the template
        member = 'No recipes found here'
        self.assertIn(member, content)
    
    def test_recipes_make_pagination_works_with_django_pagination_and_returns_the_correct_amount_of_recipes_per_page(self):
        recipe = self.make_recipe()
        for c in range(100): recipe.id = None; recipe.slug=f'recipe-slug-{c}'; recipe.save()

        response = self.client.get(reverse('recipes:home') + '?page=4')
        self.assertEqual(len(response.context['recipes']), 9)
    
    def test_recipes_home_view_returns_to_page_1_if_requested_page_is_not_a_valid_value(self):
        recipe = self.make_recipe()
        for c in range(100): recipe.id = None; recipe.slug=f'recipe-slug-{c}'; recipe.save()

        response = self.client.get(reverse('recipes:home') + '?page=4ok')
        current_page = response.context['pagination_range']['current_page']
        self.assertEqual(current_page, 1)
