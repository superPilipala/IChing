class Yao:
    # 四爻
    yin = 1
    yang = 2
    lao_yin = 0
    lao_yang = 3

    def __init__(self, yao_value: int):
        self.yao = yao_value

        if (self.yao == 1) | (self.yao == 2):
            self.is_change = False
        else:
            self.is_change = True

        if self.yao <= 1:
            self.yin_yang = False
        else:
            self.yin_yang = True

    # 获取是否是变爻
    def get_is_change(self):
        return self.is_change

    # 得到阴阳
    def get_yin_yang(self):
        return self.yin_yang
