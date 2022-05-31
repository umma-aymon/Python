d = {
    'Accuracy': {
        'Good': 0.5,
        'Average': 0.5,
        'Poor': 0
    },
    'Repu': {
        'Good': 0.5,
        'Average': 0.5,
        'Poor': 0
    },
    'Time': {
        'Good': 0.5,
        'Average': 0.5,
        'Poor': 0
    },
    'Comp': {
        'Good': 0.5,
        'Average': 0.5,
        'Poor': 0
    }
}

for i, j in d.items():
    print("\nAttribute: ", i)
    for key in j:
        print(key + ':', j[key])

d2 = {'Accuracy': 0.35, 'Repu': 0.65, 'Time': 1, 'Comp': 2}
#res={}
for i, j in d.items():
    #for x in d2:
    #print("\nAttribute: ", i)
    for k in j:
        print('\n', i, ',', k, '=', d2[i] * j[key])
    #print(key + ':', j[key])
