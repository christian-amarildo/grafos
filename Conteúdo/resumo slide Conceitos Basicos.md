### 📘 RESUMO – INTRODUÇÃO A GRAFOS (UFPA • Sistemas de Informação)

> **Visão-geral completa** dos conceitos exigidos para a 1ª avaliação, já incorporando todos os pontos listados nos slides de 07 / 10 / 2020.

---

## 1. Definições fundamentais

| Símbolo                          | Significado                                                             |
| -------------------------------- | ----------------------------------------------------------------------- |
| **G = (V, A)** ou **G = (V, E)** | grafo com vértices V e arestas A (ou E)                                 |
|                                  | • V ≠ ∅ (conjunto finito) <br>• A ⊆ V × V (pares de vértices distintos) |

* **Arestas** codificam relações entre objetos (vértices).
* Notação ordinária: (u, v) em grafos orientados; {u, v} ou (u, v) em grafos não orientados.

---

## 2. Aplicações típicas

| Domínio       | Vértices     | Arestas                       |
| ------------- | ------------ | ----------------------------- |
| Comunicação   | computadores | fibras ópticas                |
| Redes Sociais | pessoas      | amizade/seguimento            |
| Transporte    | cidades      | rotas (rodoviárias ou aéreas) |
| Biologia      | proteínas    | interações                    |
| Web           | tags HTML    | hierarquia/links              |
| Química       | átomos       | ligações químicas             |
| Planejamento  | atividades   | precedências                  |

---

## 3. Tipos básicos de grafos

| Tipo                       | Característica-chave                                |   |            |
| -------------------------- | --------------------------------------------------- | - | ---------- |
| **Não orientado**          | aresta sem direção → (a, b) = (b, a)                |   |            |
| **Orientado (dígrafo)**    | aresta com direção → (a, b) ≠ (b, a)                |   |            |
| **Simples**                | sem laços nem arestas paralelas                     |   |            |
| **Pseudografo**            | pelo menos um laço                                  |   |            |
| **Multigrafo**             | ≥ 2 arestas paralelas entre o mesmo par de vértices |   |            |
| **Multigrafo direcionado** | paralelas na mesma direção                          |   |            |
| **Reflexivo**              | todo vértice tem laço                               |   |            |
| **Vazio**                  | V ≠ ∅, A = ∅                                        |   |            |
| **Nulo**                   | V = ∅, A = ∅                                        |   |            |
| **Trivial**                |                                                     | V | = 1, A = ∅ |
| **Hipergrafo**             | arestas podem ligar > 2 vértices                    |   |            |

---

## 4. Conceitos de arestas e vértices

* **Adjacência:** vértices u e v são adjacentes se (u, v) ∈ A.
* **Laço:** aresta (v, v).
* **Arestas paralelas:** múltiplas arestas com mesmas extremidades.

---

## 5. Grau de vértice

* **Grau(v)** (grafo não orientado): nº de arestas incidentes em v.
* Orientado:

  * **grau-entrada** (v) = arcos que chegam.
  * **grau-saída** (v) = arcos que saem.

### Limites

* Grau mínimo: **0** (vértice isolado).
* Grau máximo em grafo simples: **n − 1**.

---

## 6. Propriedades numéricas

| Propriedade                            | Expressão                              |
| -------------------------------------- | -------------------------------------- |
| **Máximo de arestas** em grafo simples | m\_max = n(n − 1)/2                    |
| **Teorema do Aperto de Mãos**          | Σ grau(v) = 2 a                        |
| **Corolário**                          | nº de vértices de grau ímpar é **par** |

*Demonstração-chave:* cada aresta contribui 2 à soma dos graus, pois toca dois vértices.

---

## 7. Grafos especiais frequentes

| Nome                          | Descrição / Notação                    |
| ----------------------------- | -------------------------------------- |
| **Completo (Kₙ)**             | todo par de vértices conectado         |
| **Bipartido**                 | V = U ∪ W, arestas só entre U e W      |
| **Bipartido completo (Kₘ,ₙ)** | todo vértice de U liga-se a todos de W |
| **k-regular**                 | grau(v)=k ∀ v                          |

*Observação:* grafos bipartidos **não podem** ter laços.

---

## 8. Subgrafos

| Categoria                       | Condição                                                            |
| ------------------------------- | ------------------------------------------------------------------- |
| **Subgrafo**                    | V\_H ⊆ V, A\_H ⊆ A                                                  |
| **Próprio**                     | (V\_H ⊂ V ∨ A\_H ⊂ A)                                               |
| **Parcial (spanning subgraph)** | V\_H = V                                                            |
| **Induzido**                    | contém **todas** as arestas entre vértices de V\_H que existem em G |
| **Abrangente (gerador)**        | sinônimo de parcial                                                 |

---

## 9. Clique

* **Clique:** subgrafo induzido **completo**.
* **Clique maximal:** não pode ser estendido (inclusão).
* **Clique máximo:** tem o maior |V| possível (problema NP-difícil).

---

## 10. Grafos ponderados & rotulados

| Tipo          | Definição                                                                    |
| ------------- | ---------------------------------------------------------------------------- |
| **Ponderado** | cada aresta (ou vértice) recebe um peso numérico (custo, distância, tempo …) |
| **Rotulado**  | vértices/arestas têm identificadores ou rótulos textuais                     |

---

## 11. Abstração & resolução de problemas

```
Problema real
   ↓ modelagem
   grafo G
   ↓ algoritmo
   solução
```

### Exemplos de problemas em grafos

* **Conectividade:** existe caminho entre todo par de vértices?
* **Menor caminho:** Dijkstra, Bellman-Ford, A\*.
* **Alcance (reachability):** BFS/DFS.
* **Emparelhamento máximo** (bipartido ou geral).
* **Ciclo hamiltoniano / Clique máximo:** problemas intratáveis (NP-completos).

---

## 12. Teoremas clássicos (resumo)

| Teorema                        | Enunciado essencial                |   |           |
| ------------------------------ | ---------------------------------- | - | --------- |
| **Aperto de Mãos**             | Σ grau(v) = 2                      | A |           |
| **Paridade dos graus ímpares** | nº de vértices de grau ímpar é par |   |           |
| **Máx. arestas grafo simples** |                                    | A | ≤n(n−1)/2 |

---

## 13. Exercício-guia (auto-cheque)

1. Mostre que um grafo r-regular com n vértices tem m = (r · n)/2 arestas.
2. Verifique se um grafo dado é bipartido; apresente U e W ou explique a falha (∀ ciclos ímpares → não bipartido).
3. Para n = 8, desenhe K₈ e confirme a fórmula de |A|.
4. Aplique o Teorema do Aperto de Mãos em qualquer grafo pequeno e conte graus manualmente.

---

## 14. Bibliografia recomendada

* Cormen et al. **Algoritmos – Teoria e Prática** (caps. 22–26)
* Gross & Yellen **Graph Theory and Its Applications** (2ª ed.)
* Sedgewick **Algorithms in Java, Part 5 – Graph Algorithms**
* Goldbarg & Goldbarg **Grafos: Conceitos, Algoritmos e Aplicações**

---

### ✔️ Pronto!

Este resumo agora inclui **todos** os tópicos listados nos slides: definição, notação, propriedades numéricas (graus, aperto de mãos), classificações, subgrafos, cliques, grafos ponderados/rotulados e problemas clássicos.

Se precisar de:

* **Flashcards**,
* **Lista de exercícios com gabarito**,
* **Mapa mental em PDF**,

é só pedir! Bons estudos.
