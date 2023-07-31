import okx.Funding as Funding

# doc: https://www.okx.com/docs-v5/zh/#funding-account-rest-api-get-balance


def main(args):
    apikey = args.get("apikey", None)
    secretkey = args.get("secretkey", None)
    passphrase = args.get("passphrase", None)
    ccy = args.get("ccy", None)

    if apikey is None or secretkey is None or passphrase is None:
        return {
            "body": {
                "functionCode": -1,
                "message": "apikey or secretkey or passphrase is None"
            }
        }
    elif ccy is None:
        return {
            "body": {
                "functionCode": -1,
                "message": "ccy is None"
            }
        }
    else:
        flag = "0"  # Production trading:0 , demo trading:1
        accountAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
        result = accountAPI.get_balances(ccy)
        # print(result)

        return {
            "body": {
                "functionCode": 0,
                "message": "success",
                "data": result
            }
        }
