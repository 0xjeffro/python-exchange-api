import okx.Account as Account

# doc: https://www.okx.com/docs-v5/zh/#trading-account-rest-api-get-balance


def main(args):
    apikey = args.get("apikey", None)
    secretkey = args.get("secretkey", None)
    passphrase = args.get("passphrase", None)
    if apikey is None or secretkey is None or passphrase is None:
        return {
            "body": {
                "functionCode": -1,
                "message": "apikey or secretkey or passphrase is None"
            }
        }
    else:
        flag = "0"  # Production trading:0 , demo trading:1
        accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
        result = accountAPI.get_account_balance()
        # print(result)

        return {
            "body": {
                "functionCode": 0,
                "message": "success",
                "data": result
            }
        }
