# import matplotlib.pyplot as plt
import networkx as nx
import re


data = open("input.txt").read().splitlines()
# data = open("tdata.txt").read().splitlines()


class BagFinder:
    def __init__(self, data):
        self.data = data
        self.lookup = {}
        self.gold = 0
        self.parse_data()
        self.parse_data()
        self.graph = self.build_graph()
        self.distance = 0

    def build_graph(self):
        G = nx.DiGraph()
        for k, v in self.lookup.items():
            if type(v) is dict:
                for c, w in v.items():
                    G.add_edge(k, c, weight=w)

        return G

    def find_gold(self):
        # print(self.graph.edges['shiny gold', 'vibrant plum']['weight'])
        for n in self.graph.nodes:
            if n != "shiny gold" and nx.has_path(self.graph, n, "shiny gold"):
                self.gold += 1
                self.distance += (
                    nx.single_source_dijkstra(self.graph, n, "shiny gold")
                )[0]

    def parse_data(self):
        regex = "((?:[0-9]){1,})(.\w{1,}.\w{1,})"  # noqa: W605

        for line in self.data:
            c = line.split(" ")[:2]
            c = " ".join(c)
            self.lookup[c] = {}
            entries = re.findall(regex, line)
            for i in entries:
                n = i[1].strip()
                self.lookup[c][n] = int(i[0])


bf = BagFinder(data)
bf.parse_data()
bf.find_gold()
print(f"Gold is {bf.gold}")
print(f"Distance is {bf.distance}")
