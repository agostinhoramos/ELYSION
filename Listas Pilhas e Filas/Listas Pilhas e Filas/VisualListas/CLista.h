//---------------------------------------------------------------------------

#ifndef CListaH
#define CListaH

class Elemento {
    int info;
public:
    void PoeInfo(int inf) { info =  inf;}
    int TiraInfo() { return info;}
   	Elemento *proximo;
		Elemento(int e) {
			info = e;
			proximo = 0;
		}
    Elemento() {
     	info = 0;
		  proximo = 0;
		}
};
class LISTA {
  private:
     Elemento * inicio;
  public:
    LISTA() { inicio = 0;}
    ~LISTA();
    void InserirInicio(int e);
    void InserirFim(int e);
    void EliminarInicio();
    void EliminarFim();
    void ListarLista();
    bool Vazia();
    int Tamanho();
    void InserirOrdenado(int e);
    void EliminarElemento(int e);
    void EliminarElementos(int e);
    void EliminarDeUmElementoAteFim(int e);
    void EliminarDoInicioAteElemento(int e);
    void EliminarRepetidos();
    int ContarElememto(int e);
    Elemento * GetInicio();
};
//---------------------------------------------------------------------------
#endif
