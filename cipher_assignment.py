import sys
#s is shift
def encrypt_func(s):
  message = input()
  final_result = ""
  main_result = ''
  """ Converting all message to uppercase
  """
  my_message = message.upper()
  
  for each_letter in my_message:
    """
    Discarding all the punctuation marks, digits, blanks, 
    and anything else from the input string.
    """
    if each_letter.isalpha():
      """
      Encoding each letter by shifting s amount
      """
      final_result += chr((ord(each_letter) + s-65) % 26 + 65)
  """Printing the final encoded message 
  in blocks of five letters to the screen
  """  
  final_result = [final_result[i:i+5] for i in range(0, len(final_result), 5)]
  """
  Printing ten blocks of messages per line
  """
  count = 1
  for each_value in final_result:
    if count % 10 == 0:
      main_result += each_value +'\n'
    else:    
      main_result += each_value + ' '
    count += 1    
  return (main_result)

"""
Assignment requirement: type in a message from keyboard
& amount to shift as an input to main method
"""
a = int(sys.argv[1])

print(encrypt_func(a))










  