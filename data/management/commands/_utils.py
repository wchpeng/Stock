import easyquotation

conditions = ['sina', 'tencent', 'qq']


def get_all_stock_info():
    data = {}

    for cond in conditions:
        quote = easyquotation.use(cond)
        data = quote.market_snapshot(prefix=True)
        if data:
            break

    return data
