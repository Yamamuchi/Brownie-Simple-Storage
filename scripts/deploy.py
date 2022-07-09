from lib2to3.pgen2.literals import simple_escapes
from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]

    # account = accounts.load("yamamuchi")

    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"Deployed contract: {simple_storage}")

    stored_value = simple_storage.retrieve()
    print(f"Stored value: {stored_value}")

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()
    print(f"Updated stored value: {updated_stored_value}")


def main():
    deploy_simple_storage()
