from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    
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


    
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)
    
    def test_recipes_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)
    
    def test_recipes_category_template_loads_recipes(self):
        # atleast 1 recipe is needed for this test
        needed_title = 'title'
        self.make_recipe(title= needed_title)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        # Checking if there are any recipes in the template
        self.assertIn(needed_title, content)
    
    def test_recipes_category_template_does_not_load_a_recipe_if_is_published_field_is_set_to_false(self):
        # atleast 1 recipe is needed for this test
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
        status_code = response.status_code

        # Checking if there are any recipes in the template
        self.assertEqual(status_code, 404)



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