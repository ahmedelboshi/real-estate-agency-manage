from django.test import TestCase
from .models import *
from place.models import Country,City,Governorate
from django.contrib.auth import get_user_model
from django.urls import reverse
# import Image from pillow
# from pi
User = get_user_model()
# Create your tests here.


# create test for test create item
class PropertyTest(TestCase):
    def setUp(self):
        # create category Country City Governorate
        self.user = User.objects.create_user(username='test', password='test',phone_number='+24*123456789',email="g@g.com")
        self.country = Country.objects.create(name_ar='test', name_en='test')
        self.governorate = Governorate.objects.create(name_ar='test', name_en='test', country=self.country)
        self.city = City.objects.create(name_ar='test', name_en='test', governorate=self.governorate)
        self.category = Category.objects.create(name_ar='test', name_en='test')

        self.item = Property.objects.create(name_ar='test', name_en='test', description_ar='test', description_en='test',
                                        price=10, status_item=1, city=self.city,  category=self.category)
        self.type = PropertyType.objects.create(name_ar='test', name_en='test')

        self.attr1 = Attribute.objects.create(name_ar='test1', name_en='test1', type=self.type)
        self.attr2 = Attribute.objects.create(name_ar='test2', name_en='test2', type=self.type)
        # create 3 choices for attr1 each one has diffrent value
        self.choice1 = AttributeChoice.objects.create(name_ar='test1', name_en='test1', value=1, attribute=self.attr1)
        self.choice2 = AttributeChoice.objects.create(name_ar='test2', name_en='test2', value=2, attribute=self.attr1)
        self.choice3 = AttributeChoice.objects.create(name_ar='test3', name_en='test3', value=3, attribute=self.attr1)

        # create 3 choices for attr2 each one has diffrent value
        self.choice4 = AttributeChoice.objects.create(name_ar='test4', name_en='test4', value=4, attribute=self.attr2)
        self.choice5 = AttributeChoice.objects.create(name_ar='test5', name_en='test5', value=5, attribute=self.attr2)
        self.choice6 = AttributeChoice.objects.create(name_ar='test6', name_en='test6', value=6, attribute=self.attr2)

    def get_image(count=1):
        images = []
        for i in list(range(count)):
            file = io.BytesIO()
            image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
            image.save(file, 'png')
            file.name = 'test.png'
            file.seek(0)
            images.append(file)
        return images[0] if count == 1 else images


    def create_image(self):
        # create image file
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

    def test_item(self):
        self.assertEqual(self.item.name_ar, 'test')
        self.assertEqual(self.item.name_en, 'test')
        self.assertEqual(self.item.description_ar, 'test')
        self.assertEqual(self.item.description_en, 'test')
        self.assertEqual(self.item.price, 10)
        self.assertEqual(self.item.status_item, 1)
        self.assertEqual(self.item.city, 1)
        self.assertEqual(self.item.department, 1)
        self.assertEqual(self.item.category, 1)

    def test_item_create_endpoint(self):
        #test create item endpoint
        self.client.force_login(self.user)
        # send request to create item create the serializer is PropertyCreateUpdateSerialzer for images upload image to server using
        response = self.client.post(reverse('item-create'), data={"name_ar": "test", "name_en": "test","price": 10, "status_item": 1, "city": 1, "department": 1, "category": 1,"type":self.type1.id,"choices":[self.choice1.id,self.choice4.id],"images":[{"image":"http://"}]})