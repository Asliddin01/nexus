from django.test import TestCase
from category.models import Category, Region, Brand

class CategoryModelTest(TestCase):
    def test_create_main_category(self):
        category = Category.objects.create(
            name="Elektronika",
            is_main=True,
            slug='elektronika'
        )
        self.assertEqual(category.name, "Elektronika")
        self.assertTrue(category.is_main)
        self.assertEqual(category.slug, "elektronika")
        self.assertIsNone(category.parent)
    
    def test_create_subcategory(self):
        parent = Category.objects.create(name="Elektronika", slug="elektronika") 
        sub = Category.objects.create(
            name = "Telefonlar",
            slug = "telefonlar",
            parent = parent
        )   

        self.assertEqual(sub.parent, parent)