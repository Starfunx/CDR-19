#ifndef RST
#def RST

class rst {
  public:
    //constructor
    rst();
    rst(float R[], float S[], float T[]);

    void setR(float R[]);
    void setS(float S[]);
    void setT(float T[]);

    void setConsigne(float consigne);
    float getCommand(float mesure, float consigne);

  private:
    float _R[4] = {0};
    float _S[4] = {0};
    float _T[4] = {0};

    float _consigne[4] = {0};
    float _mesure  [4] = {0};
    float _commande[4] = {0};

    void reIndex(float newValue, float* array);

};

#endif
