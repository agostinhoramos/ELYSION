//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused


#include "CLista.h"
#include <iostream.h>

int main(int argc, char* argv[])
{


  Elemento * e1 = new Elemento(10);
  Elemento * e2 = new Elemento(23);
  Elemento * e3 = new Elemento(34);
  Elemento * e4 = new Elemento(78);
  Elemento * e5 = new Elemento(87);


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


  Elemento * aux;
  aux = e1;
  for(;aux;) {
    cout << aux->info << endl;
    aux = aux->proximo;
  }


  return 0;
}
//---------------------------------------------------------------------------
