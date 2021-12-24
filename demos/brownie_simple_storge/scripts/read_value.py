from brownie import SimpleStorage, accounts, config

def read_contract():
    # -1 is to get the most recent deployment
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()