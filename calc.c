// This is a calculator program written in C
// BY: Korey Moffett (KaosFang)
// DATE: Fri, Feb 05

#include <stdio.h>
#include <stdlib.h>

int main(){

    float numOne, numTwo;
    char oper;

    printf("Please input a number\n");
    printf(">>> ");
    scanf("%f", &numOne);
    system("clear");
    printf("Please input the operation you would like to perform\n");
    printf("----------------------\n");
    printf("|     Operations     |\n");
    printf("----------------------\n");
    printf("| [+] addition       |\n");
    printf("| [-] subtraction    |\n");
    printf("| [*] multiplication |\n");
    printf("| [/] division       |\n");
    printf("----------------------\n\n");
    printf(">>> ");
    scanf("%s", &oper);
    system("clear");
    printf("Please input another number\n");
    printf(">>> ");
    scanf("%f", &numTwo);
    system("clear");

    // LOGICAL

    switch(oper){
        case '+':
            printf("Answer: %f\n", numOne +  numTwo);
            break;
        case '-':
            printf("Answer: %f\n", numOne - numTwo);
            break;
        case '*':
            printf("Answer: %f\n", numOne * numTwo);
            break;
        case '/':
            printf("Answer: %f\n", numOne / numTwo);
            break;
        default:
            printf("Please enter a valid operation");
    }



}
