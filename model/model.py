import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph =nx.Graph()
        self._idMap={}

    def build_graph(self,c,b):
        self._graph.clear()
        self._idMap.clear()

        nodi=DAO.get_nodi(c,b)
        self._graph.add_nodes_from(nodi)
        for n in nodi:
            self._idMap[n.driverId]=n

        edges=DAO.get_archi(list(self._idMap.keys()),self._idMap,int(c),int(b))
        for a in edges:
            self._graph.add_edge(a.o1, a.o2, weight=a.peso)


    def get_stats(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_anni(self):
        lista=DAO.getAllYears()
        return lista



    def top3(self):
        archi=self._graph.edges(data=True)
        lista=sorted(archi, key=lambda x: x[2]["weight"], reverse=True)
        s=""
        for i in range(3):
            s=s+lista[i][0].__str__() + lista[i][1].__str__() + str(lista[i][2]["weight"]) + "\n"
        return s

    def connesse(self):
        lista=list(nx.connected_components(self._graph))
        largest=max(nx.connected_components(self._graph),key=len)
        k=len(lista)
        return k, largest

    def get_anni(self):
        return list(DAO.getAllYears())



