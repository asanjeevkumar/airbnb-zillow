import matplotlib.pyplot as plt


def gen_bar_plot_horizon(x_column, y_column, x_label="", y_label="", title="Real estate"):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(x_column, y_column, align='center')
    ax.set_yticks(x_column.unique())
    ax.set_yticklabels(x_column.unique())
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.savefig("bv1p.png")


def create_plots(airbnb_df, zillow_df):
    # price vs bedroom
    airbnb_df_filtered = airbnb_df[airbnb_df["bedrooms"] <= 2]
    price = airbnb_df_filtered["price"].str.replace("$", "").str.replace(",", "").astype(float)
    bedrooms = airbnb_df_filtered["bedrooms"]

    gen_bar_plot_horizon(bedrooms, price, x_label="Price", title="Price for bedroom")

    # graph showing property type
    property_type = airbnb_df["property_type"]
    pt = property_type.cumsum()
    pt.plot(kind="bar")
    plt.savefig("pt.png")
