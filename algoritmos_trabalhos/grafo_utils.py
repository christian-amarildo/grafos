import numpy as np
from typing import List, Dict, Tuple, Union, Any, Optional


class Grafo:
    def __init__(self, vertices: List[Union[str, int]], 
                 arestas: Union[List[Tuple], Dict[Tuple, Union[int, float]]], 
                 direcionado: bool = True):
        
        self.direcionado = direcionado
        
        for v in vertices:
            if not isinstance(v, (str, int)):
                raise ValueError("Os labels dos vertices devem ser inteiros ou strings")
        
        self.vertices = vertices
        self._vertices_set = set(vertices)
        
        if isinstance(arestas, list):
            self.arestas = []
            self.ponderado = False
            
            for a in arestas:
                if not isinstance(a, tuple) or len(a) != 2:
                    raise ValueError("Arestas devem ser tuplas de tamanho 2")
                
                u, v = a
                if u not in self._vertices_set or v not in self._vertices_set:
                    raise ValueError(f"Aresta {a} contem vertices nao existentes")
                
                if not direcionado:
                    self.arestas.extend([(u, v), (v, u)])
                else:
                    self.arestas.append((u, v))
        
        elif isinstance(arestas, dict):
            self.arestas = {}
            self.ponderado = True
            
            for aresta, valor in arestas.items():
                if not isinstance(aresta, tuple) or len(aresta) != 2:
                    raise ValueError("Arestas devem ser tuplas de tamanho 2")
                
                u, v = aresta
                if u not in self._vertices_set or v not in self._vertices_set:
                    raise ValueError(f"Aresta {aresta} contem vertices nao existentes")
                
                if not isinstance(valor, (int, float)):
                    raise ValueError("Pesos das arestas devem ser numericos")
                
                if not direcionado:
                    self.arestas[aresta] = valor
                    self.arestas[(v, u)] = valor
                else:
                    self.arestas[aresta] = valor
        
        else:
            raise ValueError("Arestas devem ser list ou dict")
        
        self._lista_adj_cache = None

    def printar_grafo(self) -> None:
        print(f"G=(V = [", end="")
        print(", ".join(map(str, self.vertices)), end="], A = [")
        
        if isinstance(self.arestas, list):
            arestas_str = ", ".join(str(a) for a in self.arestas)
            print(arestas_str, end="")
        else:
            arestas_str = ", ".join(f"{a}: {peso}" for a, peso in self.arestas.items())
            print(arestas_str, end="")
        
        print("])")

    def grau_entrada_dos_vertices(self) -> Dict[Any, int]:
        graus = {v: 0 for v in self.vertices}
        
        if isinstance(self.arestas, list):
            for _, v in self.arestas:
                graus[v] += 1
        else:
            for (_, v) in self.arestas:
                graus[v] += 1
        
        return graus
    
    def grau_saida_dos_vertices(self) -> Dict[Any, int]:
        graus = {v: 0 for v in self.vertices}
        
        if isinstance(self.arestas, list):
            for u, _ in self.arestas:
                graus[u] += 1
        else:
            for (u, _) in self.arestas:
                graus[u] += 1
        
        return graus
    
    def graus_de_um_vertice(self, v: Union[str, int]) -> Tuple[int, int]:
        if v not in self._vertices_set:
            raise ValueError(f"Vertice {v} nao existe no grafo")
        
        entrada = saida = 0
        
        if isinstance(self.arestas, list):
            for u, w in self.arestas:
                if u == v:
                    saida += 1
                if w == v:
                    entrada += 1
        else:
            for (u, w) in self.arestas:
                if u == v:
                    saida += 1
                if w == v:
                    entrada += 1
        
        return entrada, saida
    
    def verificar_aresta(self, aresta: Tuple) -> bool:
        if isinstance(self.arestas, list):
            return aresta in self.arestas
        else:
            return aresta in self.arestas
    
    def vertice_isolado(self, v: Union[str, int]) -> bool:
        if v not in self._vertices_set:
            raise ValueError(f"Vertice {v} nao existe no grafo")
        
        if isinstance(self.arestas, list):
            for u, w in self.arestas:
                if v in (u, w):
                    return False
        else:
            for (u, w) in self.arestas:
                if v in (u, w):
                    return False
        
        return True
    
    def adicionar_vertice(self, v: Union[str, int]) -> None:
        if not isinstance(v, (str, int)):
            raise ValueError("Vertice a adicionar deve ser string ou inteiro")
        
        if v in self._vertices_set:
            raise ValueError(f"Vertice {v} ja existe no grafo")
        
        self.vertices.append(v)
        self._vertices_set.add(v)
        self._lista_adj_cache = None

    def adicionar_aresta(self, aresta: Tuple, peso: Union[int, float] = 1) -> None:
        if not isinstance(aresta, tuple) or len(aresta) != 2:
            raise ValueError("Aresta deve ser tupla com tamanho 2")
        
        u, v = aresta
        
        if u not in self._vertices_set or v not in self._vertices_set:
            raise ValueError(f"Vertices {u} ou {v} nao existem")
        
        if isinstance(self.arestas, list):
            if not self.direcionado:
                self.arestas.extend([(u, v), (v, u)])
            else:
                self.arestas.append(aresta)
        else:
            if not self.direcionado:
                self.arestas[aresta] = peso
                self.arestas[(v, u)] = peso
            else:
                self.arestas[aresta] = peso
        
        self._lista_adj_cache = None
    
    def remover_vertice(self, v: Union[str, int]) -> None:
        if v not in self._vertices_set:
            raise ValueError(f"Vertice {v} nao existe no grafo")
        
        self.vertices.remove(v)
        self._vertices_set.remove(v)
        
        if isinstance(self.arestas, list):
            self.arestas = [(u, w) for u, w in self.arestas if u != v and w != v]
        else:
            self.arestas = {(u, w): peso for (u, w), peso in self.arestas.items() 
                           if u != v and w != v}
        
        self._lista_adj_cache = None
    
    def remover_aresta(self, aresta: Tuple) -> None:
        if isinstance(self.arestas, list):
            if aresta in self.arestas:
                self.arestas.remove(aresta)
                if not self.direcionado:
                    self.arestas.remove((aresta[1], aresta[0]))
        else:
            if aresta in self.arestas:
                del self.arestas[aresta]
                if not self.direcionado:
                    del self.arestas[(aresta[1], aresta[0])]
        
        self._lista_adj_cache = None
    
    def lista_adjacencias(self) -> Dict[Any, List[Any]]:
        if self._lista_adj_cache is not None:
            return self._lista_adj_cache
        
        lista_adjacencias = {v: [] for v in self.vertices}
        
        if isinstance(self.arestas, list):
            for v1, v2 in self.arestas:
                if v2 not in lista_adjacencias[v1]:
                    lista_adjacencias[v1].append(v2)
        else:
            for (v1, v2) in self.arestas:
                if v2 not in lista_adjacencias[v1]:
                    lista_adjacencias[v1].append(v2)
        
        self._lista_adj_cache = lista_adjacencias
        return lista_adjacencias
    
    def matriz_de_adjacencias(self) -> List[List[int]]:
        tam = len(self.vertices)
        matriz = [[0 for _ in range(tam)] for _ in range(tam)]
        
        vertice_idx = {v: i for i, v in enumerate(self.vertices)}
        
        if isinstance(self.arestas, list):
            for v1, v2 in self.arestas:
                i1, i2 = vertice_idx[v1], vertice_idx[v2]
                matriz[i1][i2] = 1
        else:
            for (v1, v2), peso in self.arestas.items():
                i1, i2 = vertice_idx[v1], vertice_idx[v2]
                matriz[i1][i2] = peso
        
        return matriz

    def conexo_por_mm(self, m: Optional[List[List[int]]] = None, 
                      ignorar_indices: Optional[List[int]] = None) -> bool:
        tam = len(self.vertices)
        R = np.zeros((tam, tam), dtype=int)
        
        if m is None:
            m = np.array(self.matriz_de_adjacencias())
        else:
            m = np.array(m)
        
        if ignorar_indices is None:
            ignorar_indices = []

        for i in range(1, tam + 1):
            R += np.linalg.matrix_power(m, i)

        np.fill_diagonal(R, 1)

        for i in ignorar_indices:
            for j in range(tam):
                R[i][j] = 1
                R[j][i] = 1

        return np.all(R > 0)
    
    def numero_de_arestas(self) -> int:
        if isinstance(self.arestas, list):
            return len(self.arestas)
        else:
            return len(self.arestas)
    
    def densidade(self) -> float:
        n = len(self.vertices)
        if n <= 1:
            return 0.0
        
        max_arestas = n * (n - 1)
        if not self.direcionado:
            max_arestas = max_arestas // 2
        
        return self.numero_de_arestas() / max_arestas if max_arestas > 0 else 0.0
    
    def eh_completo(self) -> bool:
        return abs(self.densidade() - 1.0) < 1e-9
    
    def vertices_vizinhos(self, v: Union[str, int]) -> List[Any]:
        if v not in self._vertices_set:
            raise ValueError(f"Vertice {v} nao existe no grafo")
        
        vizinhos = set()
        
        if isinstance(self.arestas, list):
            for u, w in self.arestas:
                if u == v:
                    vizinhos.add(w)
                if not self.direcionado and w == v:
                    vizinhos.add(u)
        else:
            for (u, w) in self.arestas:
                if u == v:
                    vizinhos.add(w)
                if not self.direcionado and w == v:
                    vizinhos.add(u)
        
        return list(vizinhos)
    
    def caminho_existe(self, origem: Union[str, int], destino: Union[str, int]) -> bool:
        if origem not in self._vertices_set or destino not in self._vertices_set:
            return False
        
        if origem == destino:
            return True
        
        visitados = set()
        fila = [origem]
        
        while fila:
            atual = fila.pop(0)
            if atual == destino:
                return True
            
            if atual in visitados:
                continue
                
            visitados.add(atual)
            
            lista_adj = self.lista_adjacencias()
            for vizinho in lista_adj[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)
        
        return False


if __name__ == "__main__":
    print("Teste 1: Grafo direcionado simples")
    grafo1 = Grafo(vertices=[1, 2, 3], arestas=[(1, 2), (2, 3)])
    grafo1.printar_grafo()
    print("Grau de entrada:", grafo1.grau_entrada_dos_vertices())
    print("Grau de saida:", grafo1.grau_saida_dos_vertices())
    print("Graus do vertice 2:", grafo1.graus_de_um_vertice(2))
    print("Lista de adjacencia:", grafo1.lista_adjacencias())
    print("Matriz de adjacencia:")
    for linha in grafo1.matriz_de_adjacencias():
        print(linha)
    print("Vertice 3 e isolado?", grafo1.vertice_isolado(3))
    print()

    print("Teste 2: Adicionando vertice e aresta")
    grafo1.adicionar_vertice(4)
    grafo1.adicionar_aresta((3, 4))
    grafo1.printar_grafo()
    print("Lista de adjacencia atualizada:", grafo1.lista_adjacencias())
    print()

    print("Teste 3: Grafo com pesos")
    grafo2 = Grafo(vertices=['A', 'B'], arestas={('A', 'B'): 5})
    grafo2.printar_grafo()
    print("Verificar aresta ('A', 'B'):", grafo2.verificar_aresta(('A', 'B')))
    print("Matriz de adjacencia:")
    for linha in grafo2.matriz_de_adjacencias():
        print(linha)
    print()
    
    print("Teste 4: Funcoes adicionais")
    print("Numero de arestas:", grafo1.numero_de_arestas())
    print("Densidade do grafo:", grafo1.densidade())
    print("Grafo completo?", grafo1.eh_completo())
    print("Vizinhos do vertice 2:", grafo1.vertices_vizinhos(2))
    print("Existe caminho de 1 para 4?", grafo1.caminho_existe(1, 4))