import random
from IChing.Yao import Yao
from IChing.DivinatoryFactory import DivinatoryFactory


# 周易
class IChing:

    def __init__(self):
        # 卦象
        # # 变卦
        # self.changed_divinatory = 0
        # 主卦
        self.main_divinatory = 0

        # 变卦标识flag
        self.yao_index = 0b0
        # 变爻数量
        self.change_count = 0

        # 占卜结果
        self.origin_divinatories: list[Yao] = []

    # 起卦随机正反
    @staticmethod
    def roll() -> bool:
        return random.choice([True, False])

    # 3枚铜钱得到一爻
    def get_yao(self) -> int:
        one = int(self.roll())
        two = int(self.roll())
        three = int(self.roll())
        all = one + two + three
        return all

    # 6爻得到一卦
    def init_yaoes(self, byte_divinatories: list):

        if not byte_divinatories:
            # 起卦
            for i in range(6):
                byte_divinatories.append(self.get_yao())
        for div in byte_divinatories:
            self.origin_divinatories.append(Yao(div))

        index = 0
        for yao in self.origin_divinatories:
            # 得到爻
            a = yao.yin_yang << index

            # 检查是否是变爻
            if yao.is_change:
                self.change_count += 1
                self.yao_index = self.yao_index | (0b1 << index)

            # 得到本卦
            self.main_divinatory |= a

            index += 1

    # 返回卦象标识符
    def get_binary_divinatory(self):
        if self.main_divinatory:
            return self.main_divinatory
        else:
            raise "先初始化"

    # 得到卦象对象
    def get_divinatory(self):
        div_f = DivinatoryFactory()
        binary = self.get_binary_divinatory()
        div = div_f.get_divinatory(binary, self.yao_index)
        div.set_changeed_count(self.change_count)
        return div
