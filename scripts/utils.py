import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["figure.figsize"] = (20, 6)


def gen_bar_plot_horizon(
        x_column, y_column, x_label="", y_label="", title="Real estate",
        output="price_vs_bedroom.png"):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(x_column, y_column, align='center')
    ax.set_yticks(x_column.unique())
    ax.set_yticklabels(x_column.unique())
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.savefig(output)


def create_plots(airbnb_df, zillow_df, output_dir=''):
    # price vs bedroom
    airbnb_df_filtered = airbnb_df[airbnb_df["bedrooms"] <= 2]
    price = airbnb_df_filtered["price"].str.replace("$", "").str.replace(",", "").astype(float)
    bedrooms = airbnb_df_filtered["bedrooms"]

    #gen_bar_plot_horizon(bedrooms, price, x_label="Price", title="Price for bedroom",
    #                     output=output_dir+"/price_vs_bedroom.png")

    # graph showing property type
    make_hist(airbnb_df, column="property_type", output=output_dir+"/property_type_hist.png")

    # graph showing bedrooms
    make_hist(airbnb_df, column="bedrooms", output=output_dir + "/bedrooms_hist.png")

    # graph showing zipcode hist
    make_hist(airbnb_df, column="zipcode", output=output_dir + "/zipcode_property_hist.png")


def make_hist(airbnb_df, column, output="property_hist.png"):
    d = pd.DataFrame({column: airbnb_df[column]})
    vc = d.apply(pd.value_counts)
    ax = vc[vc > 10].plot(kind="bar")
    plt.xticks(rotation=90)
    plt.savefig(output)


def make_radviz(df, name="Radviz plot"):
    df = df.filter(["bedroom", "price"])
    df["price"] = df["price"].str.replace("$", "").str.replace(",", "").astype(float)
    pd.plotting.radviz(df, "price")
    plt.savefig("radviz.png")
