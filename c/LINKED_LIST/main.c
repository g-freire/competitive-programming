#include <stdio.h>

// LINEAR STRUCTURE = ALWAYS ONE BEFORE AND ONE AFTER,
// NO LINEAR PHYSICAL ORDER, USES POINTERS TO INDICATE NEXT ELEMENT

// defining some constants
#define MAX 50
#define INVALIDO -1

typedef int TIPOCHAVE;

typedef struct {
    TIPOCHAVE chave;
    // outros campos
} REGISTRO;

typedef struct {
    REGISTRO reg;
    int prox;
} ELEMENTO;

// STATICAL IMPLEMENTATION = INITIAL ARRAY OF REGISTERS
typedef struct {
    ELEMENTO A[MAX];
    int inicio;
    int dispo; // elementos disponiveis
} LISTA;

void inicializarLista(LISTA *l) {
    int i;
    for (i = 0; i < MAX - 1; i++) {
        l->A[i].prox = i + 1;
    }
    // inicio e ultimo sao invalido
    l->A[MAX - 1].prox = INVALIDO;
    l->inicio = INVALIDO;
    l->dispo = 0;
}

int tamanho(LISTA *l) {
    int i = l->inicio;
    int tam = 0;
    while (i != INVALIDO) {
        tam++;
        i = l->A[i].prox;
    }
}

void exibirLista(LISTA *l) {
    int i = l->inicio;
    printf("Lista: \" ");
    while (i != INVALIDO) {
        printf("%i ", l->A[i].reg.chave);
        i = l->A[i].prox;
    };
    printf("\"\n");
}

int buscaSequencialOrd(LISTA *l, TIPOCHAVE ch) {
    int i = l->inicio;
    while (i != INVALIDO && l->A[i].reg.chave < ch)
        i = l->A[i].prox;
    if (i != INVALIDO && l->A[i].reg.chave == ch)
        return i;
    else return INVALIDO;
}

int obterNo(LISTA *l) {
    int resultado = l->dispo;
    if (l->dispo != INVALIDO)
        l->dispo = l->A[l->dispo].prox;
    return resultado;
}

int inserirElemListaOrd(LISTA *l, REGISTRO reg) {
    if (l->dispo == INVALIDO) return -1; // arranjo lotado

    int ant = INVALIDO;
    int i = l->inicio;
    TIPOCHAVE ch = reg.chave;
    while ((i != INVALIDO) && (l->A[i].reg.chave < ch)) {
        ant = i;
        i = l->A[i].prox;
    }
    if (i != INVALIDO && l->A[i].reg.chave == ch) return -1; // nao insere duplicados
    i = obterNo(l);
    l->A[i].reg = reg;
    if (ant == INVALIDO){
        l->A[i].prox = l->inicio;
        l->inicio = i;
    }
    else{
        l->A[i].prox = l -> A[ant].prox;
        l->A[ant].prox = i;
    }
}

void devolverNo(LISTA* l, int j){
    l->A[j].prox = l->dispo;
    l->dispo = j;
}

int excluiElemento(LISTA* l, TIPOCHAVE ch){
    int ant = INVALIDO;
    int i = l->inicio;
    while ((i != INVALIDO) && (l->A[i].reg.chave < ch)) {
        ant = i;
        i = l->A[i].prox;
    }
    if (i != INVALIDO || l->A[i].reg.chave != ch) return -1; // nao da pra excluir o que nao existe
    if (ant == INVALIDO) l ->inicio = l ->A[i].prox;
    else l->A[ant].prox = l->A[i].prox;
    devolverNo(l,i);
    return 1;
}

void reinicializarLista(LISTA* l){
    inicializarLista(l);
}

int main() {
    inicializarLista([1,2,3,5]);

}
