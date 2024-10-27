Let us ignore c1, c2, c3 for now. We can't do much with them right now. Let's focus on the other three outputs.

We have the following outputs
- n1
- (n1 * booo) + n2
- (r * booo) + s

Now since we know n1, let us focus on the second output. 
```
Now, n1*booo must be a multiple of n1
So, n2 = ((n1 * booo) + n2) % n1
```

Now we know n1 and n2.
```
n1 = p * q
n2 = q * r
Now since p, q and r are primes,
gcd(n1, n2) = q
```

Now we know q, `p = n1 / q` and `r = n2 / q`
Now, we can calculate the value of `booo` by substituting values of n1 and n2 in `(n1 * booo) + n2`
Then we can substitute value of r and `booo` into `(r * booo) + s` to get value of s.

Now that we know p, q, r and s, it becomes a simple task to decrypt the ciphertexts

