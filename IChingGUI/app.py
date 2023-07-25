from abc import abstractmethod, ABCMeta

from IChing.IChing import IChing


class Apps(metaclass=ABCMeta):
    def __init__(self):
        self.ic = IChing()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_divinatory(self):
        pass


class TerminalApp(Apps):
    def run(self):
        div = self.get_divinatory()
        contens = div.get_content()
        for content in contens:
            print(content)

    def get_divinatory(self):
        temp = []
        for i in range(6):
            yao = self.ic.get_yao()
            if yao == 0:
                print("三反，为老阴")
            if yao == 1:
                print("两反一正，为少阴")
            if yao == 2:
                print("两正一反，为少阳")
            if yao == 3:
                print("三正，为老阳")

            temp.append(yao)

        self.__show_yaos(temp)

        self.ic.init_yaoes(temp)

        return self.ic.get_divinatory()

    def __show_yaos(self, divs: list):
        str = ''
        for yao in divs:
            if yao == 0:
                str = 'x\n'+str
            if yao == 1:
                str = '--\n'+str
            if yao == 2:
                str = '——\n'+str
            if yao == 3:
                str = 'o\n'+str
        print(str)
