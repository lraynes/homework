
def scrape():
    # coding: utf-8

    # In[27]:


    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    import pandas as pd


    # # NASA Mars News

    # In[3]:


    nasa_url = 'https://mars.nasa.gov/news/'
    html = requests.get(nasa_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup)


    # In[4]:


    title = soup.find_all("div", class_="content_title")[0].text.strip()


    # In[5]:


    paragraph = soup.find_all("div", class_="rollover_description_inner")[0].text.strip()


    # # JPL Images
    # 
    # use soup.find("article", class_="carousel_item") to find the data-link, go to the link, then click the picture

    # In[144]:


    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    html = requests.get(jpl_url)
    soup = BeautifulSoup(html.text, 'html.parser')


    # In[145]:


    featured_article = "https://www.jpl.nasa.gov" + soup.find("article", class_="carousel_item").find("a").attrs["data-link"]
    html = requests.get(featured_article)
    soup = BeautifulSoup(html.text, 'html.parser')


    # In[143]:


    for x in soup.find_all("p"):
        try:
            if x.text[:12] == "Full-Res JPG":
                featured_image_url = x.find("a").attrs["href"]
        except AttributeError as e:
            print(e)
            
    featured_image_url


    # # Mars Weather

    # In[18]:


    weather_url = "https://twitter.com/marswxreport?lang=en"
    html = requests.get(weather_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup)


    # In[22]:


    for tweet in soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        if tweet.text[:3] == "Sol":
            mars_weather = tweet.text
            break


    # # Mars Facts

    # In[23]:


    facts_url = "https://space-facts.com/mars/"
    html = requests.get(facts_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup)


    # In[60]:
    table_scrape = soup.find_all("table", id="tablepress-mars")[0]

    table_dict = []

    for x in table_scrape.find_all("tr"):
        entry = x.text.strip().split(":")
        table_dict.append({
            "Description": entry[0],
            "Value": entry[1]
        })

    table_df = pd.DataFrame(table_dict)
    table_html = table_df.to_html()
    
    # # Mars Hemispheres

    # In[108]:


    hemisphere_urls = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

    hemisphere_image_urls = []

    for url in hemisphere_urls:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        
        img_url = "https://astrogeology.usgs.gov" + soup.find_all("img", class_="wide-image")[0].attrs["src"]
        title = soup.find_all("h2", class_="title")[0].text[:-9]
        
        hemisphere_image_urls.append({
            "title": title,
            "img_url": img_url
        })
    hemisphere_image_urls



    mars = {
        "news_title": title,
        "news_paragraph": paragraph,
        "featured_image": featured_image_url,
        "weather": mars_weather,
        "mars_facts": table_dict,
        "hemispheres": hemisphere_image_urls
    }
   
    return mars