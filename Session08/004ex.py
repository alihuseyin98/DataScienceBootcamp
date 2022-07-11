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
almean=np.mean(d[: ,1:]==answerkey)
high=d[np.argmax(np.sum(d[:,1:]==answerkey,axis=1))][0]
print("+-++-",high)
low=d[np.argmin(np.sum(d[:,1:]==answerkey))][0]
print(low)
print(d[np.argmin(np.sum(d[:,1:]==answerkey))])
print(np.argmin([1,2,0]))

index_of_highest_score_student=np.argmax(np.sum(d[:,1:]==answerkey, axis=1))
print('Id of student of the highest score:',d[index_of_highest_score_student,0])
#print(d[:,1:]=="A")