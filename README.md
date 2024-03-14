# Dataset proposal 

### Spotify related artist
* #### **Description**
    * This dataset got idea from "Fans also like" function in spotify which is a function for let user find artist similar to artist that they're listening to.
    * By using `spotipy` library in python I can gather data about related artist of each artist by passing an spotify ID or spotify link. 
    * I have writen some python code ([Got code idea from this page](https://unboxed-analytics.com/data-technology/visualizing-rap-communities-wtih-python-spotifys-api/)) to collect data by passing spotify artist link as parameter and it will generate csv file in `result` directory, which is `main.py` file in this directory
    * I can choose dept of information by passing integer as other parameter 
      * if 0 in given program will only generate data with first artist and their 20 related
      * if 1 in given program will generate data with first artist and their 20 related but program will continue find related artist of first 20 related artist.
      * dept of dataset will indicate by this number
      * My dataset will use 2 level dept (Because it's take too much time to generate 3 level dept)

* #### **Example dataset**
  * This dataset is generated by using Periphery band as a core artist with dept of 2.
  * All dataset generated will contain 2 file
    * [Link file](result/2_level_Periphery_related.csv) which has this column:
      * _artist_name_ : name of source artist.
      * _artist_id_ : spotify id of source artist.
      * _related_artist_name_ : name of target artist.
      * _related_artist_id_ : spotify of target artist.
      * **This file will act as a detail for each edges.**
    * [detail file](result/2_level_Periphery_detail.csv) 
      * This file will contain each artist detail like their name image url.
      * **This file will act as a detail for each vertex**

* #### **How to run program**
  * In case more example is need this how to run a program
  * Install `spotipy` library `pip install spotipy`
  * Install `pandas` library `pip install pandas`
  * Add API key in [This file](.env)
  * Run program `python main.py {spotify artist link} {dept of data}`
  * For an example `python main.py 'https://open.spotify.com/artist/6d24kC5fxHFOSEAmjQPPhc?si=MzXRZvpIQhqQ47ySKjqQNQ' 0`
  * **More then 2 level dept of data is not recommend, because it take too much time.**



    