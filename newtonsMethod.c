/*This is a program to find the real and imaginary roots or any degree polynomial with any real coefficients. The program will prompt you for the degree of
the polynomial and then the coefficients from the x^n coefficient to the x^0 coefficient. the program will then spit out each xi root at the end of the program
The method used is newton's method, a process of iterative guesses.*/


#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <stdlib.h>

//complex.h does not include a way function for printing complex numbers. So I had to write a function to do that.
void printComplex(complex z)
{double real,imag,absimag;
  real = creal(z);
  imag = cimag(z);
  absimag = fabs(imag) ;

  if(imag<0){printf("%lf - %lfi\n",real,absimag);}
    else{printf("%lf + %lfi\n",real,absimag);}
}


int main()
{

  complex x,f,d;
  complex a[100];
  double coef;
  int i,n,r,m,z,t;
  complex tmp ;

  srand48(100) ;

  //get degree from user. Now n is number of coefficients of the polynomial
	printf("Degree?:\n");
	scanf("%d",&r);
	n = r+1;

  //get coefficients from user. The coefficients go into array a and are declared as an imaginary number with imaginary component of 0
	for(i=n;i>0;i--){
		printf("coefficient %d?\n",n+1-i);
		scanf("%lf",&coef);
		a[i] = coef + 0.0*I;
	}
 
	for(z=n;z>=1;z--){ printComplex(a[z]) ;  printf("\n") ; 
	}


  //Beginning of big loop to find all roots. Stop when we have found n roots
	for(m=0;m<r;m++){
	//generate random guess
       x = 10*drand48()+10*drand48()*I;        
  //to get a root
		for(t=0;t<50;t++){
			f = 0.0+0.0*I;
			d = 0.0+0.0*I;

                   //loop to evaluate f (polynomial) and d (derivative) at our current xi.
			for(i=n;i>=1;i--){
           
				f = x*f + a[i]; // computing f at x
              
				if(i==1){d = d;}

				else{d = x*d + f;} //computing d at x
			}              
           
			/*this is the formula for newton’s method to get the next guess for x. And we start all over again ☺.*/ 
			x = x - (f/d) ; 

		}

//We just got a root, so print to the screen
      printf("x%d= ", m+1);   printComplex(x);
      
         /* Factor out the root (divide by the polynomial x-root) and get a new polynomial for next iteration, This is using synthetic division again.?)*/
        for(z=n;z>=1;z--){
			if(z==n){a[z] = a[n];}
            else{a[z]=x*a[z+1]+a[z];}
        }
     
         //Here we just  need to scoot the smaller polynomial into a better position in a. Right now we’ve got an emply cell at the end, where the one’s place should be.
        for(z=1;z<n;z++){
			a[z]=a[z+1]; 
        }     
		n--;
		}
      printf("---------------------------------------------\n");

	}

