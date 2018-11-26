import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class PositionEarning:
    def __init__(self, dataset):
        self.dataset = dataset
        self.player_salaries = pd.read_excel(self.dataset, "Player Salaries")

    def display(self):
        """ Will display the data in a graph """
        data = self.set_values()
        averages = self.get_averages(data)
        positions = self.get_positions(data)

        # Set the size for the graph
        plt.figure(figsize=(20,10))

        # Plot The Graph
        x = np.arange(len(averages))
        plt.bar(x, height=averages)
        plt.xticks(x,positions)

        # Set labels for the graph
        plt.ylabel('Compensation')
        plt.xlabel('Position')
        plt.show()

    def set_values(self):
        """ Will create a dictionary of the data """
        data = {}

        for pos, comp in zip(self.player_salaries.Pos, self.player_salaries.Compensation):
            pos = pos.strip()

            if pos not in data:
                data[pos] = []

            data[pos].append(comp)

        return data

    def get_averages(self, data):
        """ Will return the average of the data 
        :type data: dict(str: [])
        :rtype data: Array[str]
        """
        averages = []

        for pos in data:
            averages.append(sum(data[pos]) // len(data[pos]))

        return averages

    def get_positions(self, data):
        """ Will return the positions of the players
        :type data: dict(str: [])
        :rtype data: Array[str]
        """
        positions = []

        for pos in data:
            positions.append(pos)

        return positions