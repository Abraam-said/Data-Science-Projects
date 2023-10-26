
import joblib
import streamlit as st
import pandas as pd

Model = joblib.load("Model_Final.pkl")
Inputs = joblib.load("Inputs_Final.pkl")

# Dictionary mapping main categories to their corresponding subcategories
main_category_subcategories = {
    'Food': ['Food', 'Community Gardens', 'Drinks', 'Vegan', 'Restaurants', 'Food Trucks', 'Small Batch', 'Farms', 
             'Spaces', 'Cookbooks', 'Bacon', "Farmer's Markets", 'Events'],
    'Publishing': ['Fiction', "Children's Books", 'Poetry', 'Nonfiction', 'Publishing', 'Young Adult', 'Art Books', 'Academic',
       'Periodicals', 'Anthologies', 'Calendars', 'Radio & Podcasts', 'Zines', 'Literary Journals', 'Translations', 'Comedy',
       'Literary Spaces', 'Letterpress'],
    'Theater': ['Plays', 'Musical', 'Festivals', 'Theater', 'Spaces', 'Experimental', 'Immersive', 'Comedy'],
    'Design': ['Product Design', 'Graphic Design', 'Design', 'Architecture', 'Civic Design', 'Typography'
               , 'Interactive Design'],
    'Games': ['Tabletop Games', 'Games', 'Video Games', 'Playing Cards', 'Live Games', 'Mobile Games', 'Puzzles', 
              'Gaming Hardware'],
    'Art': ['Performance Art', 'Digital Art', 'Conceptual Art', 'Illustration', 'Public Art', 'Art', 'Painting', 'Mixed Media', 'Sculpture',
       'Installations', 'Textiles', 'Ceramics', 'Video Art'],
    'Photography': ['Photobooks', 'Photography', 'Fine Art', 'Places', 'Nature', 'People', 'Animals'],
    'Film & Video': ['Festivals', 'Drama', 'Film & Video', 'Documentary', 'Shorts', 'Television', 'Experimental'
                     , 'Thrillers', 'Comedy','Science Fiction', 'Webseries', 'Romance', 'Narrative Film', 'Animation'
                     , 'Horror', 'Action', 'Music Videos', 'Family', 'Fantasy', 'Movie Theaters'],
    'Technology': ['Software', 'Web', 'Technology', 'Makerspaces', 'Gadgets', 'DIY Electronics', 'Hardware', 'Apps', 'Camera Equipment',
       'Space Exploration', 'Robots', 'Fabrication Tools', 'Sound', 'Wearables', '3D Printing', 'Flight'],
    'Fashion': ['Fashion', 'Accessories', 'Jewelry', 'Apparel', 'Ready-to-wear', 'Footwear', 'Couture', 
                'Pet Fashion', 'Childrenswear'],
    'Music': ['Electronic Music', 'Indie Rock', 'Classical Music', 'Music','Rock', 'Hip-Hop', 'World Music', 'Pop', 
              'Country & Folk', 'Jazz', 'Faith', 'Punk', 'Blues', 'R&B', 'Kids', 'Metal', 'Latin', 'Chiptune', 'Comedy'],
    'Comics': ['Graphic Novels', 'Comics', 'Comic Books', 'Anthologies',
       'Webcomics', 'Events'],
    'Dance': ['Spaces', 'Dance', 'Performances', 'Residencies', 'Workshops'],
    'Journalism': ['Journalism', 'Web', 'Print', 'Video', 'Photo', 'Audio'],
    'Crafts': ['Candles', 'DIY', 'Crochet', 'Quilts', 'Crafts', 'Weaving', 'Woodworking', 'Printing', 'Pottery'
               , 'Stationery', 'Knitting', 'Letterpress', 'Embroidery', 'Glass', 'Taxidermy']
}

def prediction(category, main_category, currency, goal, backers, country, project_duration_days, monthly_seasons):
    # Create a test dataframe with the selected inputs
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0, 'category'] = category
    test_df.at[0, 'main_category'] = main_category
    test_df.at[0, 'currency'] = currency
    test_df.at[0, 'goal'] = goal
    test_df.at[0, 'backers'] = backers
    test_df.at[0, 'country'] = country
    test_df.at[0, 'project_duration_days'] = project_duration_days
    test_df.at[0, 'monthly_seasons'] = monthly_seasons
    
    # Predict using the model and return the result
    result = Model.predict(test_df)
    return result[0]

def main():
    # Streamlit UI
    st.title("Kickstarter Project Success Predictor")
    
    # Input fields for user interaction
    main_category = st.selectbox("Select Main Category", options=main_category_subcategories.keys())
    category_options = main_category_subcategories.get(main_category, [])
    category = st.selectbox("Select Project Category", options=category_options)
    currency = st.selectbox("Select Currency", options=['USD', 'GBP', 'CAD', 'AUD', 'EUR', 'SEK', 'MXN', 'NZD', 'SGD', 'CHF', 'DKK', 'HKD', 'NOK'])
    goal = st.number_input("Enter Funding Goal", min_value=10, max_value=34500, value=10, step=10)
    backers = st.number_input("Enter Number of Backers", min_value=0, max_value=157, value=0, step=1)
    country = st.selectbox("Select Country", options=['United States', 'United Kingdom', 'Canada', 'Australia', 'Spain', 'Germany', 'Netherlands', 'Ireland', 'Sweden', 'Italy', 'Mexico', 'Belgium', 'New Zealand', 'France', 'Singapore', 'Austria', 'Switzerland', 'Unknown', 'Denmark', 'Hong Kong', 'Norway', 'Luxembourg'])
    project_duration_days = st.number_input("Enter Project Duration (days)", min_value=0, max_value=91, value=0, step=1)
    monthly_seasons = st.selectbox("Select Monthly Season", options=['Winter', 'Autumn', 'Summer', 'Spring'])

    # Predict button
    if st.button("Predict"):
        result = prediction(category, main_category, currency, goal, backers, country, project_duration_days, monthly_seasons)
        if result == 1:
            st.success("Congratulations! Your project is likely to succeed.")
        else:
            st.error("Sorry, your project is likely to fail.")

if __name__ == '__main__':
    main()
