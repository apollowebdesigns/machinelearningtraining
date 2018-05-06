from sklearn import tree
import redis
import pickle

smooth = 1
bumpy = 0

apple = 0
orange = 1

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p_features = pickle.dumps([[140, smooth], [130, smooth], [150, bumpy], [170, bumpy]])

r.set('data', p_features)

# using redis to store data and then recall it
features = pickle.loads(r.get('data'))
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

def predicter(inputData):
    if clf.predict([inputData]) == 0:
        return 'apple'
    else:
        return 'orange'

# print(clf.predict([[160, 0]]))
# print(clf.predict([[170, 0]]))

print(predicter([100, 0]))