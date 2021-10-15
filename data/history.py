from aiogram.types import LabeledPrice

from utils.item import Item

Russia15_16 = Item(
    title="Россия на рубеже XV-XVI столетий",
    description="В книге автор прослеживает изменения экономической жизни, классовой борьбы, общественно-политической мысли, происшедшие в России после ее освобождения от иноземного ига. Используя большой фактический материал, автор исследует героические страницы истории Российского государства периода становления его на путь самостоятельного экономического и политического развития, когда ненавистное иго было уже сброшено. Большое внимание в книге уделено международной деятельности русского правительства, роли окрепшего государства в европейской политике.",
    payload="4",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Россия на рубеже XV-XVI столетий",
            amount=700_00
        )
    ],
    start_parameter="create_invoice_russia1516",
    photo_url="https://cdn1.ozone.ru/multimedia/c360/1005806139.jpg",
    photo_size=238,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Russian_history_17 = Item(
    title="История российская IX-XVII веков",
    description="Книга известного историка, профессора Санкт-Петербургского университета Р.Г.Скрынникова посвящена истории Русского государства с момента его образования в IX и до конца XVII века. Автор дает цельную концепцию исторического развития общества, включая политическую и социальную жизнь, уделяя значительное внимание культурным достижениям России и представляя галерею портретов деятелей Древней Руси и Московского царства.",
    payload="5",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="История российская IX-XVII веков",
            amount=1200_00
        )
    ],
    start_parameter="create_invoice_russianhistory",
    photo_url="https://cdn1.ozone.ru/multimedia/c360/1000453766.jpg",
    photo_size=200,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Ivan_the_terrible = Item(
    title="Иван Грозный",
    description="Царь Иван Грозный - пожалуй, одна из самых неоднозначных личностей российской истории. Талантливый государственный деятель, мудрый реформатор - и кровавый тиран, человек, ввергший свой народ в хаос чудовищных репрессий. Каким же он был, Иван Грозный, основатель Московского царства, государь, оказавший большое и весьма двусмысленное влияние на ход исторических событий? Какую роль он сыграл в образовании и упадке могущественной державы? Ответы на эти вопросы предлагает в своей увлекательной книге известный историк, ученый с мировым именем, профессор Санкт-Петербургского государственного университета Р.Г.Скрынников.",
    payload="6",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Иван Грозный",
            amount=10_00
        )
    ],
    start_parameter="create_invoice_ivantheterrible",
    photo_url="https://cdn1.ozone.ru/multimedia/c1200/1010774330.jpg",
    photo_size=446,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

history_list = [Russia15_16, Russian_history_17, Ivan_the_terrible]
