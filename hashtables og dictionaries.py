#liste 
minStack = ["1IMA", "1IMB", "1IMC"]
#legger til strings i listen ved bruk av append
minStack.append("2ITA")
minStack.append("2ITB")
minStack.append("1STA")
minStack.append("1STB")
# listen printes til skjerm så popes(fjernes de to siste verdiene i listen så printes listen på nytt)
print(minStack)
  
minStack.pop()
minStack.pop()
  
print(minStack)
#printer ut hver verdi listen for seg selv ved hjelp av en for loop
for verdi in minStack:
    print(verdi)


#STACK MED DEQUE 
#importerer deque 
from collections import deque

minQueue = deque(["1IMA", "1IMB", "1IMC"])
print(minQueue,"\n")

minQueue.append("2ITA")
minQueue.append("2ITB")

print(minQueue,"\n")

minQueue.pop()
minQueue.pop()

for verdi in minQueue:
    print(verdi)
