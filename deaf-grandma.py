


def deaf_grandma():
  gbyes = 0
  msghaslower = False
  while (gbyes < 2):
    msg = input("Say something to Grandma: ")
    for char in msg:
      if char.islower():
        msghaslower = True
    if (msg == "" or msg == " "):
      rant = 'WHAT!'
    elif (msghaslower):
      rant = 'SPEAK UP, KID!'
      msghaslower = False
    elif (msg == 'GOODBYE!'):
      if (gbyes == 0):
        rant = 'LEAVING SO SOON?'
        gbyes = gbyes + 1
      elif (gbyes == 1):
        rant = 'LATER, SKATER!'
        gbyes = gbyes + 1
    elif (msg.isupper()):
      rant = 'NO, NOT SINCE 1946!'
    print(rant)

deaf_grandma()
