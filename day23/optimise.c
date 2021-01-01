int main() {
    int a, b, c, d, e, f, g, h=0;
    a = 1;      // pre condition
    b = 67;     // set b 67
    c = b;      // set c b
                // jnz a 2 skips 
                // (skipped) jnz 1 5
    b *= 100;   // mul b 100
    b += 100000;// sub b -100000
    c = b;      // set c b
    c += 17000; // sub c -17000;
l12:f = 1;      // set f 1
    d = 2;      // set d 2
l14: e = 2;      // set e 2
l15: g = d;      // set g d
    g *= e;     // mul g e
    g -= b;     // sub g b
    if (g != 0) goto l21; // jnz g 2
    f = 0;      // set f 0
l21:e -= -1;     // sub e -1
    g = e;      // set g = e
    g -= b;     // sub g b
    if (g != 0) goto l15; // jnz g -8
    d += 1;    // d -1
    d = g;      // set g d
    g -= b;     // sub g b
    if (g != 0) goto l14; // jnz g -13
    if (f != 0) goto l31; // jnz f 2
    h += 1;    // sub h -1
l31:g = b;      // set g b
    g -= c;     // sub g c
    if (g == 0) return h; // jnz g 2
    b += 17;   // sub b -17
    goto l12;   // jnz 1 -23
}

