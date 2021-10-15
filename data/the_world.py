from aiogram.types import LabeledPrice

from utils.item import Item

Spark_of_life = Item(
    title="Искра жизни",
    description="Все знают, что электричество приводит в действие машины, гораздо менее известно, что это же самое можно сказать о нас самих. Способность читать и понимать написанное, видеть и слышать, думать и говорить, шевелить руками и ногами и даже осознавать собственное Я обусловлена электрической активностью клеток, которая инициируется ионными каналами. Они регулируют наши жизненные процессы с момента зачатия и до последнего вздоха. Эта книга - почти детектив, посвященный особой разновидности белковой материи, ионному каналу. Она дает ответы на множество вопросов. Что происходит во время сердечного приступа? Можно ли на самом деле умереть от страха? Почему электрический угорь может ударить током? Как действуют на организм яды? Что в действительности делает ботокс? Что спасло Джеймса Бонда, когда его отравили? Зачем едят фугу? Почему в поздних картинах Клода Моне преобладают красные и желтые тона? Действительно ли любовь - химический феномен?",
    payload="7",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Искра жизни",
            amount=1000_00
        )
    ],
    start_parameter="create_invoice_sparkoflife",
    photo_url="https://s1.livelib.ru/boocover/1001105185/o/26ae/Frensis_Eshkroft__Iskra_zhizni._Elektrichestvo_v_tele_cheloveka.jpeg",
    photo_size=426,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Widened_phenotype = Item(
    title="Расширенный фенотип",
    description="«Расширенный фенотип» — книга английского этолога, биолога и популяризатора науки Ричарда Докинза, профессора Оксфордского университета. «Расширенный фенотип» развивает идеи предыдущей книги автора — «Эгоистичного гена», в которой эволюция и естественный отбор рассматриваются с точки зрения конкуренции генов.",
    payload="8",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Расширенный фенотип",
            amount=1000_00
        )
    ],
    start_parameter="create_invoice_widenedphenotype",
    photo_url="https://cdn1.ozone.ru/s3/multimedia-k/6010253288.jpg",
    photo_size=1725,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

The_origins_of_life = Item(
    title="Происхождение жизни",
    description="Поражаясь красоте и многообразию окружающего мира, люди на протяжении веков гадали: как он появился? Каким образом сформировались планеты, на одной из которых зародилась жизнь? Почему земная жизнь основана на углероде и использует четыре типа звеньев в ДНК?",
    payload="9",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Происхождение жизни",
            amount=1500_00
        )
    ],
    start_parameter="create_invoice_theoriginsoflife",
    photo_url="https://cdn1.ozone.ru/multimedia/1015094541.jpg",
    photo_size=788,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Selfish_gene = Item(
    title="Эгоистичный ген",
    description="«Эгоисти́чный ген» — научно-популярная книга о биологической эволюции, написанная британским биологом Ричардом Докинзом и впервые опубликованная в 1976 году. Основная идея книги состоит в обосновании геноцентричного взгляда на эволюцию.",
    payload="10",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Эгоистичный ген",
            amount=1500_00
        )
    ],
    start_parameter="create_invoice_selfishgene",
    photo_url="https://cdn1.ozone.ru/s3/multimedia-p/6036763657.jpg",
    photo_size=852,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

Brain_and_soul = Item(
    title="Мозг и душа",
    description="Знаменитый британский нейрофизиолог Крис Фрит хорошо известен умением говорить просто об очень сложных проблемах психологии - таких как психическая деятельность, социальное поведение, аутизм и шизофрения. Именно в этой сфере, наряду с изучением того, как мы воспринимаем окружающий мир, действуем, делаем выбор, помним и чувствуем, сегодня и происходит научная революция, связанная с внедрением методов нейровизуализации. В книге \"Как работает мозг\" Крис Фрит рассказывает обо всем этом самым доступным и занимательным образом",
    payload="11",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="Мозг и душа",
            amount=1000_00
        )
    ],
    start_parameter="create_invoice_brainandsoul",
    photo_url="https://cdn1.ozone.ru/s3/multimedia-m/c1200/6066427258.jpg",
    photo_size=893,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

the_world_list = [Spark_of_life, Widened_phenotype, The_origins_of_life, Selfish_gene, Brain_and_soul]
