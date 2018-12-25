#include <stdio.h>
#include <curses.h>
#include <string.h>
#include <math.h>

uint32_t msgDigest[5], key[4], A, B, C, D, E;
#define SHA1CircularShift(bits,word) \
                (((word) << (bits)) | ((word) >> (32-(bits))))

void printMessageGoingToBeProcessed(uint32_t * message) {
    printf("\n");
    int iterator = 0;
        while (iterator<15) {
            printf("%08x ",message[iterator++]);
            printf("%08x ",message[iterator++]);
            printf("%08x ",message[iterator++]);
            printf("%08x \n",message[iterator++]);
        }
}

void commonAlgorithm(uint32_t hashResult, uint32_t word, uint32_t key) {
    hashResult = hashResult + key + SHA1CircularShift(5, A) + word + E;
    E = D;
    D = C;
    C = SHA1CircularShift(30,B);
    B = A;
    A = hashResult;
}

void messageHashing(uint32_t * message) {
    //Now i have the message, Time to hash it.
    // Initiate
        int iterator;
        uint32_t hashResult, word[80];
        A = msgDigest[0];
        B = msgDigest[1];
        C = msgDigest[2];
        D = msgDigest[3];
        E = msgDigest[4];
    // Calculate for the message
        for (iterator=0;iterator<=79;iterator++) {
            if (iterator < 16)
                word[iterator] = message[iterator];
            else
                word[iterator] = SHA1CircularShift(1,(word[iterator-3] ^ word[iterator-8] ^ word[iterator-14] ^ word[iterator-16]));
            if(iterator >=0 && iterator <= 19) {
                hashResult = ((B & C) | ((~B) & D));
                commonAlgorithm(hashResult, word[iterator], key[0]);
            } else if (iterator >=20 && iterator <= 39) {
                hashResult = ((B ^ C) ^ D);
                commonAlgorithm(hashResult, word[iterator], key[1]);
            } else if (iterator >=40 && iterator <= 59) {
                hashResult = ((B & C) | (B & D) | (C & D));
                commonAlgorithm(hashResult, word[iterator], key[2]);
            } else if (iterator >=60 && iterator <= 79) {
                hashResult = ((B ^ C) ^ D);
                commonAlgorithm(hashResult, word[iterator], key[3]);
            }
        }
    // Add the values to the msgDigest.
        msgDigest[0] += A;
        msgDigest[1] += B;
        msgDigest[2] += C;
        msgDigest[3] += D;
        msgDigest[4] += E;
}

void main() {
    // Initiate
    char secureHashInput[500];
    uint32_t message[15];
    int charsProcessed=0,charsInMessage, iterator;
    uint64_t inputLenght;
    // Initial Key Values
    key[0] = 0x5A827999;
    key[1] = 0x6ED9EBA1;
    key[2] = 0x8F1BBCDC;
    key[3] = 0xCA62C1D6;
    // Initial msgDigest Values
    msgDigest[0] = 0x67452301;
    msgDigest[1] = 0xEFCDAB89;
    msgDigest[2] = 0x98BADCFE;
    msgDigest[3] = 0x10325476;
    msgDigest[4] = 0xC3D2E1F0;
    // SHA1 Process
        printf("Enter the string to be hashed: ");
        fgets (secureHashInput, 500, stdin);
        // Calculate SHA1
        inputLenght = 8*(strlen(secureHashInput));
        message[14] = inputLenght/pow(2,32);
        inputLenght = inputLenght<<32;
        message[15] = inputLenght/pow(2,32);
        while (charsProcessed < strlen(secureHashInput)) { // This while loop will divide input to 32 bit messages
            for (charsInMessage=0;charsInMessage<=13;charsInMessage++) { // Reseting the entire message to 0 so that no previous value remains
                message[charsInMessage] = 0;
            }
            for (charsInMessage=0;charsInMessage<=13;charsInMessage++) { // Fill in the words for this message
                if(charsProcessed == strlen(secureHashInput)) { // All chars are processed
                    message[charsInMessage++] = 0x80*pow(2,24);
                    break;
                } else if (charsProcessed+4 > strlen(secureHashInput)) { // If the word will not be completely filled with input.
                    iterator = 24;
                    while(1) {
                        if (charsProcessed < strlen(secureHashInput)) {
                            message[charsInMessage] += secureHashInput[charsProcessed++]*pow(2,iterator);
                            iterator=iterator-8;
                        } else {
                            message[charsInMessage] += 0x80*pow(2,iterator);
                            break;
                        }
                    }
                    break;
                } else {
                    message[charsInMessage] =
                        secureHashInput[charsProcessed++]*pow(2,24) +
                        secureHashInput[charsProcessed++]*pow(2,16) +
                        secureHashInput[charsProcessed++]*pow(2,8) +
                        secureHashInput[charsProcessed++];
                }
            }
            charsProcessed += charsInMessage;
            printMessageGoingToBeProcessed(message);
            messageHashing(message);
        }
    // Print the SHA1 Message Digest
    printf("\n%08x%08x%08x%08x%08x is the SHA1 Message Digest.\n",msgDigest[0],msgDigest[1],msgDigest[2],msgDigest[3],msgDigest[4]);
}
