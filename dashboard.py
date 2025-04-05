import matplotlib.pyplot as plt

plt.ion()


class Dashboard:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.data = []

    def display_analytics(self, data):
        self.data.append(data)
        self.ax.clear()
        for ind in ["min", "max", "avarage"]:
            y = [i[ind] for i in self.data]
            self.ax.plot([i["time"] for i in self.data], y,label = ind)

        plt.legend()
        plt.show()
