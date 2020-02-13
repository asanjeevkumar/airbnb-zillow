import matplotlib as plt


def gen_bar_plot_horizon(x_column, y_column):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(x_column, y_column, align='center')
    ax.set_yticks(x_column)
    ax.set_yticklabels(x_column.unique())
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()


def gen_
