## 📘 RESUMO - CONEXIDADE & OPERAÇÕES (com resolução dos exercícios)

---

Claro! Aqui está a tabela atualizada com os dois novos conceitos que você forneceu:

---

### 1. Conceitos-chave

| Termo                                            | Definição curta                                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| **Grafo conexo**                                 | Para **todo** par de vértices existe um caminho.                                             |
| **Grafo subjacente**                             | Versão **não direcionada** de um dígrafo (remove a orientação das arestas).                  |
| **Subgrafo maximal (Goldbarg)**                  | Subgrafo com uma propriedade (ex: ser conexo) que **não pode ser expandido** sem perdê-la.   |
| **Componente conexa**                            | Subgrafo **conexo-maximal**.                                                                 |
| **Conexidade em vértices** `k_v(G)`              | Menor nº de **vértices** cuja remoção desconecta G. (articulação múltipla)                   |
| **Conexidade em arestas** `k_e(G)`               | Menor nº de **arestas** cuja remoção desconecta G.                                           |
| **Grafo k-conexo**                               | `k_v(G) ≥ k`  ⇔  existem ≥ k caminhos **internamente disjuntos** entre quaisquer 2 vértices. |
| **Conjunto de desconexão**                       | Conjunto **mínimo** de vértices cuja retirada separa o grafo.                                |
| **Conjunto aresta-desconectante**                | Análogo com arestas.                                                                         |
| **Ponte**                                        | Aresta única cuja remoção desconecta G.                                                      |
| **Fortemente / fracamente conectado** (dígrafos) | Caminhos em **ambas** direções / somente **uma** direção.                                    |


---

### 2. Operações com grafos

*Para grafos não-orientados, vértices disjuntos $V_1\cap V_2=\varnothing$.*

| Operação                              | Descrição                                                                                             |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **União** $G_1∪G_2$                   | $V=V_1∪V_2,\;E=E_1∪E_2$                                                                               |
| **Interseção**                        | $V=V_1∩V_2,\;E=E_1∩E_2$ (precisa de rótulos)                                                          |
| **Soma / Join**                       | União **+** todas as arestas entre $V_1$ e $V_2$.                                                     |
| **Complemento**                       | Mesmo V; arestas = pares ausentes de G.                                                               |
| **Produto cartesiano** $G_1×G_2$      | $V = V_1×V_2$; aresta se “projeta” em aresta de um dos fatores.                                       |
| **Contração de vértices** $v,w\to vw$ | Funde vértices; substitui incidentes por arestas ao novo vértice; remove laço e identifica paralelas. |

---

### 3. Exercício 1 – *k*-conectividade do grafo (figura dos dois $K_5$)

![](sandbox:/mnt/data/f917bc1a-8c3c-40fb-b80f-0c8be4f550ee.png)

1. **Entenda a ponte lógica**

   * Esquerda: vértices $\{1,2,3,4,5\}=K_5$.
   * Direita: vértices $\{6,7,8,9,10\}=K_5$.
   * Ligações cruzadas: $2–6,\;3–6,\;3–9$.

2. **Cortes mínimos de vértices**

   * Remover **{ 2, 3 }** elimina **todas** as ligações entre os cliques → grafo separado.
   * Qualquer remoção de **1** vértice ainda deixa outro caminho cruzando.
     ⇒ `k_v(G)=2`.

3. **Cortes mínimos de arestas**

   * As 3 arestas cruzadas formam o único “pescoço”. Retirar **duas** delas (por ex. $2–6$ e $3–6$) já isola os cliques.
     ⇒ `k_e(G)=2`.

4. **k-conectividade**

   * Como `k_v(G)=2`, o grafo é **2-conexo** (há ≥ 2 caminhos internamente disjuntos entre quaisquer pares).

5. **Aplicação - Disponibilidade de rede**

   * Em redes de computadores, $k_v$ e $k_e$ medem quanto de falha simultânea a topologia suporta antes de perder conectividade global.

---

### 4. Exercício 2 – Contração dos vértices $u$ e $v$

Antes (6 vértices):

```
a──6──v──2──b
╲   ╲  ╱ \
 5   6/    5
  ╲  ╱1     \
   u──6──d──2──c
   ╲        ╲
    8────────╱
```

* $a$: extremo esquerdo  $b$: topo-direita
* $c$: direita inferior  $d$: inferior-esquerda

**Passo de contração** $u,v \to w$:

* Novo vértice **w** herda os vizinhos de $u$ e $v$.
* Paralelas $a\!-\!w$ (5 & 6) e $b\!-\!w$ (2 & 1) podem ser **fundidas** (ficando com a menor ou mantendo multiareste, conforme modelo).

#### Grafo resultante (5 vértices: $w,a,b,c,d$)

| Aresta | Obs.                   |
| ------ | ---------------------- |
| $w–a$  | única (fusão de 5 & 6) |
| $w–b$  | única (fusão de 1 & 2) |
| $w–d$  | peso 6                 |
| $a–d$  | peso 8                 |
| $b–c$  | peso 5                 |
| $c–d$  | peso 2                 |

Todas as demais ligações permanecem como no pentágono externo.

---

### 5. Checklist rápido para provas

1. **kv(G)** = menor nº de vértices que cortam G.
2. **ke(G)** = menor nº de arestas que cortam G.
3. *k*-conexo ⇔ `kv(G) ≥ k (⇒ ke(G) ≥ k)`.
4. Num dígrafo use **grafo subjacente** para testar conexidade “clássica”.
5. Para verificar bipartição → procure ciclo ímpar; para k-conectividade → procure cortes mínimos.
6. Contraction, join, complemento, produto cartesiano: caem muito em exercícios de construção.

Bons estudos!
