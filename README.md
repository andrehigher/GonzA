# ProA
An algorithm to predict edges in Knowledge Graphs

## Installing:
>`brew install python`   
`pip install networkx` (if you have installed Python but `pip` is still not in your path, you might need to re-link, like this `brew unlink python && brew link python` or just `sudo easy_install pip`)   
`pip install networkx --user`  

## Running an example
To run ProA you can just run `python main.py` in the root folder and see the logs.

## Real example
After `python main.py` in my terminal, I can see the first line:  
`/m/01d6jf /m/0qjfl /award/hall_of_fame_inductee/hall_of_fame_inductions./award/hall_of_fame_induction/hall_of_fame`,  
indicating that the entities `/m/01d6jf` and `/m/0qjfl` are connected by `/award/hall_of_fame_inductee/hall_of_fame_inductions./award/hall_of_fame_induction/hall_of_fame` relation. ProA removes this relation from the graph and start to calculate the probabilities.  
After several calculations, it will print the final results.
