from stellar_sdk import Asset, Server, Keypair, TransactionBuilder, Network
from dotenv import dotenv_values

config = dotenv_values(".env")

bob_address = 'GBQIZ5G4OY7SIYFUWJWJEKGGMTCW5SX54GCC3TF6REDFW7P2IBGMWJ3T'
global kp_alice


def prepare_transaction():
    server = Server("https://horizon.stellar.org")
    alice_account = server.load_account(kp_alice.public_key)

    asset_code = 'TFT'
    asset_issuer = 'GBOVQKJYHXRR3DX6NOX2RRYFRCUMSADGDESTDNBDS6CDVLGVESRTAC47'

    base_fee = server.fetch_base_fee()

    asset = Asset(asset_code, asset_issuer)
    transaction = (
        TransactionBuilder(
            source_account=alice_account,
            network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
            base_fee=base_fee,
        )
            .add_text_memo("Hello, Stellar!")
            .append_begin_sponsoring_future_reserves_op(bob_address)
            .append_change_trust_op(asset=asset, source=bob_address)
            .append_end_sponsoring_future_reserves_op(bob_address)
            .set_timeout(30)
            .build())

    print(transaction)


def get_fund_keypair():
    global kp_alice
    secret_alice = config['SECRET_BOB']

    kp_alice = Keypair.from_secret(secret_alice)


if __name__ == '__main__':
    get_fund_keypair()
    prepare_transaction()
