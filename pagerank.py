import numpy as np

matrice = [
[0, 0, 1, 0],
[1, 0, 1, 1],
[1, 0, 0, 1],
[0, 1, 1, 0]
]

pages = ["A", "B", "C", "D"] 
num_nodes = len(pages)
start_rank = 1 / num_nodes
pageRank_score = [start_rank] * num_nodes

def count_outbounds_links(page):
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
      target_inbounds =[matrice[x][target_index] for x in range(num_nodes)] # x is the line. We go further down to get the whole column of inbounds links to targetted page.
      
      new_rank = 0
      for i in range(len(target_inbounds)):
        if target_inbounds[i] == 1: # searching for links pointing towards target page. 
            neigh = pages[i]
            out_links = count_outbounds_links(neigh)
            neigh_index = pages.index(neigh)
            new_rank += pageRank_score[neigh_index] / out_links
      
      new_scores[target_index] = new_rank
    
    pageRank_score = new_scores
  
  return pageRank_score
  
print("intial Page Rank", pageRank_score)
result = pageRank(pages, pageRank_score, 3)

dictionnary = {pages[i]: result[i] for i in range(num_nodes)}

classement = sorted(dictionnary.items(), key=lambda x: x[1], reverse=True)

# affichage du classement
print("\nClassement PageRank :")
for rank, (page, score) in enumerate(classement, start=1):
    print(f"{rank}. {page}  →  {score}")