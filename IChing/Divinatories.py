# 六十四卦基类
class DivinatoryBase:

    def __init__(self):
        self.name: str = '未知'
        self.value: int = 0

        # 卦序
        self.index: int = -1

        # 上下卦
        self.up_div: DivinatoryBase = None
        self.down_div: DivinatoryBase = None
        # 变爻标识符
        self.change_flag = 0b0

    def get_div_name(self):
        return self.name

    def set_change_flag(self, change_flag):
        self.change_flag = change_flag

    def get_description(self):
        pass


