from pydantic import BaseModel, conint, field_serializer, Field
from enum import Enum
from IChing.CsvIO import CsvIO


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

    def get_content(self):
        csv_io = CsvIO()
        if self.changed_count == 0:
            return csv_io.get_content(self.value)
        if self.changed_count == 1:
            yao_index = self.changed_flag/2-1
            print(yao_index)
            return csv_io.get_yao_content(self.value, yao_index)


# 字典转类
def dict_hexagram(d: dict) -> Hexagram | None:
    if d:
        return Hexagram(name=list(d['name'].values())[0], value=list(d['value'].values())[0],
                        div_index=list(d['div_index'].values())[0],
                        up_div=BaguaEnum[list(d['up_div'].values())[0]],
                        down_div=BaguaEnum[list(d['down_div'].values())[0]])
    else:
        return None
