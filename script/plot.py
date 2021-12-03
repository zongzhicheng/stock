# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe:
"""
# win64 直接pip install talib 会报错
# 到 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 里面下载与python版本适配的whl文件手动安装
# 例如：pip install packages/TA_Lib-0.4.21-cp38-cp38-win_amd64.whl
# import talib
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates


def kline_plot(df, start_time, end_time):
    df.index = list(map(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"), df.index))
    # 指定区间
    df = df[start_time:end_time]

    plt.figure("Daily K Line")
    plt.title("Daily K Line")
    plt.ylabel("Price")

    # x轴修改
    ax = plt.gca()
    # 设置主刻度定位器为周定位器（每周一显示主刻度文本）
    ax.xaxis.set_major_locator(matplotlib.dates.WeekdayLocator(byweekday=matplotlib.dates.MO))
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_minor_locator(matplotlib.dates.DayLocator())
    plt.tick_params(labelsize=8)
    plt.grid(linestyle=":")

    close = df['close']
    open = df['open']
    colors_bool = close >= open
    colors = np.zeros(colors_bool.size, dtype="U5")
    colors[:] = "green"
    colors[colors_bool] = "red"

    edge_colors = np.zeros(colors_bool.size, dtype="U1")
    edge_colors[:] = "g"
    edge_colors[colors_bool] = "r"

    dates = df.index
    plt.plot(dates, open, color="b", linestyle="--", linewidth=2, label="open", alpha=0.3)

    plt.bar(dates, (close - open), 0.8, bottom=open, color=colors, edgecolor=edge_colors, zorder=3)

    # 7.绘制蜡烛直线(最高价与最低价)
    plt.vlines(dates, df['low'], df['high'], color=edge_colors)

    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('../600519.csv', index_col=0)
    start_time = '2021-11-01'
    end_time = '2021-12-01'
    kline_plot(df, start_time, end_time)
