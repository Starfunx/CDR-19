#include "rst.h"

rst::rst(){}

rst::rst(float R[], float S[], float T[]){
  _R = R;
  _S = S;
  _T = T;
}

void rst::setR(float R[]){
_R = R;
}

void rst::setS(float S[]){
_S = S;
}

void rst::setT(float T[]){
_T = T;
}

void rst::setConsigne(float consigne){
    reIndex(consigne, _consigne);
}

float rst::getCommand(float mesure, float consigne = _consigne[0]){
    float result = 0;
    reIndex(mesure, _mesure);
    reIndex(consigne, _consigne);

    /*
     newCommand / S[0] =
        command[1:] / S[1:]
     +  consigne[] * T[]
     -  mesure[]   * R[]
    */
    for (int i = (sizeof (_commande) / sizeof (_commande[0]))-1; i>1; i--)
        result = result + _commande[i] / _S[i];
    for (int i = (sizeof (_consigne) / sizeof (_consigne[0])); i>1; i--)
        result = result + _consigne[i] * _T[i];
    for (int i = (sizeof (_mesure) / sizeof (_mesure[0])); i>1; i--)
        result = result - _mesure[i] * _R[i];
    result = result * _S[0];

    reIndex(result, _commande);
    return result;
}

void rst::reIndex(float newValue, float* array){
    for (int i = sizeof (array) / sizeof (array[0]); i>1; i--)
        array[i] = array[i-1];
    array[0] = newValue;
}
