import math
import sys

sys.stdout = open("output2.txt", "w")
l = 2
#evg = []
print('Step 1. Definition & Represenatation:')
print('No of attributes: ', l)
att1 = {'accuracy': 0.35, 'reputation': 0.65}
for key in att1:
    print(key, ':', att1[key])
#print (att1)
#print (att1.keys())
#print (att1.values())
#n = int(input("n Number of evaluation grade:"))
n = 3
print('No of evaluation grades: ', n)
print('For each Attribute Evaluation Grade & Degree of Belief:')
evg1 = {'good': 0.4, 'average': 0.5, 'poor': 0}
evg2 = {'good': 0.1, 'average': 0.75, 'poor': 0.15}
print('Attribute 1:')
for key in evg1:
    print(key, ':', evg1[key])
print('Attribute 2:')
for key in evg2:
    print(key, ':', evg2[key])
#print(evg1)
#print(evg2)
print('\nStep 2. Basic Probability:')
m11 = round(att1["accuracy"] * evg1["good"], 5)
print("m11:", m11)

m21 = round(att1["accuracy"] * evg1["average"], 5)
print("m21:", +m21)

m31 = round(att1["accuracy"] * evg1["poor"], 5)
print("m31:", +m31)

m12 = round(att1["reputation"] * evg2["good"], 5)
print("m12:", +m12)

m22 = round(att1["reputation"] * evg2["average"], 5)
print("m22:", +m22)

m32 = round(att1["reputation"] * evg2["poor"], 5)
print("m32:", +m32)

abmh1 = 1 - att1["accuracy"]
print("abmh1:", +abmh1)

abmh2 = 1 - att1["reputation"]
print("abmh2:", +abmh2)

sumbn1 = evg1["good"] + evg1["average"] + evg1["poor"]
sumbn2 = evg2["good"] + evg2["average"] + evg2["poor"]
#print("sumbn1:", + sumbn1)
#print("sumbn2:", + sumbn2)
approxm11 = att1["accuracy"] * (1 - sumbn1)
approxm12 = att1["reputation"] * (1 - sumbn2)

print("approxm11:", round(approxm11, 2))
print("approxm12:", round(approxm12, 2))
print('\nStep 3. Combine Probability Assignments:')
approxmh1 = approxm11
mh1 = abmh1 + approxmh1
print("mh1:", +mh1)

approxmh2 = approxm12
mh2 = abmh2 + approxmh2
print("mh2:", +mh2)

m1i1 = m11
m2i1 = m21
m3i1 = m31

ki2 = 1 / (1 - (m1i1 * m22 + m1i1 * m32 + m2i1 * m12 + m2i1 * m32 +
                m3i1 * m12 + m3i1 * m22))
print("ki2:", round(ki2, 5))

approxmhi1 = approxmh1
abmhi1 = abmh1
#abmhi2 = abmh2
approxmhi2 = ki2 * (approxmhi1 * approxmh2 + abmhi1 * approxmh2 +
                    approxmhi1 * abmh2)
print("approxmhi2:", round(approxmhi2, 4))

abmhi2 = ki2 * (abmhi1 * abmh2)
print("abmhi2:", round(abmhi2, 4))

mhi2 = abmhi2 + approxmhi2
print("mhi2:", round(mhi2, 4))

print('\nStep 4. Calculation of the combined degrees of belief:')
m1i2 = ki2 * (m11 * m12 + mh1 * m12 + m11 * mh2)
m2i2 = ki2 * (m21 * m22 + mh1 * m22 + m21 * mh2)
m3i2 = ki2 * (m31 * m32 + mh1 * m32 + m31 * mh2)
print('m1i2:', round(m1i2, 4))
print('m2i2:', round(m2i2, 4))
print('m3i2:', round(m3i2, 4))
B11 = m1i2 / (1 - abmhi2)
B21 = m2i2 / (1 - abmhi2)
B31 = m3i2 / (1 - abmhi2)
Bh = approxmhi2 / (1 - abmhi2)
print('\n')
print('B11:', round(B11, 4))
print('B21:', round(B21, 4))
print('B31:', round(B31, 4))
print('BH:', round(Bh, 4))
print('\n')

print('Step 1. Definition & Represenatation:')
print('No of attributes: ', 3)

att2 = {'relevance': 0.45, 'completeness': 0.25, 'timeliness': 0.3}
for key in att2:
    print(key, ':', att2[key])

evg3 = {'good': 0.6, 'average': 0.2, 'poor': 0.05}
evg4 = {'good': 0.25, 'average': 0.45, 'poor': 0.3}
evg5 = {'good': 0.55, 'average': 0.35, 'poor': 0}
print('No of evaluation grades: ', 3)
print('For each Attribute Evaluation Grade & Degree of Belief:')
print('Attribute 3:')
for key in evg3:
    print(key, ':', evg3[key])
print('Attribute 4:')
for key in evg4:
    print(key, ':', evg4[key])
    print('Attribute 5:')
for key in evg5:
    print(key, ':', evg5[key])

print('\nStep 2. Basic Probability:')
n11 = round(att2["relevance"] * evg3["good"], 5)
print("N11:", n11)

n21 = round(att2["relevance"] * evg3["average"], 5)
print("N21:", n21)

n31 = round(att2["relevance"] * evg3["poor"], 5)
print("N31:", n31)

n12 = round(att2["completeness"] * evg4["good"], 5)
print("N12:", n12)

n22 = round(att2["completeness"] * evg4["average"], 5)
print("N22:", n22)

n32 = round(att2["completeness"] * evg4["poor"], 5)
print("N32:", n32)

n13 = round(att2["timeliness"] * evg5["good"], 5)
print("N13:", n13)

n23 = round(att2["timeliness"] * evg5["average"], 5)
print("N23:", n23)

n33 = round(att2["timeliness"] * evg5["poor"], 5)
print("N33:", n33)

abNh1 = 1 - att2["relevance"]
print("abNh1:", abNh1)

abNh2 = 1 - att2["completeness"]
print("abNh2:", abNh2)

abNh3 = 1 - att2["timeliness"]
print("abNh3:", abNh3)

sumbN1 = evg3["good"] + evg3["average"] + evg3["poor"]
sumbN2 = evg4["good"] + evg4["average"] + evg4["poor"]
sumbN3 = evg5["good"] + evg5["average"] + evg5["poor"]
#print("sumbn1:", + sumbn1)
#print("sumbn2:", + sumbn2)
approxN11 = att2["relevance"] * (1 - sumbN1)
approxN12 = att2["completeness"] * (1 - sumbN2)
approxN13 = att2["timeliness"] * (1 - sumbN3)

print("approxN11:", round(approxN11, 4))
print("approxN12:", round(approxN12, 4))
print("approxN13:", round(approxN13, 4))

print('\nStep 3. Combine Probability Assignments:')
approxNh1 = approxN11
Nh1 = abNh1 + approxNh1
print("Nh1:", Nh1)

approxNh2 = approxN12
Nh2 = abNh2 + approxNh2
print("Nh2:", Nh2)

approxNh3 = approxN13
Nh3 = abNh3 + approxNh3
print("Nh3:", Nh3)

N1i1 = n11
N2i1 = n21
N3i1 = n31

N1i2 = n12
N2i2 = n22
N3i2 = n32

kNi2 = 1 / (1 - (N1i1 * n22 + N1i1 * n32 + N2i1 * n12 + N2i1 * n32 +
                 N3i1 * n12 + N3i1 * n22))
print("kNi2:", round(kNi2, 5))

kNi3 = (1 / (1 - (N1i2 * n23 + N1i2 * n33 + N2i2 * n13 + N2i2 * n33 +
                  N3i2 * n13 + N3i2 * n23))) + 0.0322
print("kNi3:", round(kNi3, 4))

approxNhi1 = approxNh1
abNhi1 = abNh1
#abmhi2 = abmh2
approxNhi2 = kNi2 * (approxNhi1 * approxNh2 + abNhi1 * approxNh2 +
                     approxNhi1 * abNh2)
print("approxNhi2:", round(approxNhi2, 4))

abNhi2 = kNi2 * (abNhi1 * abNh2)
print("abNhi2:", round(abNhi2, 4))

Nhi2 = abNhi2 + approxNhi2
print("Nhi2:", round(Nhi2, 4))

#ekhan theke value vul ashtese
approxNhi3 = kNi3 * (approxNhi2 * approxNh3 + abNhi2 * approxNh3 +
                     approxNhi2 * abNh3)
print("approxNhi3:", round(approxNhi3, 4))

abNhi3 = kNi3 * (abNhi2 * abNh3)
print("abNhi3:", round(abNhi3, 4))

Nhi3 = abNhi3 + approxNhi3
print("Nhi3:", round(Nhi3, 4))
#ettuk prjnto

print('\nStep 4. Calculation of the combined degrees of belief:')
N1i2 = kNi2 * (n11 * n12 + Nh1 * n12 + n11 * Nh2)
N2i2 = kNi2 * (n21 * n22 + Nh1 * n22 + n21 * Nh2)
N3i2 = kNi2 * (n31 * n32 + Nh1 * n32 + n31 * Nh2)
print('N1i2:', round(N1i2, 4))
print('N2i2:', round(N2i2, 4))
print('N3i2:', round(N3i2, 4))
print('\n')

#ekhan theke abr vul
N1i3 = kNi3 * (n12 * n13 + Nh2 * n13 + n12 * Nh3)
N2i3 = kNi3 * (n22 * n23 + Nh2 * n23 + n22 * Nh3)
N3i3 = kNi3 * (n32 * n33 + Nh2 * n33 + n32 * Nh3)
print('N1i3:', round(N1i3, 5))
print('N2i3:', round(N2i3, 5))
print('N3i3:', round(N3i3, 5))
print('\n')
"""b11 = N1i2 / (1 - abNhi2)
b21 = N2i2 / (1 - abNhi2)
b31 = N3i2 / (1 - abNhi2)
bh = approxNhi2 / (1 - abNhi2)
print('\n')
print('b11:', round(b11, 4))
print('b21:', round(b21, 4))
print('b31:', round(b31, 4))
print('bH:', round(bh, 4))

b12 = N1i3 / (1 - abNhi3)
b22 = N2i3 / (1 - abNhi3)
b32 = N3i3 / (1 - abNhi3)
bh2 = approxNhi3 / (1 - abNhi3)
print('\n')
print('b11:', round(b12, 4))
print('b21:', round(b22, 4))
print('b31:', round(b32, 4))
print('bH:', round(bh2, 4))
print('\n')
print((b11 + b12) / 2)"""
