import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class CommonPosition:
    def __init__(self, dataset):
        self.dataset = dataset
        self.player_salaries = pd.read_excel(self.dataset, "Player Salaries")

    def display(self):
        """ Will display the data in a graph """
        data = self.set_values()
        positions = self.get_positions(data)
        npositions = self.get_npositions(data)

        # Set the size for the graph
        plt.figure(figsize=(20,10))

        # Plot The Graph
        x = np.arange(len(positions))
        plt.bar(x, height=npositions)
        plt.xticks(x,positions)

        # Set labels for the graph
        plt.ylabel('Players on position')
        plt.xlabel('Position')
        plt.show()

    def set_values(self):
        """ Will create a dictionary of the data """
        data = {}

        for pos, comp in zip(self.player_salaries.Pos, self.player_salaries.Compensation):
            pos = pos.strip()

            if pos not in data:
                data[pos] = 1
            else:
                data[pos] += 1

        return data

    def get_npositions(self, data):
        """ Will return the number of player at position
        :type data: dict(str: [])
        :rtype data: Array[int]
        """
        npositions = []

        for pos in data:
            npositions.append(data[pos])

        return npositions

    def get_positions(self, data):
        """ Will return the positions of the players
        :type data: dict(str: [])
        :rtype data: Array[str]
        """
        positions = []

        for pos in data:
            positions.append(pos)

        return positions