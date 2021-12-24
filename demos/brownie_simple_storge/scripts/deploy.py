from brownie import accounts, config, network, SimpleStorage


def deploy_simple_storage():
    # Load account from the ganache instance created by brownie
    # account = accounts[0]
    # Load from an account that was created by manually importing to brownie account details
    # account = accounts.load("freecodecamp-account")
    # Load account from .env file
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    simplae_storage = SimpleStorage.deploy({"from": account})
    stored_value = simplae_storage.retrieve()
    print(stored_value)
    transaction = simplae_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simplae_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active == "devlopment":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
