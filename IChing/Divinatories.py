from pydantic import BaseModel, conint, field_serializer
from enum import Enum


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
    changed_flag: conint(le=64)

    @field_serializer('up_div')
    def serialize_up(self, up: BaguaEnum, _info):
        return up.name

    @field_serializer('down_div')
    def serialize_down(self, down: BaguaEnum, _info):
        return down.name


def dict_hexagram(d: dict):
    return Hexagram(name=d['name'][0], value=d['value'][0], div_index=d.get('div_index')[0], changed_flag=d.get('changed_flag')[0],
                    up_div=BaguaEnum[d['up_div'][0]],
                    down_div=BaguaEnum[d['down_div'][0]])
