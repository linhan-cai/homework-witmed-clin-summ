import numpy as np 
import json 
import faiss

def main():
    generate_chq()
    generate_d2n()
    generate_opi()
    ...


def generate_d2n():
    """
    you are a knowledgeable medical professional. 
summarize the patient/doctor dialogue into an assessment and plan, using the provided examples to guide word choice.

patient/doctor dialogue: [doctor] hi andrea , how are you ? [patient] i'm doing well . how are you ? [doctor] doing well . uh , so i know the nurse told you about dax . i'd like to tell dax a little bit about you . okay ? [patient] okay . [doctor] so , andrea is a 52-year-old female with a past medical history significant for rheumatoid arthritis , atrial fibrillation , and reflux who presents today for her annual exam . so andrea , it's been a year since i saw you . how are you doing ? [patient] i'm doing well . so , i've been walking like you told me to and , um , exercising and doing yoga , and that's actually helped with my arthritis a lot , just the- the constant movement . so , i have n't had any joint pain recently . [doctor] okay . good . so , no- no issues with any stiffness or pain or flare ups over the last year ? [patient] no . [doctor] okay . and i know that we have you on the methotrexate , are you still taking that once a week ? [patient] yes , i am . [doctor] okay . and any issues with that ? [patient] no . [doctor] no . okay . and then in terms of your a-fib , how are you doing with that ? are you having any palpitations ? or , i know that you've kind of been in and out of it over the past , you know , year or so . [patient] yeah . i've still been having palpitations . the- the last one i had was about a week ago . i've noticed that when i start to get stressed , um , they start to flare up again . so , i've been trying meditation , trying running with my dog to try and relieve the stress but it has n't really been working . [doctor] yeah . i- i know that you had called , um , last month and we- we did that event monitor for you , uh , which we'll take a look at in a few minutes . okay ? [patient] okay . [doctor] um , how about um , your reflux ? you know , we had placed you on the protonix , uh , has that helped ? and i know that you were gon na do some dietary modifications . [patient] yeah . i cut out soda and that- that's helped- seemed to help , and the medication's been helping too . i have n't had a flare up in over , i think , five months . [doctor] okay . all right . um , so , you know , i know that you did the review of systems sheet when you checked in and , you know , you had- you know , you endorsed the palpitations and you had some nasal congestion . any other symptoms ? you know , chest pain , shortness of breath , nausea or vomiting ? [patient] no , nothing like that . just the nasal- nasal congestion because of my allergies . [doctor] okay . all right . okay . well , i'd like to go ahead and do a quick physical exam , okay ? [patient] okay . [doctor] all right . hey dragon , show me the vital signs . okay . so , you're in- here in the office today , it looks like , you know , your heart rate's really good today . it's- it's nice and controlled so that's good . um , i'm just gon na take a look into your heart and lungs and- and i'll let you know what i find . okay ? [patient] okay . [doctor] okay . so , on physical examination , um , you know , everything looks really good . on your heart examination , i do appreciate a slight 2/6 systolic- systolic ejection murmur , um , which we've heard in the past so i'm not worried at that . you're in the- a nice regular rate and rhythm at this time . your lungs are nice and clear . on your right elbow , i do notice some edema and some erythema . does it hurt when i press it ? [patient] yeah , it does a bit . [doctor] okay . so , she has pain to palpation of the right elbow . um , and you have no lower extremity edema , okay ? um , so i wan na go ahead and just take a look at some of your results . okay ? [patient] okay . [doctor] hey dragon , show me the event- event monitor results . okay . so , you know , this is the results of your event monitor which shows that , you know , you're in and out of a-fib , you have what we call a conversion pause . you know , you're in a-fib , you pause , and then you go back to regular rhythm . so , we'll talk about that , okay ? [patient] okay . [doctor] hey dragon , show me the autoimmune panel . so , looking here at your autoimmune panel , everything looks good , it looks like you're- you know , everything is well controlled with your rheumatoid arthritis on the methotrexate . okay ? so , let me just go over a little bit about my assessment and my plan for you . okay ? [patient] okay . [doctor] so for your first problem , your rheumatoid arthritis , again , everything looks good . i wan na just continue you on the methotrexate 2.5 mg , once weekly . um , and uh , if you need a referral back to see the rheumatologist , let me know , but i think everything seems stable now . do you need a refill of the methotrexate ? [patient] yes , i do . [doctor] okay . hey dragon , order methotrexate , 2.5 mg once weekly . for your second problem , the atrial fibrillation . so , you're going in and out of a-fib and i'd like to just keep you in normal sinus rhythm . so , i wan na go ahead and refer you to cardiology for a cardiac ablation which just maps out where that rhythm is coming from and burns it so it does n't come back . okay ? you're young , we wan na keep you in a normal rhythm and , being that you're going in and out of a-fib , i think that's what we should do . okay ? [patient] okay . [doctor] hey dragon , order a referral to cardiology . and for your last problem , the reflux , you know , i wanna- i want you to just continue on the protonix , 40 mg a day . continue with your dietary modifications , you know , avoiding coffee and spicy foods , that type of thing . okay ? and then let me know if you have any other issues with that , okay ? [patient] will do . [doctor] any questions ? [patient] no , i do n't . [doctor] okay . all right . it was good to see you . [patient] good seeing you . [doctor] hey dragon , finalize the note .
assessment and plan: xxxx

patient/doctor dialogue: [doctor] hi , brian . how are you ? [patient] hi , good to see you . [doctor] it's good to see you too . so , i know the nurse told you a little bit about dax . [patient] mm-hmm . [doctor] i'd like to tell dax about you , okay ? [patient] sure . [doctor] so , brian is a 58 year old male with a past medical history significant for congestive heart failure and hypertension , who presents today for follow-up of his chronic problems . so , brian , it's been a little while i've seen you . [patient] mm-hmm . [doctor] whats , what's going on ? [patient] i , i just feel out of sorts lately . i do n't know if it's the change in the seasons or if we're just doing a lot of projects around the house and , and some , some construction on our own . i'm just feeling out of it . lack of , uh , energy . i'm just so tired and fatigued , and i feel kinda ... i feel lightheaded every once in a while . [doctor] okay . all right . um , how long has that been going on for ? [patient] uh , probably since labor day , so about five weeks or so . [doctor] okay . and , have you noticed any , like , symptoms of weight gain , like , like swollen legs , or , you know , your belly feels bloated and things like that ? [patient] i feel , i feel bloated every once in a while . [doctor] okay . all right . um , and , are you taking your , your medications ? [patient] uh , yes , i am . [doctor] okay . and , how about your diet ? are you watching your diet ? [patient] uh , it's been a little bit of a struggle . we began construction on our kitchen over labor day weekend , and it was ... hard to cook or prepare meals so we ate out a lot, and not always the best food out. it , it , it kind of reeked havoc , uh , so it's been maybe off a little bit . [doctor] okay . all right . and , how about , you know , other symptoms , like , have you had a fever or chills ? [patient] no . [doctor] okay , and any problems breathing ? do you feel short of breath ? [patient] uh , just when i'm doing doing the projects . again , not even lifting anything really heavy , it's just that if i'm ex- exerting any energy , i , i kinda feel it at that point . [doctor] okay . do you have any chest pain ? [patient] slight cramps . that seems to go away after about , maybe about an hour or so after i first feel it . [doctor] okay , and how about a cough ? [patient] a , a slight cough , and again , i'm not sure if it's just the change of seasons and i'm getting a cold . [doctor] mm-hmm . okay . all right . well , you know , for the most part , how , you know , before all of this- [patient] mm-hmm . [doctor] . how were you doing with your heart failure ? i know that we've kinda talked about you being able to watch your healthy food intake and that's been kind of a struggle in the past . [patient] i , i , i've actually been pretty good about that ever since . the , the , the last year , it's been a little chaotic , but i wanted to make sure i stayed on top of that . [doctor] okay . all right . are you excited for halloween ? [patient] uh , ca n't wait . [doctor] okay . [patient] our home renovations should be complete by then [doctor] all right , yeah , right . [patient] yeah . [doctor] and , so , lastly , for your high blood pressure , how are you doing with that ? have , are , did you buy the blood pressure cuff like i asked ? [patient] yeah , i , i did , and we do mon- , i , i monitor it regularly . my wife makes sure i stay on top of that , but it's been pretty good . [doctor] okay . all right . well , i know you did the review of systems sheet when you checked in , and you were endorsing this fatigue- [patient] mm-hmm . [doctor] . and a little dizziness and we just talked a lot about a lot of other symptoms . [patient] mm-hmm . [doctor] any other symptoms i might be missing ? nausea or vomiting , diarrhea ? [patient] no . [doctor] anything like that ? [patient] no . [doctor] okay . all right . well , i just want to go ahead and do a quick physical exam . [patient] mm-hmm . [doctor] hey , dragon ? show me the vital signs . so , looking at your vital signs here in the office , everything looks good . you know , your blood pressure and your heart rate and your oxygenation all look really good . [patient] mm-hmm . [doctor] so , i'm gon na just take a listen to a few things and check some things out , and i'll let you know what i find , okay ? [patient] perfect . [doctor] okay . so , on your physical examination , you know , i do appreciate some jugular venous distention to- [patient] mm-hmm . [doctor] to about eight centimeters . on your heart exam , i do appreciate a three out of six systolic ejection murmur , which we've heard in the past . and , on your lung exam , i do appreciate some fine crackles at the bases bilaterally , and your lower extremities have , you know , 1+ pitting edema . so , what does all that mean ? that means i think you're retaining a little bit of fluid . [patient] mm-hmm . [doctor] okay ? i wan na just go ahead and look at some of your results , okay ? [patient] sure . [doctor] hey , dragon ? show me the chest x-ray . so , looking here at the results of your chest x-ray , it does look like you have a little bit of fluid in your lungs there , and that can be just from , um , your heart failure , okay ? hey , dragon ? show me the echocardiogram . so , this is the echocardiogram that we did about four months ago , and this shows that the pumping function of your heart is a little bit reduced at 45 % , and it also shows that leaky valve , the mitral regurgitation that , that you have , okay ? um , so , let me just go over and talk about , a little bit , my assessment and my plan for you . [patient] mm-hmm . [doctor] okay ? so , for your first problem , your congestive heart failure , i think you're retaining fluid , and i wan na go ahead and increase your lasix to 80 mg once a day . [patient] mm-hmm . [doctor] i want you to weigh yourself every day . i want you to call me if you're gaining more weight . [patient] mm-hmm . [doctor] and , i certainly want you to call me if you have any other symptoms of shortness of breath , and i wan na go ahead and order another echocardiogram , okay ? [patient] sure . [doctor] hey , dragon ? order an echocardiogram . lastly , for your high blood pressure , it looks like you're managing it well at this time , okay ? so , i wan na go ahead and continue with the lisinopril 20 mg a day . i want you to continue to record your blood pressures at home , and report them to me in the patient portal if you see they're getting elevated , okay ? [patient] mm-hmm . [doctor] does that sound like a plan ? [patient] that sounds fine . [doctor] okay . um , i'm gon na be in touch with you after we get your test results , and we'll go from there , okay ? [patient] sure . [doctor] all right . hey , dragon , finalize the note .
assessment and plan: xxxx

patient/doctor dialogue: [doctor] hi , stephanie . how are you ? [patient] i'm doing okay . how are you ? [doctor] i'm doing okay . um , so i know the nurse talked to you about dax . i'd like to tell dax a little bit about you , okay ? [patient] okay . [doctor] so , stephanie is a 49-year-old female with a past medical history significant for congestive heart failure , kidney stones and prior colonoscopy who presents today for an abnormal lab finding . so , stephanie , i called you in today because your hemoglobin is low . um , how have you been feeling ? [patient] over the past couple of months , i've been really tired and dizzy . lately , i've been really just worn out , even just , you know , walking a mile or going to work , doing things that i've done in the past every day that have been relatively okay , and i have n't gotten tired . and now , i've been getting tired . [doctor] okay , yeah . i , you know , the nurse told me that you had called with these complaints . and i know that we have ordered some labs on you before the visit . and it did , it c- you know , your , your , your hemoglobin is your red blood cell count . and now , and that came back as a little low on the results , okay ? so , have you noticed any blood in your stools ? [patient] uh , no , i have n't . i did about three years ago , um , and i did a colonoscopy for that , but nothing since then . [doctor] okay , yeah . i remember that , okay . and how about , you know , do your stools look dark or tarry or black or anything like that ? [patient] no , nothing like that . [doctor] okay . and have you been , um , having any heavy menstrual bleeding or anything like that ? [patient] no , not that i've noticed . [doctor] okay , all right . and any , have you passed out at all , or anything like that ? any weight loss ? [patient] no , no weight loss or passing out . i have felt a bit dizzy , but it has n't l- led to me passing out at all . [doctor] okay . so , you endorse some dizziness . you endorse some fatigue . have you , but you have n't had any weight loss , loss of appetite , anything like that ? [patient] no , nothing like that . [doctor] okay , all right . so , you know , let's talk a little bit about that colonoscopy . i know you had a colonoscopy about three years ago and that showed that you had some mild diverticuli- diverticulosis . um , no issues since then ? [patient] nope , no issues since then . [doctor] okay , all right . and then i know that , uh , you know , you have this slightly reduced heart function , you know , your congestive heart failure . how have you been doing watching your salt intake ? i know that that's kind of been a struggle for you . [patient] um , it's been more of a struggle recently . i've been traveling a lot . i went up to vermont , um , to go , um , explore the mountains . and along the way i stopped at , you know , mcdonald's and got two cheeseburgers . and so , i , i could be doing better . i've noticed some swelling in my , my legs . um , but nothing too extreme that where i thought i should call . [doctor] okay , all right . and any shortness of breath or problems lying flat at night , anything like that ? [patient] no , nothing like that . [doctor] okay , all right . and then in terms of the kidney stones , i know that you had those a couple years ago , as well . any recent flare ups ? have you had any , any back pain , flank pain , anything like that ? [patient] no , nothing like that . [doctor] okay . any blood in your urine that you've seen ? [patient] no . [doctor] okay , all right . um , okay . well , i know that the nurse did a review of system sheet when you came in . and we've just talked a lot about your , your s- your symptoms , you know , your dizziness , your fatigue and that type of thing . anything else that i might have missed , fever chills , any nasal congestion , sore throat , cough ? [patient] uh , i've had a little bit of nasal congestion just because with the seasons changing , i , i get seasonal allergies . but everything else has been okay . [doctor] okay , all right . well , i'm gon na go ahead and do a quick physical exam , okay ? [patient] okay . [doctor] hey , dragon , show me the vital signs . so , here in the office today , your vital signs look great . your blood pressure is fine . your heart rates r- right where it should be , which is good , okay ? i'm just gon na do a quick exam . and i'll let you know what , what i find , okay ? [patient] okay . [doctor] all right . so , your physical , physical examination looks fine . so , on your heart exam , i do hear a three out of six systolic ejection murmur , which we've heard in the past , okay ? and on your lower extremities , i do notice some trace to one plus pitting edema in your ankles , which is probably from the salt intake , okay ? [patient] mm-hmm . [doctor] so , we'll talk about that . i wan na just look at some of your results , okay ? [patient] okay . [doctor] hey , dragon , show me the echocardiogram . so , i just wanted to go over the results of your last echocardiogram , that was about six months ago . that shows that you do have the low pumping function of , of your heart at about 45 % , which is not terrible . and it does show that you have some moderate mitral regurgitation . so , that's that slight heart murmur i heard in your exam , okay ? hey , dragon , show me the hemoglobin . and here , this is the hemoglobin that i was referring to . it's low at 8.2 , okay ? so , we'll have to talk a little bit about that , all right ? [doctor] so , let me go over a little bit about my assessment and my plan for you , okay ? so , for you first problem this new anemia , uh , i wan na go ahead and send off some more labs and anemia profile , just to see exactly what type of anemia we're dealing with . i also wan na go and refer you back to the gastroenterologist for another evaluation , okay ? hey , dragon , order referral to gastroenterology . so , they're gon na do , uh , probably do an endoscopy and another colonoscopy on you . um , but again , i wan na send off those labs just to make sure that it's not something else , okay ? [patient] okay . [doctor] for your next problem your congestive heart failure , um , i do think you're retaining a little bit of fluid . so , i'm gon na go ahead and start you on some lasix 40 milligrams once a day . i want you to continue you on your toprol 50 milligrams daily . and as well your , as well , as your lisinopril 10 milligrams a day . i really want you to watch your salt intake , okay ? get a scale , weigh yourself every day . and call me if your weight starts to go up , okay ? [patient] okay . [doctor] 'cause i might need to give you more diuretic . [patient] all right . [doctor] and for your last problem your kidney stones , uh , i think everything seems to be fine right at this time . again , continue to watch your diet and stay hydrated . um , and i know that might be a little difficult with the diuretic , but do your best . uh , and give me a call if you have any question , okay ? [patient] okay . [doctor] all right . any questions right now ? [patient] not that i can think of . [doctor] okay , great . hey , dragon , finalize the note .
assessment and plan: xxxxxx

patient/doctor dialogue: [doctor] and why is she here ? annual exam . okay . all right . hi , sarah . how are you ? [patient] good . how are you ? [doctor] i'm good . are you ready to get started ? [patient] yes , i am . [doctor] okay . so sarah is a 27-year-old female here for her annual visit . so , sarah , how have you been since the last time i saw you ? [patient] i've been doing better . um , i've been struggling with my depression , um , a bit more just because we've been trapped really inside and remotely over the past year , so i've been struggling , um , off and on with that . [doctor] okay . uh , and from looking at the notes , it looks like we've had you on , uh , prozac 20 milligrams a day . [patient] yes . [doctor] are , are you taking that ? [patient] i am taking it . i think it's just a lot has been weighing on me lately . [doctor] okay . um , and do you feel like you need an increase in your dose , or do you ... what are you thinking ? do you think that you just need to deal with some stress or you wan na try a , a different , uh , medication or ... [patient] i think the , the medication has helped me in the past , and maybe just increasing the dose might help me through this patch . [doctor] okay . all right . and , and what else has been going on with you ? i know that you've had this chronic back pain that we've been dealing with . how's that , how's that going ? [patient] uh , i've been managing it . it's still , um , here nor there . just , just keeps , um , it really bothers me when i sit for long periods of time at , at my desk at work . so i have ... it helps when i get up and move , but it gets really stiff and it hurts when i sit down for long periods of time . [doctor] okay , and do you get any numbing or tingling down your legs or any pain down leg versus the other ? [patient] a little bit of numbing , but nothing tingling or hurting down my legs . [doctor] okay , and does the , um , do those symptoms improve when you stand up or change position ? [patient] yeah , it does . [doctor] okay . all right . and any weakness in , in your legs ? [patient] no , no weakness , just , just the weird numbing . like , it's , like , almost like it's falling asleep on me . [doctor] okay . and are you able to , um , do your activities of daily living ? do you exercise , go to the store , that type of thing ? [patient] yeah , i am . it bothers me when i'm on my feet for too long and sitting too long , just the extremes of each end . [doctor] okay . and i know that you've had a coronary artery bypass grafting at the young age of 27 , so how's that going ? [patient] yeah , i had con- i had a congenital ... you know , i had a congenital artery when i was a baby , so , um , they had to do a cabg on me , um , fairly young in life , but i've been ... my heart's been doing , doing well , and arteries have been looking good . [doctor] okay . all right , well , let's go ahead and do a quick physical exam . um , so looking at you , you do n't appear in any distress . um , your neck , there's no thyroid enlargement . uh , your heart i hear a three out of six , systolic ejection murmur , uh , that's stable . your lungs otherwise sound clear . your abdomen is soft , and you do have some pain to palpation of your lumbar spine . uh , and you've had decreased flexion of your back . uh , your lower extremity strength is good , and there's no edema . so let's go ahead and look at some of your results . hey , dragon , show me the ecg . okay , so that looks basically unchanged from last year , which is really good . hey , dragon , show me the lumbar spine x-ray . hey , dragon , show me the back x-ray . great . so this looks good . that's also stable from last year . okay . so let's go ahead and , you know , my , my plan for you at this time , you know , from a chronic back pain standpoint , if you need , um , you know , some more physical therapy , and i can refer you to physical therapy to help with those symptoms that are kind of lingering . [patient] mm-hmm . [doctor] um , and we can always give you some pain medication if you , if you get some pain periodically with activity . how do you feel about that ? do you need some pain medication ? [patient] no , i think physical therapy is the right way to , way to start out on this . [doctor] okay . hey , dragon , order physical therapy referral . and then in terms of your depression , we talked about increasing your prozac , so we'll increase it from 20 milligrams to 40 milligrams . it's just one tablet once a day . [patient] okay . [doctor] um , and i'll send those to your pharmacy . does that sound okay ? [patient] that sounds great . [doctor] hey , dragon , order prozac , 40 milligrams , once a day . and then in terms of your ... the heart bypass that you've had ... let's go ahead and just order another echocardiogram for you , and i wan na continue you on the aspirin for now , okay ? [patient] okay . [doctor] hey , dragon , order an echocardiogram . hey , dragon , order aspirin 81 milligrams daily . okay , so the nurse will come in . she'll help you schedule those things , and we'll go from there , okay ? [patient] okay . [doctor] all right , take care . [patient] thank you . [doctor] hey , dragon , finalize the note . 
assessment and plan: xxxxxxx

patient/doctor dialogue: [doctor] hi , cheryl . how are you ? [patient] i'm doing well . how are you ? [doctor] i'm doing well . so i know the nurse told you a little bit about dax . i'd like to tell dax about you . [patient] okay . [doctor] cheryl is a 34-year-old female with a past medical history significant for hypertension , who presents today with back pain . cheryl , what happened to your back ? [patient] so i've been walking a lot lately . i've been walking to ... 30 minutes to an hour or so a day . and all of a sudden , um , when i was walking , my , um , back just kind of seized up on me . and i do n't really know what it was . maybe i was going a little bit faster . but it just all kind of clenched . [doctor] okay . so you felt like , maybe like a spasm or something like that ? [patient] yeah . [doctor] okay . and how many days ago was that ? [patient] that was about six days ago now . [doctor] okay . and what have you taken for the pain ? [patient] i've been taking ibuprofen . um , and then i've been putting some heat on it . but it's still pretty stiff . [doctor] okay . all right . um , and did you have any trauma before that happened ? were you doing anything strenuous like crossfit or lifting boxes or anything like that before you went for , for the walk ? [patient] i have been lifting more , um , probably around three times a week . so i do n't know if it was because i was doing deadlifts that day and then walked . [doctor] okay . [patient] um , maybe i was using my back more than my legs . [doctor] okay . all right . and was it any particular area in your back ? was it the lower back ? [patient] yeah , it was . [doctor] okay . on one side versus the other ? [patient] um , kind of both equally . [doctor] okay . all right . and any numbing or tingling in your legs or your feet ? [patient] no , i have n't felt anything like that . [doctor] okay . any weakness in your lower extremities ? [patient] no . [doctor] okay . all right . and then in terms of your blood pressure , how are you doing ? [patient] so i got that cuff that you suggested the ... our ... the last visit , and i've been doing readings at home . and that's been looking great , too . i've been watching my diet . again , my boyfriend's been great and dieting with me so i do n't have to do it alone . and everything's been good . [doctor] okay . excellent . and you're taking the lisinopril ? [patient] yes . [doctor] okay . wonderful . okay . so i know you did a review of systems sheet with the nurse , and i know you endorse , you know , this back pain . um , do you have any other symptoms ? fever , chills , congestion , cough , chest pain , shortness of breath ? [patient] i have a little bit of nasal congestion , but that's just from my seasonal allergies . [doctor] okay . all right . well , let's go ahead . i want to do a quick physical exam on you . [patient] okay . [doctor] okay ? hey , dragon , show me the vital signs . so good- you know , here in the office , your vital signs look great . your blood pressure's really well controlled , which is good . so that's a good job . so i'm going to take a listen to your heart and lungs . i'm going to examine your back , and i'm going to let you know what i find . okay ? [patient] okay . [doctor] okay . all right . so on physical examination , you know , everything looks good . you know , on your heart exam , i do hear that slight two out of six systolic ejection murmur , but you've had that before . that seems stable to me . on your back exam , you do have some pain to palpation on the right lateral aspect of your lumbar spine , and you do have pain with flexion and extension as well , and you have a negative straight leg raise . so what does that mean ? so we're going to go over that . okay ? let's ... let me look at some of your results , though , first . okay ? [patient] okay . [doctor] we did an x-ray before you saw me , so let's look at that . hey , dragon , show me the back x-ray . so looking here at this x-ray of the lumbar spine , everything looks good . there's good boney alignment . there's no obvious fracture , you know , which is not surprising based on your history . okay ? [patient] hmm . [doctor] hey , dragon , show me the labs . and your labs that we did before you came in all look great . there's no elevated white blood cell count . there's no signs of infection . again , those are all really good . okay ? so let me go over with you about my assessment and my plan for you . so for your first problem , this back pain , i think you have a lumbar strain , and , you know , that might've happened , you know , lifting something or exercising . and so what i want to do is prescribe meloxicam , 15 milligrams once a day . uh , i want you ... you can ice the area , and you can also apply heat sometimes as well . um , you know , i'm going to refer you to physical therapy just to do some strengthening exercises of your back , um , because i do want you to continue to be able to work out and exercise . okay ? [patient] okay . [doctor] and for your last problem , your high blood pressure , again , everything looks great here . um , you know , i think you're doing a really good job with that as well . i want you to continue on the lisinopril , 10 milligrams a day . and then , uh , let me know if you notice any increases in your blood pressure readings . okay ? [patient] okay . [doctor] do you need a refill of the lisinopril ? [patient] yes , i do , actually . [doctor] okay . hey , dragon ? order lisinopril 10 milligrams po daily . okay . uh , so the nurse will be in soon , and she'll get you checked out . okay ? [patient] okay . [doctor] all right . hey , dragon ? finalize the note .
assessment and plan: xxxxxxx
 


Take a deep breath. Let's get started.

patient/doctor dialogue: [doctor] hi , martha . how are you ? [patient] i'm doing okay . how are you ? [doctor] i'm doing okay . so , i know the nurse told you about dax . i'd like to tell dax a little bit about you , okay ? [patient] okay . [doctor] martha is a 50-year-old female with a past medical history significant for congestive heart failure , depression and hypertension who presents for her annual exam . so , martha , it's been a year since i've seen you . how are you doing ? [patient] i'm doing well . i've been traveling a lot recently since things have , have gotten a bit lighter . and i got my , my vaccine , so i feel safer about traveling . i've been doing a lot of hiking . uh , went to washington last weekend to hike in northern cascades, like around the mount baker area . [doctor] nice . that's great . i'm glad to hear that you're staying active , you know . i , i just love this weather . i'm so happy the summer is over . i'm definitely more of a fall person . [patient] yes , fall foliage is the best . [doctor] yeah . um , so tell me , how are you doing with the congestive heart failure ? how are you doing watching your diet ? i know we've talked about watching a low sodium diet . are you doing okay with that ? [patient] i've been doing well with that . i resisted , as much , as i could , from the tater tots , you know , the soft pretzels , the salty foods that i , i love to eat . and i've been doing a really good job . [doctor] okay , all right . well , i'm glad to hear that . and you're taking your medication ? [patient] yes . [doctor] okay , good . and any symptoms like chest pains , shortness of breath , any swelling in your legs ? [patient] no , not that i've noticed . [doctor] okay , all right . and then in terms of your depression , i know that we tried to stay off of medication in the past because you're on medications for your other problems . how are you doing ? and i know that you enrolled into therapy . is that helping ? or- [patient] yeah , it's been helping a lot . i've been going every week , um , for the past year since my last annual exam . and that's been really helpful for me . [doctor] okay . so , no , no issues , no feelings of wanting to harm yourself or hurt others ? [patient] no , nothing like that . [doctor] okay , all right . and then in terms of your high blood pressure , i know that you and i have kind of battled in the past with you remembering to take some of your blood pressure medications . how are you doing with that ? [patient] i'm still forgetting to take my blood pressure medication . and i've noticed when work gets more stressful , my blood pressure goes up . [doctor] okay . and , and so how has work going for you ? [patient] it's been okay . it's been a lot of long hours , late nights . a lot of , um , you know , fiscal year end data that i've been having to pull . so , a lot of responsibility , which is good . but with the responsibility comes the stress . [doctor] yeah , okay , all right . i understand . um , all right . well , i know that you did a review of system sheet when you checked in with the nurse . i know that you were endorsing some nasal congestion from some of the fall pollen and allergies . any other symptoms , nausea or vomiting , abdominal pain , anything like that ? [patient] no , nothing like that . [doctor] no , okay , all right . well , i'm gon na go ahead and do a quick physical exam , okay ? [patient] okay . [doctor] hey , dragon , show me the blood pressure . so , yeah , looking at your blood pressure today here in the office , it is a little elevated . you know , it could just , you could just be nervous . uh , let's look at some of the past readings . hey , dragon , show me the blood pressure readings . hey , dragon , show me the blood pressure readings . here we go . uh , so they are running on the higher side . um , y- you know , i , i do think that , you know , i'd like to see you take your medication a little bit more , so that we can get that under control a little bit better , okay ? [patient] okay . [doctor] so , i'm just gon na check out your heart and your lungs . and you know , let you know what i find , okay ? [patient] okay . [doctor] okay . so , on your physical examination , you know , everything looks good . on your heart exam , i do appreciate a three out of six systolic ejection murmur , which i've heard in the past , okay ? and on your lower extremities , i do appreciate one plus pitting edema , so you do have a little bit of fluid in your legs , okay ? [patient] okay . [doctor] let's go ahead , i wan na look at some of your results , okay ? hey , dragon , show me the echocardiogram . so , this is the result of the echocardiogram that we did last year . it showed that you have that low-ish pumping function of your heart at about 45 % . and it also sh- shows some mitral regurgitation , that's that heart murmur that i heard , okay ? [doctor] um , hey , dragon , show me the lipid panel . so , looking at your lipid panel from last year , you know , everything , your cholesterol was like , a tiny bit high . but it was n't too , too bad , so i know you're trying to watch your diet . so , we'll repeat another one this year , okay ? [patient] okay . [doctor] um , so i wan na just go over a little bit about my assessment and my plan for you , okay ? so , for your first problem your congestive heart failure , um , i wan na continue you on your current medications . but i do wan na increase your lisinopril to 40 milligrams a day , just because your blood pressure's high . and you know , you are retaining a little bit of fluid . i also wan na start you on some lasix , you know , 20 milligrams a day . and have you continue to watch your , your diet , okay ? [patient] okay . [doctor] i also wan na repeat another echocardiogram , okay ? [patient] all right . [doctor] hey , dragon , order an echocardiogram . from a depression standpoint , it sounds like you're doing really well with that . so , i'm , i'm really happy for you . i'm , i'm glad to see that you're in therapy and you're doing really well . i do n't feel the need to start you on any medications this year , unless you feel differently . [patient] no , i feel the same way . [doctor] okay , all right . and then for your last problem your hypertension , you know , again i , i , i think it's out of control . but we'll see , i think , you know , i'd like to see you take the lisinopril as directed , okay ? uh , i want you to record your blood pressures within the patient , you know , take your blood pressure every day . record them to me for like , about a week , so i have to see if we have to add another agent , okay ? 'cause we need to get that under better control for your heart failure to be more successful , okay ? [patient] okay . [doctor] do you have any questions ? , and i forgot . for your annual exam , you're due for a mammogram , so we have to schedule for that , as well , okay ? [patient] okay . [doctor] okay . do you have any questions ? [patient] can i take all my pills at the same time ? [doctor] yeah . [patient] 'cause i've been trying to take them at different times of the day , 'cause i did n't know if it was bad to take them all at once or i should separate them . i do n't know . [doctor] yeah . you can certainly take them , you know , all at the same time , as long , as yeah , they're all one scale . you can take them all at the same time . just set an alarm- [patient] okay . [doctor] . some time during the day to take them , okay ? [patient] that might help me remember better . [doctor] all right . that sounds good . all right , well , it's good to see you . [patient] good seeing you too . [doctor] hey , dragon , finalize the note .
assessment and plan:
    """
    dimension = 1024
    top_k = 3

    # 1. 定义相似索引
    index = faiss.IndexFlatL2(dimension)
    
    # 2. 加载数据集，embedding文件
    source_file, embedding_file = "./dataset/d2n.jsonl", "./dataset/d2n_embedding.jsonl"
    dict_entities = {}
    dict_embedding = {}

    # 3. 添加数据构建索引
    with open(source_file, "r") as fd_source:
        for i, row in enumerate(fd_source):
            dict_entities[i] = json.loads(row)

    embeddings = []
    with open(embedding_file, "r") as fd_embedding:
        for i, row in enumerate(fd_embedding):
            data = np.array(json.loads(row)["embedding"], dtype=np.float32)
            embeddings.append(data)
            dict_embedding[i] = json.loads(row)
        index.add(np.array(embeddings))

    # 4. 召回相似问题
    def _recall(id):
        _result = []
        _search_embedding = dict_embedding[id]["embedding"]
        _, result_ids = index.search(np.array([_search_embedding]), top_k + 1)
        for recall_id in result_ids[0]:
            if id == recall_id:
                continue
            _result.append(dict_entities[recall_id])
        return _result

    prompts = []
    # 5. 构建prompt文件
    for i in range(len(dict_entities)):
        query_entity = dict_entities[i]
        in_context_entites = _recall(i)

        assert len(in_context_entites) == top_k

        PROPMT_CHQ = f"""
you are a knowledgeable medical professional. 
summarize the patient/doctor dialogue into an assessment and plan, using the provided examples to guide word choice.
"""
        for i in range(top_k):
            PROPMT_CHQ += f"""

patient/doctor dialogue: {in_context_entites[i]['inputs']}
assessment and plan: {in_context_entites[i]['target']}
"""

        PROPMT_CHQ += f"""

Take a deep breath. Let's get started.

patient/doctor dialogue: {query_entity['inputs']}
assessment and plan:
"""
        prompts.append(PROPMT_CHQ)
    
    # 6. 输出到文件
    with open("./dataset/d2n_prompt.jsonl", "a+") as fd:
        for i, prompt in enumerate(prompts):
            fd.write(json.dumps({
                "idx": i, 
                "inputs":dict_entities[i]["inputs"], 
                "target":dict_entities[i]["target"], 
                "prompt": prompt}) + "\n")



def generate_chq():
    """
    eg:

    you are a knowledgeable medical professional. 
    summarize the patient health query into one question of 15 words or less, using the provided examples to guide word choice.

    query: I have been diagnosed with bipolar and fibromialgia and have been told I cannot take lyrica with having been put on medication for bipolar as well as the issue with side affects. Is this true?
    summarized question: What drugs should not be taken with lyrica?

    query: SUBJECT: ? MESSAGE: Well the story is I had sex a couple of days after my period but I have been getting sore sides and sore stomach what does these signs mean
    summarized question: What causes abdominal pain after intercourse?

    Take a deep breath. Let's get started.

    query: man, 89, unable to urinate MESSAGE: My husband, 89, has been unable to urinate for 11 hours after his catheter was removed. Is it time to call the doctor?
    summarized question:
    """
    dimension = 1024
    top_k = 20

    # 1. 定义相似索引
    index = faiss.IndexFlatL2(dimension)
    
    # 2. 加载数据集，embedding文件
    source_file, embedding_file = "./dataset/chq.jsonl", "./dataset/chq_embedding.jsonl"
    dict_entities = {}
    dict_embedding = {}

    # 3. 添加数据构建索引
    with open(source_file, "r") as fd_source:
        for i, row in enumerate(fd_source):
            dict_entities[i] = json.loads(row)

    embeddings = []
    with open(embedding_file, "r") as fd_embedding:
        for i, row in enumerate(fd_embedding):
            data = np.array(json.loads(row)["embedding"], dtype=np.float32)
            embeddings.append(data)
            dict_embedding[i] = json.loads(row)
        index.add(np.array(embeddings))

    # 4. 召回相似问题
    def _recall(id):
        _result = []
        _search_embedding = dict_embedding[id]["embedding"]
        _, result_ids = index.search(np.array([_search_embedding]), top_k + 1)
        for recall_id in result_ids[0]:
            if id == recall_id:
                continue
            _result.append(dict_entities[recall_id])
        return _result

    prompts = []
    # 5. 构建prompt文件
    for i in range(len(dict_entities)):
        query_entity = dict_entities[i]
        in_context_entites = _recall(i)

        assert len(in_context_entites) == top_k

        PROPMT_CHQ = f"""
you are a knowledgeable medical professional. 
summarize the patient health query into one question of 15 words or less, using the provided examples to guide word choice.
"""
        for i in range(top_k):
            PROPMT_CHQ += f"""

query: {in_context_entites[i]['inputs']}
summarized question: {in_context_entites[i]['target']}
"""

        PROPMT_CHQ += f"""

Take a deep breath. Let's get started.

query: {query_entity['inputs']}
summarized question:
"""
        prompts.append(PROPMT_CHQ)
    
    # 6. 输出到文件
    with open("./dataset/chq_prompt.jsonl", "a+") as fd:
        for i, prompt in enumerate(prompts):
            fd.write(json.dumps({
                "idx": i, 
                "inputs":dict_entities[i]["inputs"], 
                "target":dict_entities[i]["target"], 
                "prompt": prompt}) + "\n")





def generate_opi():
    """
    eg:
    you are a knowledgeable medical professional. 
    summarize the radiology report findings into an impression with minimal text, using the provided examples to guide word choice.

    finding: The lungs are clear, and without focal airspace opacity. The cardiomediastinal silhouette is normal in size and contour, and stable. There is no pneumothorax or large pleural effusion.
    impression: No acute cardiopulmonary abnormality.

    finding: The lungs are clear, and without focal airspace opacity. The cardiomediastinal silhouette is normal in size and contour, and stable. There is no pneumothorax or large pleural effusion.
    impression: No acute cardiopulmonary abnormality.

    finding: The lungs are clear, and without focal air space opacity. The cardiomediastinal silhouette is normal in size and contour, and stable. There is no pneumothorax large pleural effusion.
    impression: No acute cardiopulmonary abnormality.

    finding: The lungs are clear, and without focal air space opacity. Cardiomediastinal silhouette is normal in size and contour, and stable. There is no pneumothorax or large pleural effusion.
    impression: No acute cardiopulmonary abnormality.

    finding: The lungs are clear, and without focal air space opacity. The cardiomediastinal silhouette is normal in size and contour. There is no pneumothorax or large pleural effusion.
    impression: No acute cardiopulmonary abnormality.

    Take a deep breath. Let's get started.

    finding: The lungs are clear, and without focal air space opacity. The cardiomediastinal silhouette is normal in size and contour, and stable. There is no pneumothorax or large pleural effusion.
    impression:
    """
    dimension = 1024
    top_k = 20

    # 1. 定义相似索引
    index = faiss.IndexFlatL2(dimension)
    
    # 2. 加载数据集，embedding文件
    source_file, embedding_file = "./dataset/opi.jsonl", "./dataset/opi_embedding.jsonl"
    dict_entities = {}
    dict_embedding = {}

    # 3. 添加数据构建索引
    with open(source_file, "r") as fd_source:
        for i, row in enumerate(fd_source):
            dict_entities[i] = json.loads(row)

    embeddings = []
    with open(embedding_file, "r") as fd_embedding:
        for i, row in enumerate(fd_embedding):
            data = np.array(json.loads(row)["embedding"], dtype=np.float32)
            embeddings.append(data)
            dict_embedding[i] = json.loads(row)
        index.add(np.array(embeddings))

    # 4. 召回相似问题
    def _recall(id):
        _result = []
        _search_embedding = dict_embedding[id]["embedding"]
        _, result_ids = index.search(np.array([_search_embedding]), top_k + 1)
        for recall_id in result_ids[0]:
            if id == recall_id:
                continue
            _result.append(dict_entities[recall_id])
        return _result

    prompts = []
    # 5. 构建prompt文件
    for i in range(len(dict_entities)):
        query_entity = dict_entities[i]
        in_context_entites = _recall(i)

        PROPMT_CHQ = f"""
you are a knowledgeable medical professional. 
summarize the radiology report findings into an impression with minimal text, using the provided examples to guide word choice.
"""
        for i in range(top_k):
            PROPMT_CHQ += f"""
finding: {in_context_entites[i]['inputs']}
impression: {in_context_entites[i]['target']}
"""

        PROPMT_CHQ += f"""

Take a deep breath. Let's get started.

finding: {query_entity['inputs']}
impression:
"""
        prompts.append(PROPMT_CHQ)
    
    # 6. 输出到文件
    with open("./dataset/opi_prompt.jsonl", "a+") as fd:
        for i, prompt in enumerate(prompts):
            fd.write(json.dumps({
                "idx": i, 
                "inputs":dict_entities[i]["inputs"], 
                "target":dict_entities[i]["target"], 
                "prompt": prompt}) + "\n")


if __name__ == "__main__":
    main()
