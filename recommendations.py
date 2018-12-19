# A dictionary of movie critics and thheir ratings of a small
# set of movie
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt
# Return a distance based similarity score for person 1 and person 2
def sim_distance(prefs,person1,person2):
 #Get the list of shared_items
 si={}
 for item in prefs[person1]:
  if item in prefs[person2]:
   si[item]=1
 #if they have no ratings in common, return 0
 if len(si)==0: 
  return 0
 #Add up the squares of all the differences
 sum_of_squares=sum(pow(prefs[person1][item]-prefs[person2][item],2) 
                     for item in prefs[person1] if item in prefs[person2])
 return 1/(1+sum_of_squares)
 
 
 
# print (sim_distance(critics,'Lisa Rose','Gene Seymour'))

# *******************19/12/2018****************************
# Return the pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
 # Get the list of mutually rated item
 si={}
 for item in prefs[p1]:
  if item in prefs[p2]:
   si[item]=1
 # Find the number of elements
 n=len(si)
 
 # if they are no rating in common, return 0
 if n==0: return 0
 
 # Add up all the preferences
 sum1=sum(prefs[p1][item] for item in si)
 sum2=sum(prefs[p2][item] for item in si)
 
 # Sum up the squares
 sum1Sq=sum(pow(prefs[p1][item],2) for item in si)
 sum2Sq=sum(pow(prefs[p2][item],2) for item in si)
 
 # Sum up the products
 pSum=sum(prefs[p1][item]*prefs[p2][item] for item in si)
 
 #Caculate Pearson Score
 num=pSum-(sum1*sum2/n)
 den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
 r=num/den
 return r
# print (sim_pearson(critics,'Lisa Rose','Gene Seymour'))


# *****This function will find the best matches for person specified
def topMatches(prefs,person,n=5,similarity=sim_pearson):
 scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
 scores.sort()
 scores.reverse()
 return scores[0:n]
print (topMatches(critics,'Lisa Rose',3,sim_distance))
print (topMatches(critics,'Lisa Rose',3,sim_pearson))