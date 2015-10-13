#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/* Only accurate for small inputs, since we're using fixed-width
   integers. */
int factorial (int x) {
  /* mathematically, factorial isn't defined for negative numbers, and
     yet our spec says we must take a signed integer.  So we
     arbitrarily define the factorial of a negative number to be 1.

     We handle large numbers the same way: if we discover that our
     product has become negative (which indicates that the integer has
     overflowed), we also return 1.
  */
  if (x < 2) {
    return 1;
  }
  int product = 1;
  while (x > 1) {
    product *= x;

    /* check for overflow */
    if (product < 0) {
      return 1;
    }

    x -= 1;
  }
  return product;
}

/* test like so:
 *
 * make factorial && ./factorial 2 5 10 12 13 frotz 14 15
 *
 */
int main (int argc, char *argv[]) {
  argc--;
  argv++;
  while (*argv) {
    int i = strtol (*argv, NULL, 10);
    if (errno) {
      fprintf (stderr, "%s doesn't parse as an integer\n", *argv);
      errno = 0;
    } else {
      printf ("%s => %d => %d\n", *argv, i, factorial (i));
    }
    argv++;
  }
}
