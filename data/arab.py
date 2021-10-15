from aiogram.types import LabeledPrice

from utils.item import Item

Kuzmin_studentsbook = Item(
    title="Учебник Кузьмина",
    description="Учебник рассчитан на одногодичный курс обучения в вузах и двух-трёхгодичное обучение в лицеях. Он ориентирован на выработку коммуникативных навыков, снабжен прописями, аудиозаписью ряда текстов и может служить в качестве самоучителя. Предыдущие издания учебника вышли в 2001.2003,2005 и 2009 годах.",
    payload="1",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Учебник Кузьмина",
            amount=101_00
        )
    ],
    start_parameter="create_invoice_Kuzmin_studentsbook",
    photo_url="https://s1.livelib.ru/boocover/1001524106/o/b7a2/Sergej_Kuzmin__Uchebnik_arabskogo_yazyka_dlya_pervogo_goda_obucheniya.jpeg",
    photo_size=1200,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Yakovenko_studentsbook = Item(
    title="Учебник Яковенко",
    description="Учебник создавался в рамках образовательных стандартов нового поколения и впервые в российской учебной литературе охватывает в столь полном объеме грамматические темы арабского языка, предназначенные для изучения на продвинутом этапе. Для студентов, уже владеющих основами арабского языка и изучающих этот язык как основной в пределах академического уровня Бакалавриат на втором году обучения.",
    payload="2",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Учебник Яковенко",
            amount=2_000_00
        )
    ],
    start_parameter="create_invoice_Yakovenko_studentsbook",
    photo_url="https://18.img.avito.st/640x480/9209480018.jpg",
    photo_size=497,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Yakovenko_studentsbook_polit = Item(
    title="Учебник Яковенко по политпереводу",
    description="Учебное пособие предназначено для студентов, изучающих арабский язык и уже владеющих основами арабской грамматики. Структура пособия и принцип распределения нового материала по урокам позволяют активно закреплять пройденное. Звуковая иллюстрация текстов на прилагаемом диске призвана способствовать развитию навыков восприятия арабской речи, учит понимать и переводить арабские тексты, развивает технику речи.",
    payload="3",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Учебник Яковенко по политпереводу",
            amount=1000_00
        )
    ],
    start_parameter="create_invoice_Yakovenko_studentsbook_polit",
    photo_url="https://www.centrmag.ru/catalog/av11_270717.jpg",
    photo_size=1050,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

arab_list = [Kuzmin_studentsbook, Yakovenko_studentsbook, Yakovenko_studentsbook_polit]
