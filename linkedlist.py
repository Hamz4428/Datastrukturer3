#LinkedList

#setter data i objekt om til parameter data . setter next i objekt(self ) som skal pekke på neste objekt(self) setter objektet til nulldverdi.
class Node:                             # Class Node
    def __init__(self,data):            # Constructor
        self.data = data               
        self.next = None                
#cclass som er en singellinkedlist           
class SingleLinkedList:  
  #lager en funksjon som har self som parameter funksjonen sier at self har et (hode) og en (halle)hode er først i listen mens hallen er sist. 
    def __init__(self):  
        self.head = None              
        self.tail = None        
    #metode som legger til å lager en nynode i linkedlist, har også if skjekker som skjekker om listen er tom vis listen er tom vil noden som ble lagd på starten være først og siste noden i listen altså hode og hallen ellers vil ny node bli satt til siste node  og siste node sin neste node      
    def addNode(self, data):           
        newNode = Node(data)          
          
        if(self.head == None):       
            self.head = newNode         
            self.tail = newNode     
        else:  
            self.tail.next = newNode   
            self.tail = newNode       
     #viser alle noder på skjermen gjeldene node blir satt til første node(hode)         
    def display(self):                 
        gjeldende = self.head            
        #vis listen er tom skrives det ut, og metoden avsluttes.
        if(self.head == None):        
            print("List is empty")    
            return                     
        #node overskrift skrives ut , og skjer en while loop som skjekker at gjeldende node ikke er None så rkives data til gjeldende node  og vi bytter gjeldende node til å være gjeldende node sin neste. 
        print("Noder i linked list: ") 
        while(gjeldende != None):       
            print(gjeldende.data)       
            gjeldende = gjeldende.next  
 #lager en linkedlist basert på class SingleLinkedList  
minLinkedList = SingleLinkedList()      
#legger til 4 noder med metode addNode          
minLinkedList.addNode(1);              
minLinkedList.addNode(2);               
minLinkedList.addNode(3);                 
minLinkedList.addNode(4);             
#metode som skriver ut all node data
minLinkedList.display();             