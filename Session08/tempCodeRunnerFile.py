import numpy as np

answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answerkey=np.array(answerkey.split(","))
print(answerkey)
""" - Means score.
    - Id of student of the highest score.
    - Id of student of the lowest score."""
    
d=np.loadtxt('answers.txt',delimiter=',', dtype=str)
print(d[:,1:])
print(d[np.argmax(np.sum(d[:,1:]==answerkey,axis=1))])