from aiogram import types

POST_REGULAR_SHIPPING = types.ShippingOption(
    id="regular_sh",
    title="Почтой",
    prices=[
        types.LabeledPrice(
            "Обычная упаковка", 0
        ),
        types.LabeledPrice(
            "Почта", 500_00
        ),
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="vip_sh",
    title="Срочная доставка почтой",
    prices=[
        types.LabeledPrice(
            "Прочная упаковка", 1000_00
        ),
        types.LabeledPrice(
            "Доставка в течение 3 дней по России", 3000_00
        ),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id="pick_up",
    title="Самовывоз",
    prices=[
        types.LabeledPrice(
            "Самовывоз", 0
        )
    ]
)
