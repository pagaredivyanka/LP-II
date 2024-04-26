import pyperclip def main():     
  myMessage = 'Transposition technique'     
  myKey = 10     
  ciphertext = encryptMessage(myKey, myMessage)      
  print("Cipher Text is")     
  print(myMessage)     
  print(ciphertext + '|')     
  pyperclip.copy(ciphertext)  
  def encryptMessage(key, message):     
    ciphertext = [''] * key      
    for col in range(key):         
      position = col          
      while position < len(message):              
        ciphertext[col] += message[position]       
        return ''.join(ciphertext)    
        if __name__ == '__main__':     
          main()

Output :
1) Cipher Text is
Transposition technique
Tiqrouanen stpeocshinti|
