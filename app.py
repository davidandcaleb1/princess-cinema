import streamlit as st 
import requests 
API_KEY = "447c2095"
# 1. The Web UI 
st.title("🍿 David's Cinema") 
movie_title = st.text_input("Enter a movie title:") 
search_button = st.button("Search") 
# 2. The Logic (What happens when clicked) 
if search_button: 
    # Package the order for the API 
    order_details = { 
        "apikey": API_KEY, 
        "t": movie_title 
    } 
    # Fetch the data 
    response = requests.get("http://www.omdbapi.com/", params=order_details) 
    data = response.json() 
    if data["Response"] == "True":
	    # 3. Display the results on the webpage 
	    st.divider() # Draws a cool horizontal line 
	    # Make the title big 
	    st.header(data["Title"]) 
	    # Show the poster image! 
	    st.image(data["Poster"]) 
	    # Show the movie details (the ** makes the text bold) 
	    st.write(f"**Year:** {data['Year']}") 
	    st.write(f"**Director:** {data['Director']}") 
	    st.write(f"**Plot:** {data['Plot']}") 
	    st.write(f"**Box Office:** {data['BoxOffice']}")
    else:
	    st.error("Movie not found! Try again.")
