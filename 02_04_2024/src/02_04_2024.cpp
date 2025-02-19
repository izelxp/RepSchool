//============================================================================
// Name        : 02_04_2024.cpp
// Author      : Maria Izel Martinez Vera
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <math.h>
#include <tgmath.h>
using namespace std;

class Forma {
private:
	string nombre;

public:
	double virtual Area(){

	}
	double virtual Perimetro(){

	}

	Forma();
	Forma(string nombre){
		this->nombre = nombre;
	}
	string Nombre(){
		return nombre;
	}


};
class Circulo : public Forma {
public:
	double PI =3.1416;


	double RADIO = 0;

	Circulo( double radio, string nombre) :Forma (nombre){
			this->RADIO = radio;

			}

	double Area(){
		return PI*RADIO*RADIO;
	}

	double Perimetro(){
			return 2*PI*RADIO;
		}

};

class Rectangulo : public Forma {
public:
		double ancho = 0;
		double alto = 0;

		Rectangulo(double ancho, double alto, string nombre) :Forma(nombre) {
			this->ancho = ancho;
			this->alto = alto;
		}

		double Area(){
				return ancho*alto;
			}

		double Perimetro(){
					return 2*(ancho+alto);
				}

	};
class Triangulo : public Forma {
public:


	double base = 0;
	double altura = 0;
	Triangulo(double base, double altura, string nombre) :Forma(nombre){
			this->base = base;
			this->altura = altura;

		}
	double Area(){

				return base*altura/2;
					}

	double Perimetro(){

		double H = sqrt((pow(base, 2)) + (pow(altura, 2)));
		double P = base+altura+H;

							return P;


							//PENDIENTE EL PERIMETRO DE UN TRIANGULO YA QUE SE NECESITAN MAS DATOS
						}

};

int main() {

	//vector<Forma> vect;
	//Circulo c = Circulo(5);
	//Rectangulo r= Rectangulo(4,6);
	//Triangulo t= Triangulo(10,5.86);

	//cout << "\t Circulo : " << endl;
	//cout << "\t\t Area: " <<t.Area()<< endl;
	//cout << "\t\t Perimetro: " <<t.Perimetro() << endl;

	Circulo *c_ptr = new Circulo(10,"Circulo");
	Rectangulo *r_ptr = new Rectangulo(4,3, "Rectangulo");
	Triangulo *t_ptr = new Triangulo(3,6, "Triangulo");

	Forma *forma_list []={c_ptr, r_ptr,t_ptr};



	for(int i=0; i<3; i++){
	cout << "\t\t Nombre : " << forma_list[i]->Nombre()<< endl;
	cout << "\t\t Area: " << forma_list [i]->Area()<< endl;
	cout << "\t\t Perimetro: " <<forma_list [i]->Perimetro() << endl;
	cout << "\t******************************* : " << endl;
	}

return 0;
}
