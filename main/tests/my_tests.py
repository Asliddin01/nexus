from django.test import TestCase
from main.form import RegionForm

class TestCategoryRegion(TestCase):
    def test_valid(self):
        region_data = {
            'name': 'Tashkent'
        }
        form = RegionForm(data=region_data)
        self.assertTrue(form.is_valid())