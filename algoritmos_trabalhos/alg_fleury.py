from copy import deepcopy
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


def verificar_euleriano(G: Grafo) -> Tuple[bool, bool, List]:
    if G.direcionado:
        raise ValueError("Algoritmo de Fleury funciona apenas para grafos nao direcionados")
    
    if not G.conexo_por_mm():
        return False, False, []
    
    vertices_impares = []
    for v in G.vertices:
        _, grau_saida = G.graus_de_um_vertice(v)
        if grau_saida % 2 == 1:
            vertices_impares.append(v)
    
    tem_circuito = len(vertices_impares) == 0
    tem_caminho = len(vertices_impares) == 2
    
    return tem_circuito, tem_caminho, vertices_impares


def alg_fleury(G: Grafo, vertice_inicial: Optional[Union[str, int]] = None) -> Union[List[Tuple], bool]:
    if G.direcionado:
        raise ValueError("Algoritmo funciona apenas para grafos nao direcionados")
    
    tem_circuito, tem_caminho, vertices_impares = verificar_euleriano(G)
    
    if not tem_circuito and not tem_caminho:
        return False
    
    if vertice_inicial is None:
        if tem_caminho:
            vertice_inicial = vertices_impares[0]
        else:
            vertice_inicial = G.vertices[0]
    elif vertice_inicial not in G._vertices_set:
        raise ValueError(f"Vertice inicial {vertice_inicial} nao existe")
    
    resposta = []
    tam = len(G.vertices)
    matriz_adj = np.array(G.matriz_de_adjacencias())
    
    vertice_idx = {v: i for i, v in enumerate(G.vertices)}
    idx_vertice = {i: v for v, i in vertice_idx.items()}
    
    current_idx = vertice_idx[vertice_inicial]
    vertices_isolados = []
    
    total_arestas = np.sum(matriz_adj) // 2
    
    while len(resposta) < total_arestas:
        vizinhos = []
        for i in range(tam):
            if matriz_adj[current_idx][i] > 0:
                vizinhos.append(i)
        
        if not vizinhos:
            return False
        
        proximo_idx = None
        
        if len(vizinhos) == 1:
            proximo_idx = vizinhos[0]
        else:
            for idx in vizinhos:
                matriz_temp = matriz_adj.copy()
                matriz_temp[current_idx][idx] = 0
                matriz_temp[idx][current_idx] = 0
                
                if eh_conexo_ignorando_isolados(matriz_temp, vertices_isolados + [current_idx]):
                    proximo_idx = idx
                    break
            
            if proximo_idx is None:
                proximo_idx = vizinhos[0]
        
        matriz_adj[current_idx][proximo_idx] -= 1
        matriz_adj[proximo_idx][current_idx] -= 1
        
        resposta.append((idx_vertice[current_idx], idx_vertice[proximo_idx]))
        
        if np.sum(matriz_adj[current_idx]) == 0:
            vertices_isolados.append(current_idx)
        
        current_idx = proximo_idx
    
    return resposta


def eh_conexo_ignorando_isolados(matriz: np.ndarray, isolados: List[int]) -> bool:
    tam = matriz.shape[0]
    vertices_ativos = [i for i in range(tam) if i not in isolados and np.sum(matriz[i]) > 0]
    
    if len(vertices_ativos) <= 1:
        return True
    
    visitados = set()
    fila = [vertices_ativos[0]]
    
    while fila:
        atual = fila.pop(0)
        if atual in visitados:
            continue
        
        visitados.add(atual)
        
        for i in range(tam):
            if matriz[atual][i] > 0 and i not in visitados and i in vertices_ativos:
                fila.append(i)
    
    return len(visitados) == len(vertices_ativos)


def alg_fleury_otimizado(G: Grafo) -> Union[List[Tuple], bool]:
    tem_circuito, tem_caminho, vertices_impares = verificar_euleriano(G)
    
    if not tem_circuito and not tem_caminho:
        return False
    
    arestas_dict = {}
    for aresta in G.arestas:
        if isinstance(G.arestas, list):
            chave = tuple(sorted(aresta))
            arestas_dict[chave] = arestas_dict.get(chave, 0) + 1
        else:
            chave = tuple(sorted(aresta))
            arestas_dict[chave] = arestas_dict.get(chave, 0) + 1
    
    vertice_atual = vertices_impares[0] if tem_caminho else G.vertices[0]
    caminho = []
    arestas_temp = arestas_dict.copy()
    
    while any(count > 0 for count in arestas_temp.values()):
        vizinhos = []
        
        for (u, v), count in arestas_temp.items():
            if count > 0:
                if u == vertice_atual:
                    vizinhos.append((v, (u, v)))
                elif v == vertice_atual:
                    vizinhos.append((u, (u, v)))
        
        if not vizinhos:
            return False
        
        if len(vizinhos) == 1:
            proximo, aresta_chave = vizinhos[0]
        else:
            proximo = None
            aresta_escolhida = None
            
            for viz, aresta_chave in vizinhos:
                arestas_temp[aresta_chave] -= 1
                
                if verifica_conectividade_rapida(vertice_atual, arestas_temp, G.vertices):
                    proximo = viz
                    aresta_escolhida = aresta_chave
                    arestas_temp[aresta_chave] += 1
                    break
                
                arestas_temp[aresta_chave] += 1
            
            if proximo is None:
                proximo, aresta_escolhida = vizinhos[0]
            else:
                aresta_chave = aresta_escolhida
        
        caminho.append((vertice_atual, proximo))
        arestas_temp[aresta_chave] -= 1
        vertice_atual = proximo
    
    return caminho


def verifica_conectividade_rapida(excluir_vertice: Any, arestas: Dict, vertices: List) -> bool:
    vertices_com_arestas = set()
    
    for (u, v), count in arestas.items():
        if count > 0:
            if u != excluir_vertice:
                vertices_com_arestas.add(u)
            if v != excluir_vertice:
                vertices_com_arestas.add(v)
    
    if len(vertices_com_arestas) <= 1:
        return True
    
    inicio = next(iter(vertices_com_arestas))
    visitados = set()
    fila = [inicio]
    
    while fila:
        atual = fila.pop(0)
        if atual in visitados:
            continue
        
        visitados.add(atual)
        
        for (u, v), count in arestas.items():
            if count > 0:
                if u == atual and v not in visitados and v != excluir_vertice:
                    fila.append(v)
                elif v == atual and u not in visitados and u != excluir_vertice:
                    fila.append(u)
    
    return len(visitados) == len(vertices_com_arestas)


def imprimir_caminho_euleriano(caminho: List[Tuple]) -> str:
    if not caminho:
        return ""
    
    resultado = [str(caminho[0][0])]
    for _, v in caminho:
        resultado.append(str(v))
    
    return " -> ".join(resultado)


if __name__ == "__main__":
    print("Teste 1: Grafo com circuito euleriano")
    g1 = Grafo(
        vertices=[1, 2, 3, 4, 5, 6],
        direcionado=False,
        arestas=[
            (1, 2), (1, 3), (1, 5),
            (2, 4), (2, 6),
            (3, 6), (3, 4),
            (4, 5),
            (5, 6),
        ]
    )
    
    tem_circuito, tem_caminho, vertices_impares = verificar_euleriano(g1)
    print(f"Tem circuito euleriano: {tem_circuito}")
    print(f"Tem caminho euleriano: {tem_caminho}")
    if vertices_impares:
        print(f"Vertices de grau impar: {vertices_impares}")
    
    resultado = alg_fleury(g1)
    if resultado:
        print(f"\nCaminho encontrado ({len(resultado)} arestas):")
        print(imprimir_caminho_euleriano(resultado))
    else:
        print("Nenhum caminho euleriano encontrado")
    
    print("\n" + "="*50 + "\n")
    
    print("Teste 2: Grafo K3 (triangulo)")
    g2 = Grafo(
        vertices=['A', 'B', 'C'],
        direcionado=False,
        arestas=[('A', 'B'), ('B', 'C'), ('C', 'A')]
    )
    
    resultado2 = alg_fleury(g2)
    if resultado2:
        print("Circuito euleriano K3:")
        print(imprimir_caminho_euleriano(resultado2))
    
    print("\n" + "="*50 + "\n")
    
    print("Teste 3: Grafo sem caminho euleriano")
    g3 = Grafo(
        vertices=[1, 2, 3, 4],
        direcionado=False,
        arestas=[(1, 2), (2, 3), (3, 4)]
    )
    
    tem_circuito3, tem_caminho3, _ = verificar_euleriano(g3)
    print(f"Tem circuito: {tem_circuito3}, Tem caminho: {tem_caminho3}")
    resultado3 = alg_fleury(g3)
    print(f"Resultado: {resultado3}")
    
    print("\n" + "="*50 + "\n")
    
    print("Teste 4: Grafo com multiplas arestas")
    g4 = Grafo(
        vertices=[1, 2, 3],
        direcionado=False,
        arestas=[(1, 2), (1, 2), (2, 3), (2, 3), (1, 3)]
    )
    
    resultado4 = alg_fleury_otimizado(g4)
    if resultado4:
        print("Caminho com multiplas arestas:")
        print(imprimir_caminho_euleriano(resultado4))