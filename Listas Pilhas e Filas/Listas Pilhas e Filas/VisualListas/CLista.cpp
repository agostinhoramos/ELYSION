//---------------------------------------------------------------------------

#include "CLista.h"
#include <stdlib.h>
#include <alloc.h>
#include <iostream.h>

void LISTA::InserirInicio(int e)
{
    Elemento *novo = new Elemento(e);
    novo->proximo = inicio;
    inicio = novo;
}
void LISTA::InserirFim(int e)
{
  Elemento *aux = inicio;
  Elemento *ant = aux;

  if (!inicio)
    InserirInicio(e);
  else {
    for(;aux;) {
      ant = aux;
      aux = aux->proximo;
    }
    Elemento *novo = new Elemento(e);
    ant->proximo = novo;
  }
}
void LISTA::EliminarInicio()
{
   Elemento *aux = inicio;
   if (inicio) {
     inicio = inicio->proximo;
     delete aux;
   }
}
void LISTA::EliminarFim()
{
  if (inicio)
    if (inicio->proximo) {                  // 2 ou + elementos
      Elemento *aux = inicio->proximo;
      Elemento *ultimo = inicio;
      Elemento *penultimo = 0;
      for(;aux;) {
        penultimo = ultimo;
        ultimo = aux;
        aux = aux->proximo;
      }
      penultimo->proximo = 0;
      delete ultimo;
    } else {                                // um elemento
       EliminarInicio();
    }

}

Elemento * LISTA::GetInicio()
{
  return inicio;
}
void LISTA::ListarLista()
{
  Elemento *aux;
  aux = inicio;
  cout << endl << "Listar" << endl;
  for(;aux;) {
    cout << aux->info << endl;
    aux = aux->proximo;
  }
}
bool LISTA::Vazia()
{
  return (inicio == 0);
}
void LISTA::InserirOrdenado(int e)
{
  /*
  Em primeiro lugar vamos determinar onde ficará o novo nó
  que irá ser adicionado à lista, para conter o valor
  especificado. Para isso vamos determinar qual o nó que
  fica antes do novo e qual o nó que fica depois.
  */

  /*
  Partimos do princípio que o novo nó vai ficar antes de
  todos os outros da lista, portanto antes dele não há
  nenhum e depois dele vem o primeiro.
  */
  Elemento * anterior = 0;
  Elemento * seguinte = inicio;

  /*
  E agora vamos procurar a posição exacta do novo nó. Para
  tal vamos deslocar-nos para a frente na lista enquanto
  não chegarmos ao fim desta (se já chegamos ao fim da
  lista, isto é se seguinte é NULL, é porque o novo nó
  fica depois de todos os outros) e enquanto o valor que
  andamos à procura for maior que o valor do nó que deve
  ficar a seguir (O valor do nó que fica a seguir do novo
  nó deverá ser sempre maior que o valor contido no novo
  nó).
  */
  while(seguinte != NULL && seguinte->info < e) {
    /*
    Vamos então deslocar-nos para a frente. O nó
    anterior ao novo passa a ser aquele que é agora
    o seguinte e o seguinte passa a ser aquele que
    está à frente daquele que é actualmente o
    seguinte.
    */
    anterior = seguinte;
    seguinte = seguinte->proximo;
  }

  /*
  Uma vez encontrada a posição do novo nó, vamos então
  criá-lo e colocar no atributo valor o valor que
  pretendemos que ele guarde.
  */
  Elemento * novo = new Elemento;
  novo->info = e;

  /*
  Resta-nos agora introduzi-lo na lista. Se antes do nosso
  novo nó não existe nenhum, ele passa a ser o primeiro,
  logo o ponteiro primeiro deve apontar para o nosso novo
  nó. Senão temos que indicar que o nó que vem a seguir ao
  nó que fica antes do nosso novo nó é precisamente o novo
  nó.
  */
  if (anterior == 0)
    inicio = novo;
  else
    anterior->proximo = novo;

  /*
  Para acabar de ligar o novo nó à lista temos ainda que
  indicar que o nó que vem a seguir ao novo é aquele que
  já tínhamos determinado previamente como vindo depois do
  novo nó.
  */
  novo->proximo = seguinte;
}
void LISTA::EliminarElemento(int e)
{
  /*
  Para retirarmos um valor da lista, ao contrário do que
  acontecia nas pilhas e nas filas, temos de especificar
  qual o valor a retirar. Então o primeiro passo para
  removermos um dado valor na lista será o de procurarmos
  o nó (a apagar) que contém esse mesmo valor.
  */

  /*
  Partimos do princípio que o nó a apagar é o primeiro.
  Portanto antes dele não há nenhum.
  */
  Elemento * anterior = 0;
  Elemento * actual   = inicio;

  /*
  E agora vamos procurar a posição exacta do nó a apagar.
  Para tal vamos deslocar-nos para a frente na lista
  enquanto não chegarmos ao fim desta (se já chegamos ao
  fim da lista, isto é se actual é NULL, é porque não
  existe um nó com o valor especificado) e enquanto o
  valor que andamos à procura for maior que o valor do nó
  actual (Se o nó actual tem um valor maior ou igual
  àquele que andamos à procura então ou já encontramos o
  nó contendo o valor que andamos à procura ou não existe
  nenhum nó na lista com esse valor (não nos podemos
  esquecer que a lista está ordenada)).
  */
  while(actual != NULL && actual->info < e) {
    anterior = actual;
    actual   = actual->proximo;
  }

  // se encontramos o elemento a apagar (actual)
  if (actual != NULL && actual->info == e) {
    /*
    se ó nó a apagar é o primeiro, o primeiro deverá
    passar a ser aquele que vem depois do nó que
    vamos apagar. Senão o nó que vem depois do nó
    que está antes do que vamos apagar passa a ser
    aquele que vem depois do que vamos apagar.
    */
    if (anterior == 0)          // if (actual == primeiro)
      inicio = actual->proximo;
    else
      anterior->proximo = actual->proximo;

    /*
    Podemos apagar agora o nó, uma vez que já
    estabelecemos as ligações entre o nó que estava
    antes deste e o que vinha depois.
    */
    delete actual;
  }
}
void LISTA::EliminarElementos(int e)
{
}
void LISTA::EliminarDeUmElementoAteFim(int e)
{
}
void LISTA::EliminarDoInicioAteElemento(int e)
{
}
void LISTA::EliminarRepetidos()
{
}
int LISTA::ContarElememto(int e)
{
}
int LISTA::Tamanho()
{
  int c = 0;
  Elemento *aux = inicio ;
  while (aux != 0) {
    aux = aux->proximo;
    c++;
  }
  return c;
}


/*
    Vamos apagar o primeiro elemento, mas antes
    guardamos o elemento que vem depois
    do primeiro, já que este passará, depois de
    apagarmos aquele que é o primeiro, a ser o
    primeiro.
*/
LISTA::~LISTA()
{

  while (inicio != 0) {
    Elemento * segundo = inicio->proximo;
    delete inicio;
    inicio = segundo;
  }
}

/*
int *v= (int *) malloc(100 * sizeof(int));
free(v);

int *v2 = new int[100];
delete [] v2;*/




/*void LISTA::InserirOrdenado(int e)
{
  Elemento * seguinte = inicio;
  while((seguinte != 0) && (seguinte->info < e))
    seguinte = seguinte->proximo;
  Elemento * novo = new Elemento(e);
  novo->proximo = seguinte;
  if (seguinte == NULL) {   // ins fim
    novo->anterior = fim;
    fim = novo;
  } else {
    novo->anterior = seguinte->anterior;
    seguinte->anterior = novo;
  }
  El emento * ant = novo->anterior;
  if (ant == NULL)
    inicio = novo;
  else
    ant->proximo = novo;
} */

