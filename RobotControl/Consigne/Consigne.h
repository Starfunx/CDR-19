#ifndef CONSIGNE_H
#define CONSIGNE_H

#include <math.h>

#ifndef PI
#define PI 3.1415926535897932384626433832795
#endif

class Consigne{

public:
Consigne(double x, double y, double theta);

void setConsigne(double x_c, double y_c, double theta_c);

void getConsigne(double* x_c, double* y_c, double* theta_c);

void getsNewError(double* distance, double* cap, double x, double y, double theta);

void getsNewError(double* distance, double* cap, double x, double y, double theta,
                  double* erreurX, double* erreurY, double* erreurCap );


private:
double m_x_c, m_y_c, m_theta_c;

double m_dist, m_cap;

double m_erreurX, m_erreurY, m_erreurCap;

protected:
void  processNewError(double x, double y, double theta);
};


#endif
