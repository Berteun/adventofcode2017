#include <stdio.h>

int part2() {
  int h=0;

  // Basically finds some primes
  for (int b = 106700; b <= 123700; b += 17) {
    for (int d = 2; d * d < b; d++) {
      if (b % d == 0) {
        h += 1;
        break;
      }
    }
  }
  return h;
}

int main() {
  printf("%d\n", part2());
}
