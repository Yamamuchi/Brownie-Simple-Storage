from brownie import accounts, config


def deploy_simple_storage():
    # account = accounts[0]
    # print(account)

    # account = accounts.load("yamamuchi")
    # print(account)

    account = accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
