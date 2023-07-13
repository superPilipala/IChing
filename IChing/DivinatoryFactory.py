from IChing.HexagramDivinatories import *


# 六十四卦工厂基类
class DivinatoryFactoryBase:
    def __init__(self):
        # 卦象
        self.divinatories: list[list[DivinatoryBase]] = [[DivinatoryBase()] * 8] * 8

    def get_divinatory(self, binary_divinatory, change_flag):
        pass


# 卦象工厂
class DivinatoryFactory(DivinatoryFactoryBase):
    def __init__(self):
        super().__init__()
        self.divinatories[0b000][0b000] = KunDiv()
        self.divinatories[0b111][0b111] = QianDiv()
        self.divinatories[0b011][0b111] = GuaiDiv()
        self.divinatories[0b101][0b111] = DaYouDiv()
        self.divinatories[0b001][0b111] = DaYouDiv()
        self.divinatories[0b110][0b111] = XiaoXuDiv()

    # 返回卦象
    def get_divinatory(self, binary_divinatory, change_flag):
        # 截取高位
        up = binary_divinatory >> 3
        # 截取低位
        down = binary_divinatory & 0b111
        divinatory = self.divinatories[up][down]

        # 设置变爻
        divinatory.set_change_flag(change_flag)

        return divinatory
