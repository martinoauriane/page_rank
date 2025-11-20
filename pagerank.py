import numpy as np

# This matrice represents the numbers of outbound links for any given page.
# we can analyze this matrice through the reading of lines and columns. 
# Each line represents the number of outbound links for a page. 
# Each column represents the number of inbound links for a page. 
#   
matrice = [
    #A  B  C  D
    [0, 0, 1, 0],     #A  Line A analysis: A has one outbound link to page C.
    [1, 0, 1, 1],     #B  Line B analysis: B has one outbound link to A, one outbound link to C, one outbound link to D. 
    [1, 0, 0, 1],     #C  Line C analysis: C has one outbound link to A and one outbound link to D.
    [0, 1, 1, 0]      #D  Line D analysis: D has one outbound link to D, and one outbound link to C. 
]
# Column A analysis: there are two inbound links pointing to A, coming from page B and page C. 
# Column B analysis: there is one inbound link coming from D. 
# Column C analysis: there are three inbound links coming from A, B and D. 
# Column D analysis: there are two inbound links coming from B and C.  

pages = ["A", "B", "C", "D"] 
num_nodes = len(pages)
start_rank = 1 / num_nodes # The initial start rank is the same for all pages/nodes. 
pageRank_score = [start_rank] * num_nodes # Initialize array of page rank scores. This array will we updated multiple times. 

def count_outbounds_links(page): # count the number of outbound links for a page. 
  index = pages.index(page)
  outbounds_potential = matrice[index]
  count = outbounds_potential.count(1)
  return count

def pageRank(pages, pageRank_score, max_iterations):
  for iteration in range(max_iterations):
    new_scores = [0] * num_nodes
    for target_page in pages:  #we calculate the new page rank for all the pages. 
      target_index = pages.index(target_page) #Find the index of target page
      #iterate on all the target neighbors linking to page
      target_inbounds =[matrice[x][target_index] for x in range(num_nodes)] # We create a new array based of all the inbounds link pointing to page n. 

      new_rank = 0
      for i in range(len(target_inbounds)):
        if target_inbounds[i] == 1: # if matrice[line][target_index] is = to 1, it means there's an inbound link. 
            neigh = pages[i]
            out_links = count_outbounds_links(neigh) # we count the number of outbound links for thispage. 
            neigh_index = pages.index(neigh)
            new_rank += pageRank_score[neigh_index] / out_links # we add this inbound link to the new_rank score. 
       
      new_scores[target_index] = new_rank # once we're done iterating, we complete the new_scores array with the new page rank of corresponding page. 
    
    pageRank_score = new_scores # Once we're done iterating on all nodes and calculating a new page rank for each, we assign the pageRank_score a new array. 
  
  return pageRank_score # return the new array after x max_iterations. 
  
print("intial Page Rank", pageRank_score)
result = pageRank(pages, pageRank_score, 3)

dictionnary = {pages[i]: result[i] for i in range(num_nodes)}

classement = sorted(dictionnary.items(), key=lambda x: x[1], reverse=True)

# affichage du classement
print("\nClassement PageRank :")
for rank, (page, score) in enumerate(classement, start=1):
    print(f"{rank}. {page}  →  {score}")