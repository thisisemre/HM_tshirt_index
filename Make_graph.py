import matplotlib.pyplot as plt
from datetime import datetime

def make_graph(x,y,x_label,y_label,tittle):
    current_date = datetime.now().strftime("%d %b %Y")
    new_tittle = tittle+" "+current_date
    plt.bar(x, y, color='green', width=0.8)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(new_tittle)

    plt.savefig(new_tittle)
