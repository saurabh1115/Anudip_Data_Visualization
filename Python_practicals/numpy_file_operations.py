import numpy as np
score = np.array([1,2,3,4,5,6,7,8,9])
np.save('student_score.npy',score)
loaded_score = np.load('student_score.npy')
print("original scores = ",score)
print("loaded scores = ",loaded_score)