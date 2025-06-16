## 📘 RESUMO – PERCURSOS, CICLOS, EULER & HAMILTON (UFPA • 15 nov 2020)

| **Bloco**                                | **Ideias-chave (definições e teoremas essenciais)**                                                                                                         | **Notas / Aplicações**                               |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Adjacências**                          | • **Vértices adjacentes**: existe aresta entre $v_i$ e $v_j$. • **Arestas adjacentes**: compartilham um mesmo vértice                                       | Base para todas as noções de percurso                |
| **Sucessor / Antecessor**                | Em dígrafos: $v_j$ é **sucessor** de $v_i$ se há arco $v_i\!\to v_j$; inverso ⇒ antecessor                                                                  |                                                      |
| **Percurso (Passeio)**                   | Sequência $v_0,a_1,v_1,\dots ,a_k,v_k$ onde cada aresta é adjacente à anterior e à seguinte                                                                 | Pode **repetir** vértices e arestas                  |
|   • **Aberto / Fechado**                 | Aberto: $v_0\neq v_k$; Fechado: $v_0=v_k$                                                                                                                   |                                                      |
|   • **Simples**                          | Não repete arestas                                                                                                                                          |                                                      |
|   • **Elementar**                        | Não repete vértices (⇒ sempre simples)                                                                                                                      |                                                      |
| **Ciclo**                                | Percurso **simples e fechado**                                                                                                                              |                                                      |
|   • **Ciclo simples**                    | Além disso, não repete vértices (exceto o primeiro)                                                                                                         |                                                      |
| **Spanning walk**                        | Percurso que visita **todos** os vértices ou todas as arestas ao menos uma vez                                                                              |                                                      |
| **Trilha / Cadeia**                      | Percurso sem repetição de arestas; cadeia **fechada** ou **aberta** conforme extremos                                                                       |                                                      |
| **Caminho**                              | Grafo $P=(V,A)$ tal que $V=\{x_0,\dots ,x_k\}$ e $A=\{x_0x_1,\dots ,x_{k-1}x_k\}$ com **todos os vértices distintos** ⇒ “cadeia sem repetição de vértices”  |                                                      |
| **Comprimento**                          | Nº de arestas usadas (contando repetições)                                                                                                                  |                                                      |
| **Euler**                                | Percurso que usa **cada aresta exactamente uma vez**                                                                                                        |                                                      |
|   • **Grafo euleriano**                  | Possui **ciclo** que percorre todas as arestas (cadeia fechada)                                                                                             |                                                      |
|   • **Semieuleriano**                    | Possui **trilha** (aberta) que percorre todas as arestas                                                                                                    |                                                      |
|   • **Teorema de Euler**                 | Grafo conexo não orientado tem **ciclo euleriano** ⇔ todos os vértices têm grau **par**                                                                     |                                                      |
|   • **Teorema (Gross)**                  | Grafo conexo possui **trilha euleriana aberta** ⇔ exatamente **dois** vértices de grau ímpar (início e fim)                                                 |                                                      |
|   • **Algoritmo de Fleury**              | Marca arestas uma a uma, evitando pontes até obrigatório; custo $O(m^2)$ sem otimização                                                                     | Resolve ciclo euleriano                              |
| **Hamilton**                             | Percurso que visita **cada vértice** exatamente uma vez (arestas podem repetir)                                                                             |                                                      |
|   • **Grafo hamiltoniano**               | Possui **ciclo** que passa por todos os vértices                                                                                                            | Decidir se um grafo é hamiltoniano é **NP-Completo** |
| **PCV (TSP)**                            | Dado grafo ponderado, procurar **ciclo hamiltoniano de custo mínimo**; problema **NP-Difícil**                                                              |                                                      |
|   • **Heurística de Bellmore–Nemhauser** | “Próximo vizinho” até cobrir todos; custo $O(n^2)$                                                                                                          | Boa para instâncias grandes, sem garantia ótima      |

---

### ✔️ Como usar

* **Euler** → roteiros que precisam cobrir **arestas** (ruas, pontes) sem repetição (ex.: coleta de lixo).
* **Hamilton / PCV** → roteiros que precisam cobrir **vértices** (cidades, clientes) uma única vez, minimizando custo.

Recomendação de estudo: praticar classificando grafos em *eulerianos*, *semieulerianos*, *hamiltonianos* e aplicar Fleury em exemplos simples.
