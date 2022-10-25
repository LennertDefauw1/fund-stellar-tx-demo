import asyncio

from stellar_sdk import Asset, ServerAsync, Keypair, TransactionBuilder, Network
from stellar_sdk.client.aiohttp_client import AiohttpClient

from dotenv import dotenv_values


config = dotenv_values(".env")

address_bob = 'GBQIZ5G4OY7SIYFUWJWJEKGGMTCW5SX54GCC3TF6REDFW7P2IBGMWJ3T'
global kp_alice


def get_fund_keypair():
    global kp_alice
    kp_alice = config['SECRET_BOB']


if __name__ == '__main__':
    get_fund_keypair()
