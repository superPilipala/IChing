import random
from Divinatory.Yao import Yao
from Divinatory.divinatories import DivinatoryFactory


# 周易
class IChing:

    def __init__(self):
        # 卦象
        # 变卦
        self.changed_divinatory = 0
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
    def init_yaoes(self):
        # 起卦
        for i in range(6):
            self.origin_divinatories.append(Yao(self.get_yao()))

        index = 0
        for yao in self.origin_divinatories:
            print(yao.yao)
            # 得到爻
            a = yao.yin_yang << index

            # 检查是否是变爻
            if yao.is_change:
                self.change_count += 1
                self.yao_index = 0b1 << index

            # 得到本卦
            self.main_divinatory |= a

            index += 1

        # 变卦
        self.changed_divinatory = self.main_divinatory ^ self.yao_index

    # 返回卦象标识符
    def get_binary_divinatory(self):
        self.init_yaoes()
        print(bin(self.changed_divinatory))

        # 6爻皆变
        if self.yao_index == 6:
            return self.changed_divinatory
        else:
            return self.main_divinatory

    # 得到卦象对象
    def get_divinatory(self):
        div_f = DivinatoryFactory()
        binary = self.get_binary_divinatory()
        return div_f.get_divinatory(binary, self.yao_index)


if __name__ == '__main__':
    ic = IChing()
    div = ic.get_divinatory()
    print(div.name)
    # 测试
