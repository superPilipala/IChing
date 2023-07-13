import numpy as np


# 六十四卦基类
class DivinatoryBase:

    def __init__(self):
        self.bagua = ['坤为地', '震为雷', '坎为水', '兑为泽', '艮为山', '离为火', '巽为风', '乾为天']
        self.name: str = '未知'
        self.value: int = 0

        self.up_name: str = '未知'
        self.down_name: str = '未知'
        self.change_flag = 0b0

    def get_div_name(self):
        return self.name

    def set_change_flag(self, change_flag):
        self.change_flag = change_flag

    def get_description(self):
        pass


# 六十四卦工厂基类
class DivinatoryFactoryBase:
    def __init__(self):
        # 卦象
        self.divinatories: list[list[DivinatoryBase]] = [[DivinatoryBase()] * 8] * 8

    def get_divinatory(self, binary_divinatory, change_flag):
        pass


class KunDivi(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '坤'
        self.value = 0b000000

        self.up_name = '坤'
        self.down_name = '坤'


class QianDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '乾'
        self.value = 0b111111

        self.up_name = '乾'
        self.down_name = '乾'


class GuaiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '夬'
        self.value = 0b011111

        self.up_name = '泽'
        self.down_name = '天'


class YouDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '有'
        self.value = 0b101111

        self.up_name = '火'
        self.down_name = '天'


class ZhuangDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '壮'
        self.value = 0b001111

        self.up_name = '雷'
        self.down_name = '天'


class XiaoXuDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '小蓄'
        self.value = 0b110111

        self.up_name = '风'
        self.down_name = '天'


class XuDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '需'
        self.value = 0b010111

        self.up_name = '坎'
        self.down_name = '乾'


# 卦象工厂
class DivinatoryFactory(DivinatoryFactoryBase):
    def __init__(self):
        super().__init__()
        self.divinatories[0b000][0b000] = KunDivi()
        self.divinatories[0b111][0b111] = QianDiv()
        self.divinatories[0b011][0b111] = GuaiDiv()
        self.divinatories[0b101][0b111] = YouDiv()
        self.divinatories[0b001][0b111] = ZhuangDiv()
        self.divinatories[0b110][0b111] = XiaoXuDiv()

    # 返回卦象
    def get_divinatory(self, binary_divinatory, change_flag):
        # 截取高位
        up = binary_divinatory >> 3
        # 截取低位
        down = binary_divinatory & 0b111
        divinatory = self.divinatories[up][down]

        divinatory.set_change_flag(change_flag)

        return divinatory
