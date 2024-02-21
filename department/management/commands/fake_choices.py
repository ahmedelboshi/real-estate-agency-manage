from django.core.management.base import BaseCommand
from department.models import *


class Command(BaseCommand):
    help = ""
    SILENT, NORMAL, VERBOSE = 0, 1, 2
    data = {
        "attributes": [
            {
                "name_en": "Make",
                "name_ar": "الصنع",
                "choices": [
                    {"id": 1, "choice_en": "Toyota", "choice_ar": "تويوتا"},
                    {"id": 2, "choice_en": "Nissan", "choice_ar": "نيسان"},
                    {"id": 3, "choice_en": "Ford", "choice_ar": "فورد"},
                ],
            },
            {
                "name_en": "Color",
                "name_ar": "اللون",
                "choices": [
                    {"choice_en": "Red", "choice_ar": "أحمر"},
                    {"choice_en": "Blue", "choice_ar": "أزرق"},
                    {"choice_en": "Black", "choice_ar": "أسود"},
                    {"choice_en": "White", "choice_ar": "أبيض"},
                ],
            },
            {
                "name_en": "Model",
                "name_ar": "الموديل",
                "choices": [
                    {"id": 4, "choice_en": "Camry", "choice_ar": "كامري"},
                    {"id": 5, "choice_en": "Altima", "choice_ar": "التيما"},
                    {"id": 6, "choice_en": "Mustang", "choice_ar": "ماستانغ"},
                ],
            },
            {
                "name_en": "Year",
                "name_ar": "السنة",
                "choices": [
                    {"id": 7, "choice_en": "2020", "choice_ar": "2020"},
                    {"id": 8, "choice_en": "2019", "choice_ar": "2019"},
                    {"id": 9, "choice_en": "2018", "choice_ar": "2018"},
                ],
            },
            {
                "name_en": "Transmission",
                "name_ar": "الناقلة",
                "choices": [
                    {"id": 10, "choice_en": "Automatic", "choice_ar": "أوتوماتيك"},
                    {"id": 11, "choice_en": "Manual", "choice_ar": "يدوي"},
                ],
            },
            {
                "name_en": "Type",
                "name_ar": "النوع",
                "choices": [
                    {"id": 1, "choice_en": "Sedan", "choice_ar": "سيدان"},
                    {"id": 2, "choice_en": "4x4", "choice_ar": "4x4"},
                    {"id": 3, "choice_en": "SUV", "choice_ar": "SUV"},
                ],
            },
        ]
    }

    def handle(self, *args, **options):
        PropertyType.objects.all().delete()
        i=PropertyType.objects.create(name_ar="سيارة",name_en="car")
        for attr in self.data["attributes"]:
            a = Attribute.objects.create(
                name_ar=attr["name_ar"], name_en=attr["name_en"],item_type=i
            )
            for c in attr["choices"]:
                AttributeChoice.objects.create(
                    choice_en=c["choice_en"], choice_ar=c["choice_ar"],attribute=a
                )

    def prepare(self):
        pass

    def main(self):
        pass

    def finalize(self):
        if self.verbosity >= self.NORMAL:
            self.stdout.write("Finished!")
