from brownie import SimpleStorage, accounts, config

def read_contract():
    # print(SimpleStorage[0])
    # 0 is the first deployement, -1 is the latest deployment
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()
