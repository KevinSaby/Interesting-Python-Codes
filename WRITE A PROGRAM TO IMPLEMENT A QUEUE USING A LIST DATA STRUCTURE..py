# WRITE A PROGRAM TO IMPLEMENT A QUEUE USING A LIST DATA STRUCTURE.

# Function to check Queue is empty or not
def isEmpty(qLst):
     if len(qLst)==0:
          return 1
     else:
          return 0


# Function to add  elements in Queue
def Enqueue(qLst,val):
     qLst.append(val)
     if len(qLst)==1:
          front=rear=0
     else:
          rear=len(qLst)-1

# Function to Delete  elements in Queue
def Dqueue(qLst):
     if isEmpty(qLst):
          return "UnderFlow"
     else:
          val = qLst.pop(0)
     if len(qLst)==0:
          front=rear=None
     return val

# Function to Display top element of Queue
def Peek(qLst):
     if isEmpty(qLst):
          return "UnderFlow"
     else:
          front=0
          return qLst[front]

# Function to Display elements of Queue
def Display(qLst):
     if isEmpty(qLst):
          print("No Item to Dispay in Queue....")
     else:
          tp = len(qLst)-1
          print("[FRONT]",end=' ')
          front = 0
          i = front
          rear = len(qLst)-1
          while(i<=rear):
               print(qLst[i],'<-',end=' ')
               i += 1
          print()
          

# Driver function
def main():
     qList = []
     front = rear = 0
     while True:
          print()
          print("##### QUEUE OPERATION #####")
          print("1. ENQUEUE ")
          print("2. DEQUEUE ")
          print("3. PEEK ")
          print("4. DISPLAY ")
          print("5. EXIT ")
          choice = int(input("Enter Your Choice: "))
          if choice == 1:
               ele = int(input("Enter element to insert"))
               Enqueue(qList,ele)
          elif choice == 2:
               val = Dqueue(qList)
               if val == "UnderFlow":
                    print("Queue is Empty")
               else:
                    print("\n Deleted Element was : ",val)

          elif choice==3:
               val = Peek(qList)
               if val == "UnderFlow":
                    print("Queue is Empty")
               else:
                    print("Item at Front: ",val)

          elif choice==4:
               Display(qList)
          elif choice==5:
               print("Bye")
               break

main()
                    








