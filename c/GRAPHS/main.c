#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0
typedef int bool;
typedef int TIPOPESO;

// REPRESENTACAO GRAFO POR MATRIZ ADJACENCIA
typedef struct grafo_matriz {
    int vertices;
    int arestas;
    TIPOPESO **adj;
} GRAFO_MATRIZ;


// REPRESENTACAO GRAFO POR LISTA ADJACENCIA (arranjo dos nos com ponteiro para lista ligada das relacoes/arestas)
// possui: n vertices + n arestas + arranjo de vertices

typedef struct adjacencia {
    int vertice;
    TIPOPESO peso;
    struct adjacencia *prox;
} ADJACENCIA;

typedef struct vertice {
    // dados armazenados vao aqui
    // cabeca da lista
    ADJACENCIA *cab;
} VERTICE;

typedef struct grafo {
    int vertices;
    int arestas;
    VERTICE *adj;
} GRAFO;


// OPERATION METHODS https://www.youtube.com/watch?v=1bNHNG0s7ug&list=PLxI8Can9yAHf8k8LrUePyj0y3lLpigGcl&index=25

GRAFO *criarGrafo(int v) {
    // inicializa o grafo sem arestas (null)
    GRAFO *g = (GRAFO *) malloc(sizeof(GRAFO));
    g->vertices = v;
    g->arestas = 0;
    g->adj = (VERTICE *) malloc(v * sizeof(VERTICE));
    int i;
    for (i = 0; i < v; i++)
        g->adj[i].cab = NULL;
    return (g);
}

ADJACENCIA *criaAdj(int v, int peso) {
    ADJACENCIA *temp = (ADJACENCIA *) malloc(sizeof(ADJACENCIA));
    temp->vertice = v;
    temp->peso = peso;
    temp->prox = NULL;
    return (temp);
}

bool criaAresta(GRAFO *gr, int vi, int vf, TIPOPESO p) {
    // para criar uma nao dirigida, chamamos o procedimento 2 vezes (vi,vf) e (vf,vi)

    if (!gr) return false;
    if ((vf < 0) || (vf >= gr->vertices)) return (false);
    if ((vi < 0) || (vf >= gr->vertices)) return (false);
    ADJACENCIA *novo = criaAdj(vf, p);
    novo->prox = gr->adj[vi].cab;
    gr->adj[vi].cab = novo;
    gr->arestas++;
    return (true);
}

void imprimo(GRAFO *gr) {
    printf("Vértices: %d. Arestas: %d. \n", gr->vertices, gr->arestas);
    int i;
    for (i = 0; i < gr->vertices; i++) {
        printf("v%d: ", i);
        ADJACENCIA *ad = gr->adj[i].cab;
        while (ad) {
            printf("v%d (%d) ", ad->vertice, ad->peso);
            ad = ad->prox;
        }
        printf("\n");
    }
}

int main(void) {
    GRAFO * gr = criarGrafo(5);
    criaAresta(gr, 0, 1, 2);
    criaAresta(gr, 1, 2, 4);
    criaAresta(gr, 2, 0, 12);
    criaAresta(gr, 2, 4, 40);
    criaAresta(gr, 3, 1, 3);
    criaAresta(gr, 4, 3, 8);

    imprimo(gr);
}
