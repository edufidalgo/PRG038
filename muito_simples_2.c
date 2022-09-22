#include <stdio.h>

int main()
{
    float a = 77.2;
    float converte_temperatura(float tempF);
    float temp = converte_temperatura(a);
    printf("%f",temp);

    return 0;
}
float converte_temperatura(float tempF){
    return (tempF -32)/1.8;
}