from algosdk import kmd, mnemonic
from algosdk.wallet import Wallet

kmd_token = "513da9f56b04078bd6721a5bb40519a7402922cc27a86cb2eb377a40bb9946a7"
kmd_address = "http://localhost:7833"

# create a kmd client
kcl = kmd.KMDClient(kmd_token, kmd_address)

walletid = None
wallets = kcl.list_wallets()
for arrayitem in wallets:
    if arrayitem.get("name") == "bob":
        walletid = arrayitem.get("id")
        break

wallethandle = kcl.init_wallet_handle(walletid, "")
accountkey = kcl.export_key(wallethandle, "", "5QX5D4HPXQIQ3ODMGN6NTH6GO435N5GJSA72FBKSJI4WCAJ5VAXWTAF6UU")
mn = mnemonic.from_private_key(accountkey)
print("Account Mnemonic: ", mn)
mnemonic_phrase = mn
account_private_key = mnemonic.to_private_key(mnemonic_phrase)
print("Private Key: ", account_private_key)
#vocal guard vintage kitten hood vacant calm naive foot shove vapor thunder sign friend bleak bean only between dream drum two range bounce about sing