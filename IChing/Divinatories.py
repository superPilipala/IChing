from pydantic import BaseModel, conint, field_serializer, Field
from enum import Enum
from IChing.CsvIO import CsvIO
from math import sqrt


class Bagua(BaseModel):
    name: str
    value: conint(le=8)


class BaguaEnum(Enum):
    Qian = Bagua(name='乾', value=0b111)
    Kun = Bagua(name='坤', value=0b000)
    Zhen = Bagua(name='震', value=0b001)
    Gen = Bagua(name='艮', value=0b100)
    Li = Bagua(name='离', value=0b101)
    Kan = Bagua(name='坎', value=0b010)
    Dui = Bagua(name='兑', value=0b011)
    Xun = Bagua(name='巽', value=0b110)


class Hexagram(BaseModel):
    # 卦名
    name: str
    # flag
    value: conint(le=64)
    # 卦序
    div_index: conint(le=65)
    # 上下卦
    up_div: BaguaEnum
    down_div: BaguaEnum
    # 变爻位置
    changed_flag: conint(le=64) = Field(None)
    # 变爻数量
    changed_count: conint(le=7) = 0

    @field_serializer('up_div')
    def serialize_up(self, up: BaguaEnum, _info):
        return up.name

    @field_serializer('down_div')
    def serialize_down(self, down: BaguaEnum, _info):
        return down.name

    def set_change_flag(self, changed_flag):
        self.changed_flag = changed_flag

    def set_changeed_count(self, cc):
        self.changed_count = cc

    def get_change_flag_array(self, flag) -> list[int]:
        flag_array = []
        if flag & 0b100000:
            flag_array.append(5)
        if flag & 0b10000:
            flag_array.append(4)
        if flag & 0b1000:
            flag_array.append(3)
        if flag & 0b100:
            flag_array.append(2)
        if flag & 0b10:
            flag_array.append(1)
        if flag & 0b1:
            flag_array.append(0)
        return flag_array


    def get_content(self) -> list[str]:
        contents = []
        csv_io = CsvIO()
        # 六爻不变，用本卦卦辞
        if self.changed_count == 0:
            contents.append(csv_io.get_content(self.value))
            return contents
        # 一个变爻，用变爻卦辞
        if self.changed_count == 1:
            yao_index = self.get_change_flag_array(self.changed_flag)[0]
            contents.append(csv_io.get_yao_content(self.value, yao_index))
            return contents
        # 两个变爻，用上爻为主，结合两个
        if self.changed_count == 2:
            flag_array = self.get_change_flag_array(self.changed_flag)
            up_yao_index = flag_array[0]
            contents.append(csv_io.get_yao_content(self.value, up_yao_index))
            down_yao_index = flag_array[1]
            contents.append(csv_io.get_yao_content(self.value, down_yao_index))
            return contents
        # 三个变爻，用本卦卦辞和变卦卦辞综合考虑
        if self.changed_count == 3:
            contents.append(csv_io.get_content(self.value))
            contents.append(csv_io.get_content(self.value ^ self.changed_flag))
            return contents
        # 四个变爻，用变卦另外两个静爻，下爻为主
        if self.changed_count == 4:
            flag_array = self.get_change_flag_array(~self.changed_flag)
            changed_value = self.value ^ self.changed_flag
            contents.append(csv_io.get_yao_content(changed_value, flag_array[1]))
            contents.append(csv_io.get_yao_content(changed_value, flag_array[0]))
            return contents
        # 五个变爻，用变卦静爻爻辞解释
        if self.changed_count == 5:
            flag_array = self.get_change_flag_array(~self.changed_flag)
            changed_value = self.value ^ self.changed_flag
            contents.append(csv_io.get_yao_content(changed_value, flag_array[0]))
            return contents
        # 六爻皆变，如果是乾坤二卦，用九，用六来解释，其他使用变卦卦辞
        if self.changed_count == 6:
            changed_value = self.value ^ self.changed_flag
            contents.append(csv_io.get_content(changed_value))
            return contents




# 字典转类
def dict_hexagram(d: dict) -> Hexagram | None:
    if d:
        return Hexagram(name=list(d['name'].values())[0], value=list(d['value'].values())[0],
                        div_index=list(d['div_index'].values())[0],
                        up_div=BaguaEnum[list(d['up_div'].values())[0]],
                        down_div=BaguaEnum[list(d['down_div'].values())[0]])
    else:
        return None
