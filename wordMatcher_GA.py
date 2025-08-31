import random
import string

targetWord = input("Enter a word: ").lower()
word_length = len(targetWord)

population = 100
max_gens = 30000

mutation_rate = 0.3
crossover_rate = 0.5

generation = []
selectedSet = []
fitnessScore = 0
generation_number = 0
best_guess = ""
best_score = -1
top_two = ["",""]

def initiation():
    print("Population: " + str(population))
    print("Max no of gens allowed: "+ str(max_gens))
    print("mutation rate: " + str(mutation_rate))
    print("crossover rate: " + str(crossover_rate))
    for c in range(word_length):
        fitness.append(0)
    for _ in range(population):
        letters = [random.choice(string.ascii_lowercase) for _ in range(word_length)]
        curr_guess = ''.join(letters)
        generation.append(curr_guess)
    print("FIRST GEN: " + str(generation))

initiation()

def mutate(population, generation):
    for p in range(population):
            old_word = generation[p]
            letters = []
            for l in range(word_length):
                if random.random() >= mutation_rate:
                    letters.append(old_word[l])
                else:
                    letters.append(random.choice(string.ascii_lowercase))
            generation[p] = ''.join(letters)

def cross(tt):
    split_point = int(round(word_length/2))
    p1 = tt[0]
    p2 = tt[1]

    c1 = p1[:split_point] + p2[split_point:]

    return c1

def runLoop():
    global generation_number
    global generation
    global best_guess
    while best_guess != targetWord and generation_number < max_gens:
        mutate(population, generation)
        calculateFitness()
        generation_number += 1
        #selectedSet.clear()

    
def calculateFitness():
    global best_score
    global best_guess
    global top_two
    global fitnessScore
    for i,ind in enumerate(generation):
        score = 0
        
        for id,c in enumerate(ind):
            if targetWord[id] == c:
                score += 1
        
        if score > best_score:
            
            best_score = score
            best_guess = ind
            if random.random() < crossover_rate:
                for t, tt in enumerate(top_two):
                    if tt != "":
                        top_two[t] = best_guess
                    else:
                        top_two.append(best_guess)
                
                    ind = cross(top_two)
            
            if ind not in selectedSet:
                selectedSet.append(ind)
        fitnessScore = best_score

def printGuess():
    print("CURRENT: " +str(generation))

runLoop()

final_gen = []
for l, lg in enumerate(generation):
    if lg == best_guess:
        final_gen.append("**" + lg.upper() + "**")
    else:
        final_gen.append(lg)

print("LAST GEN: " + str(final_gen))

print("BEST GUESS: " + best_guess)
print("FITNESS: " + str(fitnessScore))
print("Generations taken: " + str(generation_number))

    


        
    

    
