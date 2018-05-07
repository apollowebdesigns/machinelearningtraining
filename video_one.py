from sklearn import tree
import redis
import pickle

smooth = 1
bumpy = 0
big = 2

apple = 0
orange = 1
banana = 2

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p_features = pickle.dumps([[140, smooth], [130, smooth], [150, bumpy], [170, bumpy], [170, smooth], [180, big]])

r.set('data', p_features)

# using redis to store data and then recall it
features = pickle.loads(r.get('data'))
labels = [apple, apple, orange, orange, banana, banana]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

def predicter(inputData):
    if clf.predict([inputData]) == apple:
        return 'apple'
    elif clf.predict([inputData]) == orange:
        return 'orange'
    else:
        return 'banana'

# print(clf.predict([[160, 0]]))
# print(clf.predict([[170, 0]]))

print(predicter([190, smooth]))