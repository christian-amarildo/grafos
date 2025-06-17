# Algoritmo Bellmore-Nemhauser
# Entrada: Grafo G = (V, E) com n vertices
# Saida: Um ciclo hamiltoniano (possivelmente) de custo minimo

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


def bellmore_nemhauser(G: Grafo, vertice_inicial: Optional[Union[str, int]] = None) -> Union[List, bool]:
    if not G.ponderado:
        raise ValueError("Algoritmo requer grafo ponderado")
    
    if len(G.vertices) < 3:
        return False
    
    vertices = G.vertices
    arestas = G.arestas
    
    v = vertice_inicial if vertice_inicial and vertice_inicial in vertices else vertices[0]
    v_inicial = v
    H = [v]
    custo_total = 0
    
    while len(H) < len(vertices):
        menor_custo = float("inf")
        menor_vertice = None
        
        for u, w in arestas:
            if u == v and w not in H and arestas[(u, w)] < menor_custo:
                menor_custo = arestas[(u, w)]
                menor_vertice = w
        
        if menor_vertice is None:
            return False
        
        v = menor_vertice
        H.append(v)
        custo_total += menor_custo
    
    if (H[-1], v_inicial) not in arestas:
        return False
    
    custo_total += arestas[(H[-1], v_inicial)]
    H.append(v_inicial)
    
    return H, custo_total


def bellmore_nemhauser_melhorado(G: Grafo, vertice_inicial: Optional[Union[str, int]] = None) -> Union[Tuple[List, float], bool]:
    if not G.ponderado:
        raise ValueError("Algoritmo requer grafo ponderado")
    
    n = len(G.vertices)
    if n < 3:
        return False
    
    melhor_ciclo = None
    melhor_custo = float("inf")
    
    vertices_tentativa = [vertice_inicial] if vertice_inicial else G.vertices
    
    for v_inicial in vertices_tentativa:
        v = v_inicial
        H = [v]
        custo = 0
        visitados = {v}
        
        valido = True
        while len(H) < n:
            candidatos = [(w, G.arestas[(v, w)]) for v2, w in G.arestas 
                         if v2 == v and w not in visitados]
            
            if not candidatos:
                valido = False
                break
            
            proximo, peso = min(candidatos, key=lambda x: x[1])
            H.append(proximo)
            visitados.add(proximo)
            custo += peso
            v = proximo
        
        if valido and (H[-1], v_inicial) in G.arestas:
            custo += G.arestas[(H[-1], v_inicial)]
            if custo < melhor_custo:
                melhor_custo = custo
                melhor_ciclo = H + [v_inicial]
    
    return (melhor_ciclo, melhor_custo) if melhor_ciclo else False


def verificar_ciclo_hamiltoniano(G: Grafo, ciclo: List) -> bool:
    if len(ciclo) != len(G.vertices) + 1:
        return False
    
    if ciclo[0] != ciclo[-1]:
        return False
    
    vertices_unicos = set(ciclo[:-1])
    if len(vertices_unicos) != len(G.vertices):
        return False
    
    for i in range(len(ciclo) - 1):
        if (ciclo[i], ciclo[i+1]) not in G.arestas:
            return False
    
    return True


def calcular_custo_ciclo(G: Grafo, ciclo: List) -> float:
    if not G.ponderado:
        return len(ciclo) - 1
    
    custo = 0
    for i in range(len(ciclo) - 1):
        custo += G.arestas[(ciclo[i], ciclo[i+1])]
    return custo


if __name__ == "__main__":
    print("Teste 1: Grafo simples")
    g1 = Grafo(
        vertices=['a', 'b', 'c', 'd'], 
        direcionado=False, 
        arestas={
            ('a', 'b'): 3, ('a', 'c'): 2, ('a', 'd'): 7,
            ('b', 'c'): 5, ('b', 'd'): 9, ('c', 'd'): 6
        }
    )
    
    resultado = bellmore_nemhauser(g1)
    if resultado:
        ciclo, custo = resultado
        print(f"Ciclo encontrado: {ciclo}")
        print(f"Custo total: {custo}")
        print(f"Ciclo valido: {verificar_ciclo_hamiltoniano(g1, ciclo)}")
    else:
        print("Nenhum ciclo hamiltoniano encontrado")
    
    print("\nTeste 2: Versao melhorada")
    resultado_melhorado = bellmore_nemhauser_melhorado(g1)
    if resultado_melhorado:
        ciclo, custo = resultado_melhorado
        print(f"Melhor ciclo: {ciclo}")
        print(f"Custo otimizado: {custo}")
    
    print("\nTeste 3: Grafo completo K5")
    vertices_k5 = [1, 2, 3, 4, 5]
    arestas_k5 = {}
    for i in range(5):
        for j in range(i+1, 5):
            peso = abs(vertices_k5[i] - vertices_k5[j])
            arestas_k5[(vertices_k5[i], vertices_k5[j])] = peso
    
    g2 = Grafo(vertices=vertices_k5, direcionado=False, arestas=arestas_k5)
    resultado_k5 = bellmore_nemhauser(g2)
    if resultado_k5:
        ciclo, custo = resultado_k5
        print(f"Ciclo K5: {ciclo}")
        print(f"Custo: {custo}")
    
    print("\nTeste 4: Grafo sem ciclo hamiltoniano")
    g3 = Grafo(
        vertices=['x', 'y', 'z'],
        direcionado=False,
        arestas={('x', 'y'): 1, ('y', 'z'): 2}
    )
    print(f"Resultado grafo desconexo: {bellmore_nemhauser(g3)}")
    
    print("\nTeste 5: Comparacao de vertices iniciais")
    for v in g1.vertices:
        resultado = bellmore_nemhauser(g1, v)
        if resultado:
            ciclo, custo = resultado
            print(f"Iniciando em '{v}': custo = {custo}")