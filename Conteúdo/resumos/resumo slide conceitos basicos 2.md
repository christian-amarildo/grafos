## 📘 RESUMO – ISOMORFISMO, PLANARIDADE & API BÁSICA (Slides 26 / 10 / 2020)

---

### 1. Isomorfismo de Grafos

| Conceito                         | Descrição                                                                                                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Isomorfismo (grafos simples)** | Existe uma **bijeção** $f:V_1\to V_2$ tal que: $uv\in A_1 \iff f(u)f(v)\in A_2$. Preserva adjacências **e** não-adjacências.                                                                             |
| **Generalização**                | Vale mesmo com laços e arestas múltiplas se: <br>• nº de arestas entre qualquer par $u,v$ é mantido;<br>• nº de laços em cada vértice é mantido.                                                         |
| **Propriedades necessárias**     | Grafos isomorfos têm: <br>• mesma **sequência de graus**;<br>• mesmos subgrafos elementares.                                                                                                             |
| **Complexidade**                 | Força-bruta exige $n!$ verificações. <br>Problema clássico de pesquisa: “GI” ⚖️ (**não se sabe** se está em P ou se é NP-completo). <br>• Melhor algoritmo conhecido: **quasipolinomial** (Babai, 2015). |

---

### 2. Planaridade de Grafos

| Tópico                            | Pontos-chave                                                                                                                                                                 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Grafo planar**                  | Pode ser desenhado no plano **sem cruzar** arestas.                                                                                                                          |
| **Representação plana (R)**       | Divide o plano em **regiões** (externa + internas).                                                                                                                          |
| **Fórmula de Euler**              | Para grafo **simples planar**: $n + r = m + 2$ (vértices + regiões = arestas + 2).                                                                                           |
| **Corolário – limite de arestas** | Qualquer grafo planar satisfaz $m \le 3n - 6$ (para $n \ge 3$). <br>⚠️ Condição é **necessária, não suficiente** – ex.: $K_{3,3}$ cumpre  $m=9=3(6)-6$ mas **não** é planar. |

---

### 3. Exercícios sugeridos nos slides

1. **Encontrar** funções de isomorfismo entre pares de grafos (ou provar que não existem).
2. **Mostrar** violação da planaridade usando $K_{3,3}$ ou $K_5$.

---

### 4. Desafio de Pesquisa (Resenha)

* Ler e resumir (1 página) dois artigos de divulgação sobre o avanço de Babai:

  1. *“Landmark Algorithm Breaks 30-Year Impasse”* (2015, Quanta)
  2. *“Graph Isomorphism Vanquished — Again”* (2017, Quanta)

---

### 5. API Java – Estrutura Básica para Grafos Não Orientados

```java
public class Grafo {
    Grafo(int V);           // cria grafo com V vértices, 0 arestas
    int V();                // devolve nº de vértices
    int A();                // devolve nº de arestas
    void addAresta(int v, int w); // adiciona aresta v-w
    Iterable<Integer> adj(int v); // vértices adjacentes a v
    public String toString();
}
```

> **Preparação necessária**: listas encadeadas, classes genéricas e laço *foreach* em Java.

---

### 6. Bibliografia-chave

* **Cormen et al.** *Algoritmos: Teoria e Prática* – caps. 22-26
* **Gross & Yellen** *Graph Theory and Its Applications* (2ª ed.)
* **Sedgewick** *Algorithms in Java, Part 5* – Graph Algorithms
* **Goldbarg & Goldbarg** *Grafos: Conceitos, Algoritmos e Aplicações* (2012)

---

### ✔️ Pronto!

Este resumo abrange as definições, teoremas, limites, desafios de isomorfismo, planaridade e a especificação inicial da API de grafos não direcionados. Se precisar de exemplos resolvidos, diagramas ou explicações mais detalhadas, é só pedir!
