from pip import main
import tonyVariables

def greeting():
    print("Hello, I am TonyBot. An automated Coronavirus Bot")
    ggBoolean = True
    confusion = True
    while ggBoolean:
        confusion = True
        answer = input("How may I assist you today?\nInput: ")
        for line in tonyVariables.survey:
            if line in answer.lower():
                surveyBoolean = True
                while surveyBoolean:
                    wantSurvey = input("Are you asking for a COVID 19 Survey?\nInput: ")
                    for line in tonyVariables.yes:
                        if line in wantSurvey.lower():
                            surveyBoolean = False
                            ggBoolean = False
                            confusion = False
                            print("Survey Selected")
                            survey()
                            pass
                        pass
                    pass
                    for line in tonyVariables.no:
                        if line in wantSurvey.lower():
                            surveyBoolean = False
                            confusion = False
                            print("Alright, let's try something else")
                            pass
                    if surveyBoolean:
                        print("Sorry, I didn't quite get that") 
                pass
            pass
        signsBoolean = True
        for line in tonyVariables.signs:
            if line in answer.lower():
                while signsBoolean:
                    wantSigns = input("Are you asking to see a list of symptoms and risk factors?\nInput: ")
                    for line in tonyVariables.yes:
                        if line in wantSigns.lower():
                            signsBoolean = False
                            confusion = False
                            ggBoolean = False
                            print ("Symptoms Selected")
                            symptoms()
                            pass
                        pass
                    for line in tonyVariables.no:
                        if line in wantSigns.lower():
                            signsBoolean = False
                            confusion = False
                            print("Alright, let's try something else")
                            pass
                        pass
                    if signsBoolean:
                        print("Sorry, I couldn't quite catch that")
                        pass
                    pass
                pass
            pass
        for line in tonyVariables.what:
            if line in answer.lower():
                wantBoolean = True
                while wantBoolean:
                    wantWhat = input("Are you asking to see information about Coronavirus?\nInput: ")
                    for line in tonyVariables.yes:
                        if line in wantWhat:
                            wantBoolean = False
                            confusion = False
                            ggBoolean = False
                            print("What Selected")
                            what()
                            pass
                        pass
                    for line in tonyVariables.no:
                        if line in wantWhat:
                            wantBoolean = False
                            confusion = False
                            print("Alright, let's try something else")
                            pass
                        pass
                    if wantBoolean: 
                        print("Sorry, I couldn't quite catch that")
                        pass
                    pass
                pass
            pass
        if confusion:
            print("If you have any other concerns, please don't hesitate to consult with the appropriate government resources")
            pass
        pass
    print("Thank you for choosing TonyBot. We are all facing the same crisis so let us all work together!")
    pass

def what():
    print("Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds. In humans and birds, they cause respiratory tract infections that can range from mild to lethal. Mild illnesses in humans include some cases of the common cold (which is also caused by other viruses, predominantly rhinoviruses), while more lethal varieties can cause SARS, MERS and COVID-19, which is causing the ongoing pandemic. In cows and pigs they cause diarrhea, while in mice they cause hepatitis and encephalomyelitis. Coronaviruses constitute the subfamily Orthocoronavirinae, in the family Coronaviridae, order Nidovirales and realm Riboviria. They are enveloped viruses with a positive-sense single-stranded RNA genome and a nucleocapsid of helical symmetry. The genome size of coronaviruses ranges from approximately 26 to 32 kilobases, one of the largest among RNA viruses. They have characteristic club-shaped spikes that project from their surface, which in electron micrographs create an image reminiscent of the stellar corona, from which their name derives.")

def symptoms():
    print("Coronavirus symptoms include:\nFever or chills\nCough\nShortness of breath or difficulty breathing\nFatigue\nMuscle or body aches\nheadache\nLoss of taste or smell\nSore throat\nCongestion or runny nose\nNausea or vomiting\nDiarrhea\n\nShould you experience any symptoms, it is important to take it easy and treat the symptoms.\n\nWhen to seek medical attention\nTrouble breathing\nPersistent pain or pressure in the chest\nConfusion\nInability to wake or stay awake\nPale, gray, or blue-colored skin, lips, or nail beds, depending on the skin tone\n\nRisk Factors\nOlder age\nLung problems, including asthma\nHeart Disease\nBrain and nervous system conditions\nDiabetes and obesity\nCancer and certain blood disorders\nWeakened immune system\nMental health conditions\nDown syndrome\n\nIf you have any risk factor, you are at a higher risk. It is imperative we remain vigilant against Coronavirus")

def survey():
    print("Welcome to the Coronavirus online survey\n\nThis survey will give you a result based on the answers given")
    ssBoolean = True
    while ssBoolean:
        vaccinated = input("Are you fully vaccinated?\nInput: ")
        fully = False
        for line in tonyVariables.yes:
            if line in vaccinated:
                fully = True
                ssBoolean = False
                pass
            pass
        partial = False
        if not fully:
            partial = input("Are you partially vaccinated?\nInput: ")
            for line in tonyVariables.yes:
                if line in vaccinated:
                    partial = True
                    ssBoolean = False
                    pass
                pass
            pass
        if not fully and not partial:
            ssBoolean = False
            pass
        pass

    experience = input("Have you been experiencing any of symptoms? (Coughing, Fever, Headaches, etc.)\nInput: ")
    hasSymptoms = False
    for line in tonyVariables.yes:
        if line in experience:
            hasSymptoms = True
            ssBoolean = False
            pass
        pass
    
    close = input("Have you been in contact with anyone who has coronavirus or any of its symptoms\nInput: ")
    closeContact = False
    for line in tonyVariables.yes:
        if line in close:
            closeContact = True
            ssBoolean = False
            pass
        pass
    ess = input("Are you an essential worker?\nInput: ")
    essential = False
    for line in tonyVariables.yes:
        if line in ess:
            essential = True
            ssBoolean =False
            pass
        pass
    if fully:
        print("While it is important to stay safe and stay indoors, you should be able to go outside should the need arise") 
        pass
    if partial:
        print("Partial vaccination is a step in the right direction, getting yourself fully vaccinated should be a top priority!")
        pass
    if not fully and not partial:
        print("Unvaccinated whether or choice or circumstance means you MUST stay indoors. This is our duty to protect ourselves and our community")
        pass
    if hasSymptoms:
        print("It is important to take a break sometimes, ask for a day off so you can treat your symptoms properly. Negligence is the enemy!") 
        pass
    if not hasSymptoms:
        print("Great to hear you are very healthy! While it is important to stay safe, it is also important to enjoy yourself even through these trying times") 
        pass
    if closeContact:
        print("Keeping our love ones close, doing what we do for the good of many, there are many reasons to be near the sick. It is also important to never neglect our own safety")
        pass
    if not closeContact:
        pass
    if essential:
        print("Thank you for your service") 
        pass
    if not essential:
        pass

def main():
    greeting()
    pass

main()