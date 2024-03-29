from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Relo",
    "SITE_HEADER": "Relo",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": False,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": False,  # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    "DASHBOARD_CALLBACK": "accounts.views.dashboard_callback",
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
        "redirect_after": lambda request: reverse_lazy("admin:index"),
    },
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Department"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Properties"),
                        "link": reverse_lazy("admin:department_property_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "link": reverse_lazy("admin:department_category_changelist"),
                    },
                    {
                        "title": _("Property Types"),
                        "link": reverse_lazy(
                            "admin:department_propertytype_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("CRM"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Clients"),
                        "link": reverse_lazy("admin:lead_client_changelist"),
                    },
                    {
                        "title": _("Client Groups"),
                        "link": reverse_lazy("admin:lead_clientgroup_changelist"),
                    },
                ],
            },
            # {
            #     "title": _("Places"),
            
            #     "separator": True,  # Top border
            #     "items": [
            #         {
            #             "title": _("Cites"),
            #             "link": reverse_lazy("admin:place_city_changelist"),
            #         },
            #         {
            #             "title": _("Countries"),
            #             "link": reverse_lazy("admin:place_country_changelist"),
            #         },
            #         {
            #             "title": _("Governors"),
            #             "link": reverse_lazy("admin:place_governorate_changelist"),
            #         },
            #     ],
            # },
        ],
    },
    "TABS": [
        {
            "models": ["lead.client", "lead.clientgroup"],
            "items": [
                {
                    "title": _("Clients"),
                    "link": reverse_lazy("admin:lead_client_changelist"),
                },
                {
                    "title": _("Client Groups"),
                    "link": reverse_lazy("admin:lead_clientgroup_changelist"),
                },
            ],
        },
        {
            "models": [
                "department.property",
                "department.category",
                "department.propertytype",
            ],
            "items": [
                {
                    "title": _("Properties"),
                    "link": reverse_lazy("admin:department_property_changelist"),
                },
                {
                    "title": _("Categories"),
                    "link": reverse_lazy("admin:department_category_changelist"),
                },
                {
                    "title": _("Property Types"),
                    "link": reverse_lazy("admin:department_propertytype_changelist"),
                },
            ],
        },
        {
            "models": [
                "place.city",
                "place.country",
                "place.governorate",
            ],
            "items": [
                {
                    "title": _("Cites"),
                    "link": reverse_lazy("admin:place_city_changelist"),
                },
                {
                    "title": _("Countries"),
                    "link": reverse_lazy("admin:place_country_changelist"),
                },
                {
                    "title": _("Governors"),
                    "link": reverse_lazy("admin:place_governorate_changelist"),
                },
            ],
        },
    ],
}


def models():
    from django.apps import apps

    model_list = apps.get_models()

    for model in model_list:
        print(model.__name__)


# models()
