from conf import *
from urllib.request import urlopen, Request
import json
import pandas as pd


def get_kline_history_data(code, ktype):
    k_type = {'D': 'akdaily', 'W': 'akweekly', 'M': 'akmonthly'}
    url = DAY_PRICE_URL % (k_type[ktype], code)
    try:
        request = Request(url)
        lines = urlopen(request, timeout=10).read()
        if len(lines) < 15:  # 无数据
            return None
    except Exception as e:
        print(e)
    else:
        js = json.loads(lines.decode('utf-8'))
        cols = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20']
        df = pd.DataFrame(js['record'], columns=cols)
        df = df.applymap(lambda x: x.replace(u',', u''))
        df[df == ''] = 0
        for col in cols[1:]:
            df[col] = df[col].astype(float)
        df = df.set_index('date')
        df = df.sort_index(ascending=False)
        return df


if __name__ == '__main__':
    print(get_kline_history_data('sh000001', ktype='D'))
