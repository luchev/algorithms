#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * Calculate the Nth fibonacci term using the formula
 *
 * Time complexity: O(1)
 * Space complexity: O(1)
 *
 * Pro: O(1) time and space complexity
 * Con: The low precision of type double makes the program work only for the first 60ish terms.
 *
 * Compile: gcc -lm fibonacci-formula.c
 */
int main(int argc, char* argv[]) {
	if (argc != 2) {
		printf("Provide exactly one number as arguement\n");
		return 1;
	}

	int ithTerm = atoi(argv[1]);
	long double sqrt5 = sqrt(5);
	unsigned long long fibonacci = (pow((1 + sqrt5)/2, ithTerm) - pow((1 - sqrt5)/2, ithTerm)) / sqrt5;
	printf("%lu\n", fibonacci);
	return 0;
}
