# ReReCaptcha

## Challenge Description

![](./description.png)

## Hint
Rivest, Shamir, and Adleman love this challenge

Downloadable File:
[ReReCaptcha.zip](ReReCaptcha.zip)

## Solution
In the zip file, we have CT (ciphertext), E (public exponent), P and Q (Prime Numbers) in the png images, which is pretty straighforward for RSA. We first convert them to numbers from image to text converter. Then, we use this script from a previous similar CTF challenge to solve. Then, it converts the m (plaintext) to text which is the flag.

## Flag
PCTF{I_H0P3_U_U53D_0CR!}
