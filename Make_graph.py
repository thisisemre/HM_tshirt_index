import matplotlib.pyplot as plt


def make_graph(x,y,x_label,y_label,tittle):

    plt.bar(x, y, color='green', width=0.8)

    plt.xlabel(x_label)

    plt.ylabel(y_label)

    plt.title(tittle)

    plt.savefig(tittle)
