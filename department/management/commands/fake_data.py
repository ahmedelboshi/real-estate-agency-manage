from django.contrib.auth import get_user_model
from department.models import Category,Company,Department,Property
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils import timezone
from random import choice, randint
from faker import Faker
from place.models import City,Country,Governorate
from authapp.models import image_file
from place.status import Status, StatusITem
from place.models import City
from django.core.management.base import BaseCommand, CommandError

from random import choice
fake = Faker()

class Command(BaseCommand):
    help = 'genrate fake data'


    def handle(self,*args,**kwargs):
        print('start')
        User = get_user_model()
        users = User.objects.all()
        for i in range(10):
            country = Country.objects.create(
                name_ar=fake.word(),
                name_en=fake.word(),
                key_country=fake.random_int(min=1, max=10000),
                status=choice([1, 2, 3])
            )

        for i in range(20):
            governorate = Governorate.objects.create(
                country=Country.objects.order_by("?").first(),
                name_ar=fake.word(),
                name_en=fake.word(),
                coed=fake.random_int(min=1, max=10000),
                status=choice([1, 2, 3])
            )

        for i in range(20):
            city = City.objects.create(
                governorate=Governorate.objects.order_by("?").first(),
                name_ar=fake.word(),
                name_en=fake.word(),
                status=choice([1, 2, 3])
            )
        for i in range(10):
            category = Category.objects.create(
                name_ar=fake.word(),
                name_en=fake.word(),
                status=choice([1,2,3]),
                pic0=fake.image_url(width=None, height=None),
            )
            category.users.set(users)

        for i in range(20):
            company = Company.objects.create(
                category=Category.objects.order_by("?").first(),
                name_ar=fake.word(),
                name_en=fake.word(),
                logo=fake.image_url(width=None, height=None),
                url=fake.url(),
            )

        for i in range(50):
            department = Department.objects.create(
                company=Company.objects.order_by("?").first(),
                name_ar=fake.word(),
                name_en=fake.word(),
                status=choice([1,2,3]),
            )

        for i in range(50):
            city = City.objects.order_by("?").first()
            print(city)
            item = Property.objects.create(
                department=Department.objects.order_by("?").first(),
                city=city,
                name_ar=fake.word(),
                name_en=fake.word(),
                decr=fake.text(),
                status=choice([1,2,3]),
                price=fake.pyfloat(right_digits=2, positive=True),
                pic1=fake.image_url(width=None, height=None),
                pic2=fake.image_url(width=None, height=None),
                pic3=fake.image_url(width=None, height=None),
                pic4=fake.image_url(width=None, height=None),
                user=User.objects.order_by("?").first())
