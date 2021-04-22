#cmu https://www.cs.cmu.edu/~tcortina/activate/ct/lab8ques.pdf
import math

def cmu():
  #q1
  def sum(x):
    if (x == 1):
      return 1
    else:
      return x + sum(x - 1)
  #q2 makes no sense, skip

  #q3
  def count_digits(n):
    if n < 10:
      return 1
    else:
      return 1 + count_digits(n // 10)
  
  #q4
  def find_max(nums):
    if len(nums) == 2:
      if nums[0] > nums[1]:
        return nums[0]
      else:
        return nums[1]
    else:
      largest = find_max(nums[1:len(nums)])
      if  nums[0] > largest:
        return nums[0]
      else:
        return largest
    

cmu()

#cornell https://www.cs.cornell.edu/courses/cs2110/2014sp/L07-Recursion/recursion_practice.pdf

def cornell():
  #q1 no not again
  #q2 refer to q1 cmu

  #q3
  def multiply(a,b):
    if b == 1:
      return a
    else:
      return a + multiply(a, b - 1)

  #q4 ignore

  #q5 idk

  #q6
  def reverse_sentence(sentence):
    def reverse_string(text):
      if len(text) == 1:
        return text
      elif len(text) == 2:
        return text[1] + text[0]
      else:
        return text[len(text) - 1] + reverse_string(text[1: len(text) - 1]) + text[0]
    return " ".join(map(reverse_string, sentence.split()))
  
  #q7 move on to berkeley and come back
  
  #q8
  
    

cornell()
    
#berkeley 1 https://cs61a.org/lab/lab03/

def berkeley1():
  #q1 refer to type

  #q2
  def pascal(row, column):
    if column == 0 or column == row:
      return 1
    if column < 0 or column > row:
      return 0
    return pascal(row - 1, column) + pascal(row - 1, column - 1)

  #q3
  def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
  
  def repeated(f,n):
    if n == 1:
      return f
    return compose1(f, repeated(f, n - 1))

  

berkeley1()

#berkeley 2 https://cs61a.org/hw/hw03/
class Berkeley2:
  def __init__(self):
    pass
  
  #q1
  def num_eights(self, x):
    if x < 10:
      return 1 if x == 8 else 0
    else:
      return (1 if x % 10 == 8 else 0) + self.num_eights(x // 10)
  
  #2
  def ping_pong(self, x):
    def helper(idx, stored, adder):
      if idx == x:
        return stored
      return helper(
        idx + 1,
        stored + adder,
        -adder if (idx + 1) % 8 == 0 or self.num_eights(idx + 1) >= 1 else adder
      )
    return helper(1, 1, 1)

  #3
  def missing_digits(self, n):
    if n < 10:
      return 0
    def gap(smol, big):
      if smol == big or smol + 1 == big:
        return 0
      return 1 + gap(smol, big - 1)
    return gap(n // 10 % 10, n % 10) + self.missing_digits(n // 10)


  #4
  
  def count_change(self, total):

    def largest_power(m):
      if m == 0:
        return 0
      if math.log(m,2) % 1 == 0:
        return m
      return largest_power(m - 1)

    def count_partitions(n,m):
      if  n == 0:
        return 1
      elif n < 0:
        return 0   
      elif m == 0:
        return 0
      else:
        return count_partitions(n-m, m) + count_partitions(n, largest_power(m - 1))
    return count_partitions(total, largest_power(total))
   

  #5 towers of hanoi

      
  
    
    

def testBerkeley2():
  a = Berkeley2()
  #print(a.num_eights(1808))
  #print(a.ping_pong(23))
  #print(a.missing_digits(12458))
  #print(a.count_change(100))
  
testBerkeley2()
#update your notion to do list after this

#berkeley 3 https://cs61a.org/examprep/examprep03/


#stanford https://web.stanford.edu/class/cs9/lectures/06/Recursion%20Problems.pdf nvm too advanced


#geeks for geeks https://www.geeksforgeeks.org/recursion-practice-problems-solutions/