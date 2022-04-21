from datetime import datetime
import matplotlib.pyplot as plt  # data visualization
import numpy as np  # linear algebra
from matplotlib import ticker


def getFirstTimestamp(data):
    return datetime.fromtimestamp(data["Timestamp"][:1]).strftime("%d/%m/%Y %H:%M:%S")


def getLastTimestamp(data):
    return datetime.fromtimestamp(data["Timestamp"][-1:]).strftime("%d/%m/%Y %H:%M:%S")


def filterByInterval(coinbase, relativedelta):
    """
    Filter data by interval
    example: relativedelta => years=0, days=30
    """

    lastTimestamp = coinbase["Timestamp"][-1:]
    interval = (datetime.fromtimestamp(lastTimestamp) -
                relativedelta).timestamp()

    return coinbase[coinbase["Timestamp"] >= interval]


def hasMissingData(timestampList):
    """
    Verifica se possui intervalos diferentes de 60 segundos comparando o valor do iterador atual do array com o iterador anterior.

    Parameters:
        timestampList: Lista de valores timestamp -> list

    Return:
        False se não possui dados faltantes. True caso exista -> bool
    """
    missing = []
    for i in range(len(timestampList)):
        if i > 0 and (timestampList[i] - timestampList[i - 1] != 60):
            missing.append("{} {}".format(i, datetime.fromtimestamp(
                timestampList[i]), datetime.fromtimestamp(timestampList[i - 1])))

    if len(missing) == 0:
        return False

    print("Intervalos sem registros:")
    for i in missing:
        print(i)

    return True


def annot_max(x, y,  posX, posY, connectionstyle="angle,angleA=0,angleB=60", ax=None, mask="${:,.2f}"):
    text = mask.format(y)
    if ax is None:
        ax = plt.gca()

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(
        arrowstyle="->", connectionstyle=connectionstyle)
    kw = dict(xycoords='data', textcoords="data",
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top", fontsize=20)
    ax.annotate(text, xy=(x, y), xytext=(x+posX, y+posY), **kw)


def figureCloses(data, atribute, createFigure=True, showAnnotate=True, subtitle="Preço de Fechamento do Bitcoin em USD",
                 fontsize=20, mask_yaxis='${x:,.0f}', annot_yaxis=30000, annot_xaxis=20000, annot_xaxis_pos=-65000, annot_yaxis_pos=20000, angle=0, angle_pos=0):
    if createFigure:
        plt.figure(figsize=(14, 6))

    plt.suptitle(subtitle, fontsize=fontsize)
    plt.title("De {} Até {}".format(
        getFirstTimestamp(data), getLastTimestamp(data)), fontsize=14)
    plt.grid()
    plt.plot(data[atribute].values)
    ax = plt.gca()

    if showAnnotate:
        annot_max(0, data[atribute].values[0],
                  annot_xaxis, annot_yaxis, angle, ax)
        annot_max(len(data[atribute].values), data[atribute].values[-1],
                  annot_xaxis_pos, annot_yaxis_pos, angle_pos, ax)

    ax.get_xaxis().set_visible(False)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter(mask_yaxis))


def figureVolumeBtc(data, createFigure=True, showAnnotate=True, subtitle="Volume de movimentações do Bitcoin"):
    if createFigure:
        plt.figure(figsize=(7, 3))

    plt.suptitle(subtitle, fontsize=20)
    # plt.title("De {} Até {}".format(
    #     firstTimestamp, lastTimestamp), fontsize=14)
    plt.grid()
    plt.plot(data)
    ax = plt.gca()

    data2 = np.vectorize(lambda x: x if x >= 0 else 0)(data)
    index = np.argmax(data2)
    if showAnnotate:
        annot_max(index, data2[index],
                  100000, 0, "angle,angleA=0,angleB=-5", ax)
        # annot_max(len(data), data[-1],
        #           -65000, -20000, "angle,angleA=0,angleB=-90", ax)

    ax.get_xaxis().set_visible(False)


def hasMissingData(timestampList):
    """
    Verifica se possui intervalos diferentes de 60 segundos comparando o valor do iterador atual do array com o iterador anterior.

    Parameters:
        timestampList: Lista de valores timestamp -> list

    Return:
        False se não possui dados faltantes. True caso exista -> bool
    """
    missing = []
    for i in range(len(timestampList)):
        if i > 0 and (timestampList[i] - timestampList[i - 1] != 60):
            missing.append("{} {}".format(i, datetime.fromtimestamp(
                timestampList[i]), datetime.fromtimestamp(timestampList[i - 1])))

    if len(missing) == 0:
        return False

    print("Intervalos sem registros:")
    for i in missing:
        print(i)

    return True
