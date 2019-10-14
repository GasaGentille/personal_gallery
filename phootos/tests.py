from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.new_image= Image(image = 'sport1.jpg', image_name ='fudu', image_description = "food image", location = "kigali", category ="food")
        self.new_image.save()

        # Creating a new location and saving it
        self.new_image.location.add(location)
        self.new_location.save_location()

         # Creating a new category and saving it
        self.new_image.category.add(self.new_category)
        self.new_category.save_category()


    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()