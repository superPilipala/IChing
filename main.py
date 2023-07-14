from IChing.IChing import IChing


if __name__ == '__main__':
    ic = IChing()
    div = ic.get_divinatory()
    # if not div:
    print(div.model_dump())
    print(div.get_content())
