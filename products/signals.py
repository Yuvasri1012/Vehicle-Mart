# from django.db.models.signals import post_migrate
# from django.dispatch import receiver

# @receiver(post_migrate)
# def create_default_categories(sender, **kwargs):
#     if sender.name != "products":
#         return

#     from django.apps import apps
#     Category = apps.get_model("products", "Category")

#     default_categories = [
#         "Car","Bike","Scooter","Bicycle","Electric Car","Electric Bike",
#         "Auto Rickshaw","Bus","Truck","Van","SUV","Pickup",
#         "Tractor","Ambulance","Luxury Car","Sports Bike"
#     ]

#     for cat in default_categories:
#         Category.objects.get_or_create(name=cat)

#     print("Default categories added ✅")