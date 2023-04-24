from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth
from brownie import interface, config, network
from web3 import Web3

Amount=Web3.toWei(0.1,"ether")
def main ():
    account=get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    #get_weth()
    if network.show_active() in ["mainnet-fork"]:
        get_weth()

    pool = get_pool()
    print( pool)
    approve_ERC20(Amount,pool.address,erc20_address,account)
    print("Depositing ")
    tx=pool.deposit(erc20_address,Amount,account.address,0,{"from":account})
    tx.wait(1)
    print("Deposited")
    

def get_pool():
    #ABI
    #Address
    pool_addresses_provider=interface.IPoolAddressesProvider(
        config["networks"][network.show_active()]["pool_addresses_provider"]
        
    )
    pool_address=pool_addresses_provider.getPool()
    pool_abi=interface.IPool(pool_address)
    return pool_abi

   
   
   


def approve_ERC20(amount,spender,erc20_address,account):
    print("Approving Token... ")
    erc20=interface.IERC20(erc20_address)
    tx=erc20.approve(spender,amount,{"from":account})
    tx.wait(1)
    print("Approvedddd!!")
    return tx 


    


