class Node: 
  #function med to paramatere(setter objekt til paramater data)    setter next objekt som skal peke på neste objekt til null, setter prev objekt som skal peke på forrige objekt til null                         
    def __init__(self,data):             
        self.data = data                
        self.next = None              
        self.prev = None              
#setter hode altså første node til null
class DoubleLinkedList:  
    def __init__(self):  
        self.head = None             
      #metode for å legge til nynode først i linked list, lager en ny node og seter pekker fra nynode.next til self.head    
    def addNode(self, data):          
        nyNode = Node(data)         
        nyNode.next = self.head;        
        #skjekker om listen er tom, vis listen er tom blir noden første og siste node i linkedlisten 
        if(self.head != None):     
            self.head.prev = nyNode     
        self.head = nyNode           
        # Lage en ny Node
      # Setter nyNode.next til none
      # Sjekke om listen er tom
      # Hvis listen er tom sett nyNode.prev til None
      # Hvis listen er tom sett self.head(første node) til nyNode 
      # Hvis listen er tom Avslutt
      # Sett last til self.head(første)
      # Så lenge last.next ikke er None
      # last settes til last.next
      # Når last.nest = null sett last next til nuNode
      # Sett nyNode.prev til 

    def appendNode(self, data):        
        nyNode = Node(data)    
        nyNode.next = None     
        if self.head is None:           
           nyNode.prev = None           
           self.head = nyNode        
           return                   
        last = self.head            
        while (last.next is not None):
           last = last.next          
        last.next = nyNode              
        nyNode.prev = last         
        return                          # Avlsutt
      #viser alle noder på skjerm (hvis første node er tom skriv ut at listen er tom og avslutt metode)  
    def display(self, node):        
        if(self.head == None):       
            print("List is empty")     
            return                     

         #node overskrift skrives ut , og skjer en while loop som skjekker at gjeldende node ikke er None så rkives data til gjeldende node  og vi bytter gjeldende node til å være gjeldende node sin neste. 
        print("Noder i linked list: ") 
        while(node != None):           
            print(node.data)            
            last = node            
            node=node.next              
 #lager en linkedlist basert på class SingleLinkedList  
minLinkedList = DoubleLinkedList()    
#legger til noder som sender mer data           
minLinkedList.addNode(1);               
minLinkedList.addNode(2);                
minLinkedList.addNode(3);                
minLinkedList.addNode(4);                
minLinkedList.appendNode(10);             
minLinkedList.appendNode(20);                 
minLinkedList.appendNode(30);                 
minLinkedList.appendNode(40);     
#metode som skriver ut all node data          
minLinkedList.display(minLinkedList.head);  
