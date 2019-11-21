#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int i;
	for(i=0; i<10; i+=2){//for in range(0,10,1):
		printf("Hola %d \n",i);
	}

	int j;
	for(j=0; j<6; j+=1){
		int i;
		for(i=0; i<11; i+=1){
			if(j==0 || j==5 || i==0 || i==10)
			printf("#");
			else{
				printf(" ");
			}
		}
	    printf("\n");  
	}

	return 0;


}
/*
#####
####
###
##
#

#####
 ####
  ###
   ##
    #

#
##
###
####
#####

