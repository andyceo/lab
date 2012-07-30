#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

int main() {
  float fahr, celsius;
  int lower, upper, step;

  printf("Fahreheit to Celsius\n");

  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;
  while (fahr <= upper) {
    celsius = (5.0 / 9.0) * (fahr - 32.0);
    printf("%3.0f\t%6.1f\n", fahr, celsius);
    fahr = fahr + step;
  }

  printf("\n\n");

  printf("Celsius to Fahrenheit\n");

  for (celsius = UPPER; celsius >= LOWER; celsius -= STEP) {
    printf("%3.0f\t%6.1f\n", celsius, (9.0 * celsius / 5) + 32.0);
  }

  return 0;
}
