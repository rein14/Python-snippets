#  hashCode = f"{iPayData['live']}{iPayData['oid']}{iPayData['inv']}{iPayData['amount']}{iPayData['tel']}{iPayData['eml']}{iPayData['vid']}{iPayData['curr']}{iPayData['p1']}{iPayData['p2']}{iPayData['p3']}{iPayData['p4']}{iPayData['cst']}{iPayData['cbk']}"
#     h = hmac.new(iPaySecret, bytes(hashCode, 'utf-8'), hashlib.sha256)
#     hash = h.hexdigest()
#     iPayData["hash"] = hash 