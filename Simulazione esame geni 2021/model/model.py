import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.listGenes = []
        self.listEdges = []

    def buildGraph(self):
        self.listGenes = DAO.get_all_genes_id()
        self._graph.add_nodes_from(self.listGenes)

        self.listEdges = DAO.get_all_edges()
        for e in self.listEdges:
            g1 = e[0]
            g2 = e[2]
            cr1 = e[1]
            cr2 = e[3]
            if g1 in self.listGenes and g2 in self.listGenes:
                if cr1 != cr2:
                    peso = abs(e[4])
                    self._graph.add_edge(g1, g2, weight=peso)
                elif cr1 == cr2:
                    peso = 2*abs(e[4])
                    self._graph.add_edge(g1, g2, weight=peso)

    def calcolaAdiacenti(self, gene):
        listaAdiacenti = []
        if gene in self.listGenes:
            for edge in self._graph.neighbors(gene):
                peso = self._graph[gene][edge]["weight"]
                listaAdiacenti.append((edge, peso))
        listaAdiacenti.sort(key=lambda x: x[1], reverse=True)
        return listaAdiacenti

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getGeniId(self):
        listaGeni = DAO.get_all_genes_id()
        return listaGeni
