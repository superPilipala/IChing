import random


class Yao:
    def __init__(self, yao_value: int):
        self.yao = yao_value

        if self.yao == 1 | self.yao == 2:
            self.is_change = False
        else:
            self.is_change = True

        if self.yao == 1 | self.yao == 0:
            self.yin_yang = False
        else:
            self.yin_yang = True


# 周易
class IChing:
    # 四爻
    yin = 1
    yang = 2
    lao_yin = 0
    lao_yang = 3

    def __init__(self):
        self.divinatory: list[Yao] = []

    @property
    def cu_yao(self):
        return self.divinatory[0]

    @property
    def er_yao(self):
        return self.divinatory[1]

    @property
    def san_yao(self):
        return self.divinatory[2]

    @property
    def si_yao(self):
        return self.divinatory[3]

    @property
    def wu_yao(self):
        return self.divinatory[4]

    @property
    def shang_yao(self):
        return self.divinatory[5]

    @staticmethod
    def roll() -> bool:
        return random.choice([True, False])

    def get_yao(self) -> int:
        one = int(self.roll())
        two = int(self.roll())
        three = int(self.roll())
        return one + two + three

    def init_yaoes(self):
        for i in range(6):
            self.divinatory.append(Yao(self.get_yao()))

    def get_divinatory(self):
        self.init_yaoes()

# a = 0b1
# print(a<<2)
