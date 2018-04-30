from sklearn import tree
import redis
import pickle

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p_features = pickle.dumps([[140, 1], [130, 1], [150, 0], [170, 0]])

r.set('data', p_features)

# using redis to store data and then recall it
features = pickle.loads(r.get('data'))
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))