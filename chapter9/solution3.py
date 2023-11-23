# write a program to generate multiplication tables from 2 to 20 and write it to doff files

for i in range(2, 3):
    with open(f"chapter9/Multiplication_table_of_{i}", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j} = {i * j}")
            if j!=10:
                f.write('\n')
                
       
                 