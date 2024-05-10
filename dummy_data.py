import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product , Brand , Review
 


def seed_brand(n):
    fake=Faker()
    images = ['1.png','2.png','3.png','4.png','5.png']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image=f"brand/{images[random.randint(0,4)]}",
        )
    print(f"{n} add brand successfully")



def seed_products(n):
    fake=Faker()
    flag_type=['New','sale','feature']
    brands = Brand.objects.all()
    images = ['1.png','2.png','3.png','4.png','5.png']
    for _ in range(n):

        Product.objects.create(
            name = fake.name(),
            flag = flag_type[random.randint(0,2)],
            price = round(random.uniform(20.99,99.99),2),
            image = f"product/{images[random.randint(0,4)]}",
            sku = random.randint(100,1000000),
            subtitle = fake.text(max_nb_chars=450),
            description = fake.text(max_nb_chars=4000),
            brand = brands[random.randint(0,len(brands)-1)],
            quantity = 1,


        )
    print(f"{n} add product successfully")




def seed_reviws(n):
    pass


seed_brand(200)
seed_products(1500)