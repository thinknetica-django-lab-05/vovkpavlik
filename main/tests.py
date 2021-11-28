from django.test import TestCase


from django.contrib.auth.models import User
from main.models import Category, Ad, Seller, Tag


#Create users
users = ["guest_1", "guest_2", "guest_3"]
for user in users:
    User.objects.create_user(user, password=user)


#Create sellers
users = User.objects.all()

for user in users:
    Seller.objects.create(user=user)


#Create categories
categories = ["Антиквариат", "Музыкальное оборудование", "Одежда", "Копьютерная техника"]

for category in categories:
    Category.objects.create(title=category)


#Create ads
user_guest_1 = User.objects.get(username='guest_1')
user_guest_2 = User.objects.get(username='guest_2')
user_guest_3 = User.objects.get(username='guest_3')

seller_1 = Seller.objects.get(user=user_guest_1)
seller_2 = Seller.objects.get(user=user_guest_2)
seller_3 = Seller.objects.get(user=user_guest_3)

anticvar = Category.objects.get(title='Антиквариат')
music = Category.objects.get(title='Музыкальное оборудование')
clothes = Category.objects.get(title='Одежда')
comp = Category.objects.get(title='Копьютерная техника')

elephant_s_1 = Ad.objects.create(seller=seller_1, category=anticvar, title="Слоновый бивень", description="Большая слоновая кость")
piano_s_1 = Ad.objects.create(seller=seller_1, category=music, title="Старое фортепиано", description="Досталось от бабушки. Состояние - отличное")
gun_s_1 = Ad.objects.create(seller=seller_1, category=anticvar, title="Ружье 18 века", description="Не стреляет")

guitar_s_2 = Ad.objects.create(seller=seller_2, category=music, title="Гитара Курта Кобейна", description="Настоящая")
piano_s_2 = Ad.objects.create(seller=seller_2, category=music, title="Фортепиано", description="Фортепиано из слоновой кости")
hat_s_2 = Ad.objects.create(seller=seller_2, category=clothes, title="Шляпа-циллиндр", description="Настоящая шляпа Авраама Линкольна")

notebook_s_3 = Ad.objects.create(seller=seller_3, category=comp, title="Macbook 13 Pro Retina/256gb", description="Новый ноутбук в хорошем состоянии")
monitor_s_3 = Ad.objects.create(seller=seller_3, category=comp, title="Монитор Dell, 25' ", description="Игровой 144 гц монитор со встроенными динамиками")
audio_system = Ad.objects.create(seller=seller_3, category=music, title="Мониторы для сведения JBL", description="Одни из первых аудио-систем для звукорежисеров. Почти антиквариат!")


tag_anticvariat = Tag.objects.create(title="Антиквариат")
tag_exotic = Tag.objects.create(title="Экзотика")
tag_elephant_bone = Tag.objects.create(title="Слоновая кость")
tag_old = Tag.objects.create(title="Предметы старины")
tag_gun = Tag.objects.create(title="Оружие")
tag_music = Tag.objects.create(title="музыка")
tag_clothes = Tag.objects.create(title="Одежда")
tag_notebooks = Tag.objects.create(title="Ноутбуки")
tag_work = Tag.objects.create(title="Для работы")
tag_comp = Tag.objects.create(title="Компьютерная техника")


elephant_s_1.tag.set([tag_anticvariat, tag_exotic, tag_elephant_bone])
piano_s_1.tag.set([tag_anticvariat, tag_old, tag_music])
gun_s_1.tag.set([tag_anticvariat, tag_old, tag_gun])

guitar_s_2.tag.set([tag_anticvariat, tag_music, tag_exotic])
piano_s_2.tag.set([tag_anticvariat, tag_music, tag_exotic, tag_elephant_bone])
hat_s_2.tag.set([tag_anticvariat, tag_clothes, tag_old])

notebook_s_3.tag.set([tag_notebooks, tag_work, tag_comp])
monitor_s_3.tag.set([tag_music, tag_work, tag_comp])
audio_system.tag.set([tag_work, tag_comp, tag_music, tag_anticvariat])


#Filter by category
filter_by_anticvariat = Ad.objects.filter(category=anticvar)
filter_by_music = Ad.objects.filter(category=music)
filter_by_clothes = Ad.objects.filter(category=clothes)
filter_by_comp = Ad.objects.filter(category=comp)


# Count ads for sellers
for seller in Seller.objects.all():
    filter_sellers = Ad.objects.filter(seller=seller)
    filter_sellers.count()



