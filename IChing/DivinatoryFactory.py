from IChing.CsvIO import *
from IChing.Divinatories import *

# 六十四卦工厂基类
class DivinatoryFactoryBase:
    def __init__(self):
        pass
        # # 卦象
        # self.divinatories: list[list[Hexagram]] = [[DivinatoryBase()] * 8] * 8

    def get_divinatory(self, binary_divinatory, change_flag):
        pass


# 卦象工厂
class DivinatoryFactory(DivinatoryFactoryBase):
    def __init__(self):
        super().__init__()

    # 返回卦象
    def get_divinatory(self, binary_divinatory, change_flag) -> Hexagram | None:
        # # 截取高位
        # up = binary_divinatory >> 3
        # # 截取低位
        # down = binary_divinatory & 0b111

        csv_io = CsvIO()
        dict_data = csv_io.get_hexagram_dict(binary_divinatory)

        divinatory = dict_hexagram(dict_data)

        if divinatory:
            # 设置变爻
            divinatory.set_change_flag(change_flag)

            return divinatory

        else:
            return None
