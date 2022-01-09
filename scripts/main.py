import asyncio
from starknet.contract import Contract
from starknet.net.client import Client

client = Client("http://localhost:5000")

with open("./contracts/first_contract.cairo", "r") as f:
    file = f.read()

async def deploy() -> Contract:
    contract = await Contract.deploy(client, file)
    return contract

async def increase_balance(contract: Contract):
    invocation = await contract.functions['increase_balance'].invoke(amount=1)
    await invocation.wait_for_acceptance()

async def get_balance(contract: Contract):
    balance = await contract.functions['get_balance'].call()
    return balance

if __name__ == "__main__":
    contract = asyncio.get_event_loop().run_until_complete(deploy())
    asyncio.get_event_loop().run_until_complete(increase_balance(contract))
    balance = asyncio.get_event_loop().run_until_complete(get_balance(contract))
    print(balance.res)