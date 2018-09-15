import random 
import sys
import time
import math

k1 = 'EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD'
plaintext1 = 'BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION'
posct1 = 0

k2 =         'VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEXWJLLAETG'
plaintext2 = 'ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTXLAYERTWO'
posct2 = 0

k4 = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
plaintext4 = 'BERLINCLOCK'
posct4 = 63

alph = 'KRYPTOSABCDEFGHIJLMNQUVWXZ'

vig = ['ABCDEFGHIJLMNQUVWXZKRYPTOS',
       'BCDEFGHIJLMNQUVWXZKRYPTOSA',
       'CDEFGHIJLMNQUVWXZKRYPTOSAB',
       'DEFGHIJLMNQUVWXZKRYPTOSABC',
       'EFGHIJLMNQUVWXZKRYPTOSABCD',
       'FGHIJLMNQUVWXZKRYPTOSABCDE',
       'GHIJLMNQUVWXZKRYPTOSABCDEF',
       'HIJLMNQUVWXZKRYPTOSABCDEFG',
       'IJLMNQUVWXZKRYPTOSABCDEFGH',
       'JLMNQUVWXZKRYPTOSABCDEFGHI',
       'LMNQUVWXZKRYPTOSABCDEFGHIJ',
       'MNQUVWXZKRYPTOSABCDEFGHIJL',
       'NQUVWXZKRYPTOSABCDEFGHIJLM',
       'QUVWXZKRYPTOSABCDEFGHIJLMN',
       'UVWXZKRYPTOSABCDEFGHIJLMNQ',
       'VWXZKRYPTOSABCDEFGHIJLMNQU',
       'WXZKRYPTOSABCDEFGHIJLMNQUV',
       'XZKRYPTOSABCDEFGHIJLMNQUVW',
       'ZKRYPTOSABCDEFGHIJLMNQUVWX',
       'KRYPTOSABCDEFGHIJLMNQUVWXZ',
       'RYPTOSABCDEFGHIJLMNQUVWXZK',
       'YPTOSABCDEFGHIJLMNQUVWXZKR',
       'PTOSABCDEFGHIJLMNQUVWXZKRY',
       'TOSABCDEFGHIJLMNQUVWXZKRYP',
       'OSABCDEFGHIJLMNQUVWXZKRYPT',
       'SABCDEFGHIJLMNQUVWXZKRYPTO']

def findRating(segin, segpt):
    totalmatch = 0
    totallen = len(segin)
    for z in range(0, totallen):
        if segin[z] == segpt[z]:
            totalmatch += 1
    return(totalmatch)
        
print("Starting at " + time.strftime('%X %x %Z') + "\n")
    
#Only look at ratings of 8/11 or higher
ratebest = 8
snipbest = ""
wordbest = ""

#for i in range(0, 1):
for i in range(0, 100000):
    
    #scram = k4
    slist = list(k4)
    random.shuffle(slist)
    scram = ''.join(slist)
    
    kout = ""
    posct = posct4
    
    #Do a Vigenère translation based on K1 and K2 on the new random (scram) arrangement
    for j in plaintext4:
        #print(j)
        alphpos = alph.find(j)
        #print(alphpos)
        
        cttry = scram[posct]
        #print(cttry)
        
        knew = ''
        for k in vig:
            vigtry = k[alphpos]
            if vigtry == cttry:
                #print(k)
                knew = k[0]
                break
        #print(knew)
        kout += knew
        posct += 1
    
    #At this point. we have scram and kout
    #print(kout + ' = ' + scram)

    #Test for a match of an English word
    #fin = open('short.txt')
    fin = open('words.txt','r')

    for linein in fin:

        testin = linein
        testin = testin.strip()
        testin = testin.upper()
        #testin = "PALIMPSEST"
        #print(testin)
        
        if len(testin) > 5:
            testline = ""
            testline = testline + testin + testin + testin + testin + testin
            testline = testline + testin + testin + testin + testin + testin
            testline = testline + testin + testin + testin + testin + testin
            #print(testline)
            testseg = testline[posct4:(posct4+len(kout))]
            #print(testseg)
                
            ratenew = findRating(testseg, kout)
            if ratenew >= ratebest:
                #ratebest = ratenew
                snipbest = kout
                wordbest = testin
                print("Rating: " + str(ratenew) + " out of " + str(len(kout)))
                print("Segment: " + snipbest)
                print("Word: " + wordbest)
                print(scram)
                print("")

    fin.close()          
    if ((i % 1000 == 0) and (i > 0)):
        print("Iteration: " + str(i) + " at " + time.strftime('%X %x %Z'))

print("Done at " + time.strftime('%X %x %Z'))
