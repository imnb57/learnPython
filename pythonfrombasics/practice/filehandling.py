a = 'programming'

outputs = [
    a[1:0],         
    a[:-7:],         
    a[-1::],        
    a[1:-5:],       
    a[-8::-2],      
    a[1:-2:-2],      
    a[-6:10:-2],    
    a[::-4],        
    a[1::1],        
    a[-8::2]      
]

with open("demo.txt", "w") as file:
    file.write("For a = 'programming'\n\n")
    file.write("\n".join(outputs) + "\n\n")


a = 'python'

outputs = [
    a[:],
    a[::],
    a[1::],
    a[1:5:],
    a[8::-2],
    a[1:-2:-2],
    a[-6::-2],
    a[::4],
    a[1:0:1],
    a[8::2]
]

with open("demo.txt", "a") as file:
    file.write("For a = 'python'\n\n")
    file.write("\n".join(outputs) + "\n\n")


a = 'python programming'

outputs = [
    a[-1::-2],
    a[:-3:2],
    a[-2::],
    a[8:-5:],
    a[-18::-2],
    a[-1:-2:2],
    a[3:-10:-2],
    a[::4],
    a[1::],
    a[2::2],
    a[-3:],
    a[-2::2],
    a[::],
    a[-6:-5:],
    a[-3::-2]
]

with open("demo.txt", "a") as file:
    file.write("For a = 'python programming'\n\n")
    file.write("\n".join(outputs) + "\n\n")


a = 'pythonprogramming'

outputs = [
    a[::2],
    a[:],
    a[-2:3:-1],
    a[-3:4],
    a[-3:-4:-1],
    a[-3:7:-2],
    a[1:-8],
    a[9:-10],
    a[9:-10:-1],
    a[11::-6],
    a[2:-15:-1],
    a[-15::-2],
    a[7:-1],
    a[-1:0:],
    a[:-1:],
    a[::1],
    a[-1:7],
    a[:-3:],
    a[-1:0],
    a[-1:0:-1],
    a[0:-1]
]

with open("demo.txt", "a") as file:
    file.write("For a = 'pythonprogramming'\n\n")
    file.write("\n".join(outputs) + "\n\n")
