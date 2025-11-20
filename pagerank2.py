class Node:
    def __init__(self, name):
        self.name = name
        self.children = [] # children are a node outbounds links
        self.parents = [] # parents are a node inbound links
        self.auth = 1.0
        self.hub = 1.0
        self.pagerank = 1.0
    
    @staticmethod
    def page_rank_iter(graph, d):
      node_list = graph.nodes
      n = len(node_list)
      for node in node_list:
        node.updatePageRank(d, n)
    
    def updatePageRank(self, d, n):
       parents = self.parents
       pageRankSum = sum((node.pagerank / len(node.children)) for node in parents)
       random_walk = d / n
       self.pagerank = random_walk + (1 - d) * pageRankSum
       