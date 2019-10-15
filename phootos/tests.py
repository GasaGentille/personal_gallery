from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.new_image= Image(image ='images/', image_name ='fudu', image_description = "food image")

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

   # Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    #test delete
    def test_delete_image(self):
        self.new_image.save_image()
        image = Image.objects.filter(image_name='fudu').first()
        delete = Image.objects.filter(image_name = image.image_name).delete()
        images = Image.objects.all()
        self.assertFalse(len(images)==1) 

    def test_update_image(self):  
        self.new_image.save_image()
        image = Image.objects.filter(image_name='fudu').first()
        update = Image.objects.filter(image_name=image.image_name).update(image_name='ibiryo')
        updated = Image.objects.filter(image_name='ibiryo').first()
        self.assertNotEqual(image.image_name, updated.image_name)    

class LocationTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.kimuhurura = Location(location = "kimuhurura")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kimuhurura,Location))

class CategoryTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.tourist = Category(category = "tourist")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tourist,Category))
    
