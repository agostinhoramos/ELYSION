#include "CLista.h"
#include <iostream.h>

//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

int main(int argc, char* argv[])
{


 Elemento * e1 = new Elemento(10);
  Elemento * e2 = new Elemento(23);
  Elemento * e3 = new Elemento(34);
  Elemento * e4 = new Elemento(78);
  Elemento * e5 = new Elemento(87);

  Elemento e6;
  e6.info = 0;


  e1->proximo = e2;
  e2->proximo = e3;
  e3->proximo = e4;
  e4->proximo = e5;

  // v1
  cout << "V1" << endl << endl;
  cout << e1->info << endl;
  cout << e2->info << endl;
  cout << e3->info << endl;
  cout << e4->info << endl;
  cout << e5->info << endl;

  // v2
  cout << "V2" << endl << endl;
  cout << e1->info << endl;
  cout << e1->proximo->info << endl;
  cout << e1->proximo->proximo->info << endl;
  cout << e1->proximo->proximo->proximo->info << endl;
  cout << e1->proximo->proximo->proximo->proximo->info << endl;

  // v3
  cout << "V3 - ciclo" << endl << endl;

  Elemento *aux;
  aux = e1;
  for(;aux;) {
    cout << aux->info << endl;
    aux = aux->proximo;
  }

  LISTA lista;


  lista.InserirInicio(10);
  lista.InserirInicio(23);
  lista.InserirInicio(34);
  lista.InserirInicio(78);
  lista.InserirInicio(87);
  cout << "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  lista.EliminarInicio();
  cout << "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  /*lista.EliminarInicio();
  lista.EliminarInicio();
  lista.EliminarInicio();
  lista.EliminarInicio();*/

  cout << "Tamanho: " << lista.Tamanho()<< endl;

  lista.InserirFim(99);
  lista.ListarLista();

  lista.EliminarFim();
  //lista.ListarLista();

  lista.EliminarFim();
  //lista.ListarLista();

  lista.EliminarFim();
  //lista.ListarLista();

  lista.EliminarFim();
  //lista.ListarLista();

  lista.EliminarFim();
  lista.EliminarFim();
  lista.ListarLista();

  cout << endl<< "Tamanho: " << lista.Tamanho() << endl;

  lista.InserirOrdenado(78);
  lista.InserirOrdenado(34);
  lista.InserirOrdenado(87);
  lista.InserirOrdenado(10);
  lista.InserirOrdenado(23);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  lista.EliminarElemento(10);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  lista.EliminarElemento(87);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();


  lista.EliminarElemento(34);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  lista.EliminarElemento(340);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();


  lista.EliminarElemento(23);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();

  lista.EliminarElemento(78);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();


   lista.EliminarElemento(7823320);
  cout << endl<< "Tamanho: " << lista.Tamanho()<< endl;
  lista.ListarLista();



  return 0;
}
//---------------------------------------------------------------------------
 