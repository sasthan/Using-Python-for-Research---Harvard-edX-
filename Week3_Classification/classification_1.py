import pandas as pd



age={"Time":29, "Jim":31, "Pam":27, "Sam":35}

x = pd.Series(age)

data={'name': ['Tim', 'Jim', 'Pam', 'Same'],
      'age' : [29,31,27,35],
      'ZIP' : ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns = ["name", "age", "ZIP"])

x = pd.Series([6,3,8,6], index=["q","w","e","r"])

y = pd.Series([7,3,5,2], index=["e","q","r","t"])
