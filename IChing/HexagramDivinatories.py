from IChing.Divinatories import DivinatoryBase
from IChing.BaguaDivinatories import *


# 64卦

# 1乾为天
class QianDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '乾'
        self.value = 0b111111
        self.index = 1

        self.up_div = Qian
        self.down_div = Qian


# 2 坤为地
class KunDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '坤'
        self.value = 0b000000
        self.index = 2

        self.up_div = Kun()
        self.down_div = Kun()


# 3 水雷屯(Zhun)
class ZhunDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 3
        self.name = '屯'
        self.value = 0b010001

        self.up_div = Dui
        self.down_div = Zhen


# 4 山水蒙
class MengDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 4
        self.name = '蒙'
        self.value = 0b100010

        self.up_div = Gen
        self.down_div = Kan


# 5 水天需
class XuDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 5
        self.name = '需'
        self.value = 0b010111

        self.up_div = Kan
        self.down_div = Qian


# 6 天水讼
class SongDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 6
        self.name = '讼'
        self.value = 0b111010

        self.up_div = Qian
        self.down_div = Dui


# 7 地水师
class ShiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 7
        self.name = '师'
        self.value = 0b000010

        self.up_div = Kun
        self.down_div = Dui


# 8 水地比
class BiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 8
        self.name = '比'
        self.value = 0b010000

        self.up_div = Dui
        self.down_div = Kun


# 9 风天小畜(xu)
class XiaoXuDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 9
        self.name = '小畜'
        self.value = 0b110111

        self.up_div = Xun
        self.down_div = Qian


# 10 天泽履
class LvDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 10
        self.name = '履'
        self.value = 0b111101

        self.up_div = Qian
        self.down_div = Dui


# 11 地天泰
class TaiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 11
        self.name = '泰'
        self.value = 0b000111

        self.up_div = Kun
        self.down_div = Qian


# 12 天地否(pi)
class PiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 12
        self.name = '否'
        self.value = 0b111000

        self.up_div = Qian
        self.down_div = Kun


# 13 天火同人卦
class TongRenDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.index = 13
        self.name = '同人'


# 山天大畜
class DaChuDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '大畜'
        self.value = 0b100111

        self.up_div = ''


# 雷天大壮
class DaZhuangDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '壮'
        self.value = 0b001111

        self.up_div = Zhen
        self.down_div = Qian


# 火天大有
class DaYouDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '有'
        self.value = 0b101111

        self.up_div = Li
        self.down_div = Qian


# 泽天夬
class GuaiDiv(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '夬'
        self.value = 0b011111

        self.up_div = Dui
        self.down_div = Qian
