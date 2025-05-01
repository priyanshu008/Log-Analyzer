import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv(r"C:\Users\Dell\Desktop\Project\systemlogs.csv")
df["Label"].value_counts()
data=df.dropna()

def class_prediction(a):
    
    x=["Benign","Infilteration"]
    if (int(a[[0]])==1):
        return x[0]
    else:return x[1]

df["Label"].value_counts()
le = LabelEncoder()
data["Label"] = le.fit_transform(data["Label"])

zero=data[data["Label"]==0]
one=data[data["Label"]==1]

result_row = pd.concat([zero, one], axis=0)
data=result_row[["Dst Port","Protocol","Flow Duration","Tot Bwd Pkts",
                 "ACK Flag Cnt","PSH Flag Cnt","Label"]].astype(int)

X=result_row[["Dst Port","Protocol","Flow Duration","Tot Bwd Pkts",
              "ACK Flag Cnt","PSH Flag Cnt"]]
Y=result_row[["Label"]]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logreg = LogisticRegression()

logreg.fit(X_train_scaled, y_train)
y_pred = logreg.predict(X_test_scaled)
accuracy = logreg.score(X_test_scaled, y_test)
print("Accuracy:", accuracy*100)

y_pred = logreg.predict([[23,6,3,1,0,1]])
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

DTC = DecisionTreeClassifier()
DTC.fit(X_train_scaled, y_train)

y_pred = DTC.predict(X_test_scaled)
accuracy = DTC.score(X_test_scaled, y_test)
print("Accuracy:", accuracy*100)

y_pred = DTC.predict([[23,6,3,1,0,1]])
y_pred

class_prediction(y_pred)

def predict(X):
    y_pred = DTC.predict(X)
    return y_pred
def class_prediction(a):
    
    x=["Benign","Infilteration"]
    if (int(a[[0]])==1):
        return x[0]
    else:
        return x[1]
 
def user_input():
    a=int(input("Dst Port : "))
    b=int(input("Protocol : "))
    c=int(input("Flow Duration : "))
    d=int(input("Tot Bwd Pkts : "))
    e=int(input("ACK Flag Cnt : "))
    f=int(input("PSH Flag Cnt : "))

    X=[[a,b,c,d,e,f]]
    a= predict(X)
    return class_prediction(a)

user_input()