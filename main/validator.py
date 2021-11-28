import re

from django.core.exceptions import ValidationError


def validate_itn(inn):
    pattern = "\D"
    symbols = re.search(pattern, inn)
    if symbols:
        raise ValidationError(
            "inn must contains numbers",
            params={"inn": inn}
        )

    # try:
    #     int(inn)
    # except ValueError:
    #     raise ValidationError(
    #         "inn must contains numbers",
    #         params={"inn": inn}
    #     )

    if len(inn) not in (10, 12):
        raise ValidationError(
            "inn contains the wrong number of characters",
            params={"inn": inn}
        )

    def inn_csum(inn):
        k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
        pairs = zip(k[11 - len(inn):], [int(x) for x in inn])
        return str(sum([k * v for k, v in pairs]) % 11 % 10)

    if len(inn) == 10:
        if inn[-1] != inn_csum(inn[:-1]):
            raise ValidationError(
                "enter the correct inn",
                params={"inn": inn}
            )
    elif inn[-2:] != inn_csum(inn[:-2]) + inn_csum(inn[:-1]):
        raise ValidationError(
            "enter the correct inn",
            params={"inn": inn}
            )
