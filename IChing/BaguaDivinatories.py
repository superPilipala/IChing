from IChing.Divinatories import DivinatoryBase


class Qian(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '乾'
        self.value = 0b111


class Kan(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '坎'
        self.value = 0b010


class Gen(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '艮'
        self.value = 0b100


class Zhen(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '震'
        self.value = 0b001


class Xun(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '巽'
        self.value = 0b110


class Li(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '离'
        self.value = 0b101


class Kun(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '坤'
        self.value = 0b000


class Dui(DivinatoryBase):
    def __init__(self):
        super().__init__()
        self.name = '兑'
        self.value = 0b011
