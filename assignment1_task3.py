courses = {'python': 1500, 'java': 1000, 'c': 800, 'c++': 1200}

courses_inorder=sorted(courses.items(), key = lambda x : x[1])

print(courses_inorder)
