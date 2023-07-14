from IChing.IChing import IChing
from IChingGUI.MainApp import *


def iching_test():
    ic = IChing()
    div = ic.get_divinatory()
    # if not div:
    print(div.model_dump())
    print(div.get_content())


if __name__ == '__main__':
    ma=MainApp()
    ma.run()