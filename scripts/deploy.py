from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
    # get account
    # method 1, using brownie provided accounts
    # account = accounts[0]
    # print(account)

    # method2, using my own account
    # command line: brownie accounts new your_account_name
    # account = accounts.load("freecodecamp-account")
    # print(account)

    # method3, create .env file to save private_key
    # no need to enter eveytime, but less secure
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    # when working with network
    account = get_account()
    
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # need to wait for transaction to finish
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()