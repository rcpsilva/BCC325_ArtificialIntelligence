import os
import random
import re
import sys
from copy import deepcopy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    N = len(corpus)
    d = damping_factor
    prob_dist = dict.fromkeys(corpus.keys(), (1-d)/N)
    
    if corpus[page]:
        for link in corpus[page]:
            prob_dist[link] += d/len(corpus[page])
    else:
        for pages in prob_dist:
            prob_dist[page] += d/N


    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    _corpus = deepcopy(corpus)

    for page in _corpus:
        if not _corpus[page]:
            _corpus[page] = _corpus.keys()


    pr = dict.fromkeys(_corpus.keys(), 0)

    #select a random page 
    random_page = random.choice(list(_corpus.keys()))
    for i in range(n):
        
        pr[random_page]+=(1/n)

        prob_dist = transition_model(_corpus,random_page,damping_factor)

        pages = list(prob_dist.keys())
        probs = list(prob_dist.values())

        random_page = random.choices(pages, weights=probs, k=1)[0]

    return pr

def pretty_print_dict(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key) + ':', end=' ')
        if isinstance(value, dict):
            print()
            pretty_print_dict(value, indent + 1)
        else:
            print(value)



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    _corpus = deepcopy(corpus)

    for page in _corpus:
        if not _corpus[page]:
            _corpus[page] = _corpus.keys()

    N = len(_corpus)
    pr = dict.fromkeys(_corpus.keys(), 1/N)
    incoming = {key: set() for key in _corpus.keys()}

    for page in _corpus:
        #print(f'page: {page}')
        for link in _corpus[page]:
            #print(link,end=',')
            incoming[link].add(page)


    change = True
    constant_term  = (1-damping_factor)/N

    while change:
        
        max_diff = 0

        for page in pr:
            
            sum_prs = 0
            
            for page_i in incoming[page]:
                sum_prs += pr[page_i]/len(_corpus[page_i])
                    
            prev = pr[page]
            pr[page] =  constant_term + damping_factor * sum_prs
            
            max_diff = abs(prev-pr[page]) if abs(prev-pr[page]) > max_diff else max_diff
        
        if max_diff < 0.001:
            change = False


    return pr


if __name__ == "__main__":
    main()
