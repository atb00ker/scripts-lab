#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char records[500][20];
void checkUnique(int recording)
{
    int current, counter;
    for(current=0; current<=recording; current++)
    {
        for(counter=current+1; counter<=recording; counter++)
        {
            if(strcmp(records[current],records[counter])==0)
            {printf("%s\n",records[current]);}
        }
    }
}
void main()
{
    char reader[1];
    int recording = 0;
    FILE *fileContainer;
    fileContainer = fopen("records.txt", "r");
        if(!fileContainer)
            { printf("Error 101: No file found!"); }
    reader[0] = fgetc(fileContainer);
        while(reader[0]!=EOF)
        {
            if(reader[0] != ' ') { strcat(records[recording], reader); }
            else { recording++; }
            reader[0] = fgetc(fileContainer);
        }
    checkUnique(recording);
}
