import random 
import sys
import time
import math
import numpy as np
import pylab as plt

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

#Find the number of matches (out of a maximum 11)
def findRating(segin, segpt):
    totalmatch = 0
    totallen = len(segin)
    for z in range(0, totallen):
        if segin[z] == segpt[z]:
            totalmatch += 1
    return(totalmatch)

#Turn k4 into a scrambled string, also return the cyphertext per-scrambled with the eventual BERLINCLOCK letters numbered
#k4
#This is k4  = A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q
#Index in k4 = 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17... 
#scramlist
#Index scram = 88 3 76  9 74 81 27 22 70 61 12 13 23  6  9 14 89...
#scramit (aka scram)
#New scram = J  C  N  I  L  O  T  S  V  Z  L  M  R  F  I  N  Y... 
#Will be cipharray
#Index in BC = [32,66,6,61,19,95,88,2,76,1,74]
#Will be uplower
#k4 with up = A  B c  d  e F  g H  i  j  k  l  m  n  o  p  q  
#Will be fftprep
#fft 0 or 1 = [1, 1, 0, 0, 0, 1, 0, 1...]        sicne 1, 2, 6, and 8 are BERLINCLOCK indicies
def capsct(strk4):
    testnew = strk4
    
    #Create a list from 0 to the length of the input string
    templist = list(range(0, len(testnew)))
    random.shuffle(templist)
    scramit = ""

    for followit in templist:
            scramit += testnew[followit]

    return(scramit,templist)

#Now that we have a match, find the placement of the original ciphertext letters before they with placed together as BERLINCLOCK 
def makefft(k4in, bcarray):

    uplower = k4in
    
    #Find the original 11 indicies of the scrambled BERLINCLOCK cyphertext
    cipharray = bcarray[63:74]

    #Loop through the berlinclock indicies and make those 11 characters uppercase in the ciphertext
    ulout = ""
    fftprep = []
    for ctall in range(0, len(uplower)):
        flagfound = 0
        for loopca in range(0, len(cipharray)):
            
            #If this is character 13 in the ciphertext and [13] was found in the BC array, we have a match!
            if ctall == cipharray[loopca]:
                flagfound = 1
                break
                
        if flagfound == 1:
            ulout += uplower[ctall].upper()
            fftprep += [1]
        else:
            ulout +=  uplower[ctall].lower()
            fftprep += [0]
        
    return(ulout, fftprep)

print("Starting at " + time.strftime('%X %x %Z') + "\n")
    
#Only look at ratings of 8/11 or higher
ratebest = 8
snipbest = ""
wordbest = ""

#for i in range(0, 1):
for i in range(0, 100000):
    
    #scram = k4
    (slist,ctten) = capsct(k4)
    scram = ''.join(slist)
    #print(scram)
    
    kout = ""
    posct = posct4
    groupit = ""
    
    #Do a Vigenère translation based on K1 and K2 on the new random (scram) arrangement
    for j in plaintext4:
        #print("j= " + j)
        alphpos = alph.find(j)
        #print("alphapos= " + str(alphpos))
        
        cttry = scram[posct]
        #print("cttry= " + cttry)
        groupit += cttry
        
        knew = ''
        for k in vig:
            vigtry = k[alphpos]
            if vigtry == cttry:
                #print("k= " + k)
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
        
        if len(testin) > 0:
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

                (lowerout, arrout) = makefft(k4, ctten)
                
                print("Rating: " + str(ratenew) + " out of " + str(len(kout)))
                print(lowerout)
                #print(arrout)
                print("Groupit: " + groupit)
                print("Segment: " + snipbest)
                print("Word: " + wordbest)
                print(scram)
                #print(ctten)
                
                longerarrout = arrout + [0,0,0]
                N = len(longerarrout)
                #print("Len: " + str(N))
                W = np.fft.fft(longerarrout)
                freq = np.fft.fftfreq(N,1)
                absW = abs(W)
                absW[0] = 0
                idx = absW.argmax(axis=0) 
                idxval = (np.amax(absW)+1)
                max_f = abs(freq[idx])
                myest = int(round(1/max_f))
                
                #print("Period estimate: ", myest)
                print("Period estimate: ", (1/max_f))
                print("Strength: ", idxval)
                print("")
                
                plt.subplot(211)
                plt.scatter([max_f,], [np.abs(W[idx]),], s=100,color='r')
                plt.plot(freq[:N/2], abs(W[:N/2]))
                plt.xlabel(r"$f$")

                plt.subplot(212)
                plt.plot(1.0/freq[:N/2], abs(W[:N/2]))
                plt.scatter([1/max_f,], [np.abs(W[idx]),], s=100,color='r')
                plt.xlabel(r"$1/f$")
                plt.xlim(0,20)

                plt.show()
                
    fin.close()          
    if ((i % 1000 == 0) and (i > 0)):
        print("Iteration: " + str(i) + " at " + time.strftime('%X %x %Z'))

print("Done at " + time.strftime('%X %x %Z'))
