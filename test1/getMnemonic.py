from algosdk import kmd, mnemonic
from algosdk.wallet import Wallet

kmd_token = "450a05c45116374a157a032766e569e7143422eb843d60fe071e0d3d9cab58f3"
kmd_address = "http://localhost:39505"

# create a kmd client
kcl = kmd.KMDClient(kmd_token, kmd_address)

walletid = None
wallets = kcl.list_wallets()
for arrayitem in wallets:
    if arrayitem.get("name") == "unencrypted-default-wallet":
        walletid = arrayitem.get("id")
        break

wallethandle = kcl.init_wallet_handle(walletid, "")
accountkey = kcl.export_key(wallethandle, "", "4Q7QX52TW7TJARQGYYWV2RDRGL7LEUK34WXQECKDCLBTCLGNBEDXAAJ2YY")
mn = mnemonic.from_private_key(accountkey)
print("Account Mnemonic: ", mn)
mnemonic_phrase = mn
account_private_key = mnemonic.to_private_key(mnemonic_phrase)
print("Private Key: ", account_private_key)
#vocal guard vintage kitten hood vacant calm naive foot shove vapor thunder sign friend bleak bean only between dream drum two range bounce about sing