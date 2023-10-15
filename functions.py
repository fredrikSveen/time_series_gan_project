import matplotlib.pyplot as plt


def plot_sensor_data(name, df):
    plt.plot(df[name], label=name)
    plt.legend()
    plt.show()

def plot_all_nine_sensors(dataframe):
    plt.figure(figsize=(15, 9))
    rows = 3
    cols = 3
    n = rows * cols
    index = 1
    for name, df in dataframe.items():
        plt.subplot(rows, cols, index)
        index += 1
        plt.plot(df)
        plt.title(name)