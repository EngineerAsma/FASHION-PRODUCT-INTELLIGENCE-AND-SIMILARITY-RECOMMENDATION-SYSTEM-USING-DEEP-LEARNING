import streamlit as st

st.title("Fashion Product Intelligence & Similarity Recommendation System using Deep Learning")

st.header("Project Overview")

st.write("The objective of this project is to build a Fashion Product Intelligence System that:\n"
"1. Converts complex JSON product data into a structured format\n"
"2. Performs detailed Exploratory Data Analysis (EDA)\n"
"3. Identifies trends across gender, season, usage, and color\n"
"4. Selects a single category (Men / Women / Kids)\n"
"5. Download and build the image dataset \n"
"6. Builds a Deep Learning–based similarity recommendation system using product images\n")

st.header("Dataset Description\n")

st.write("2 datasets:\n " \
"1. product metadata dataset\n" \
"2. image mapping dataset\n")

st.header("1. Product metadata dataset\n")

st.markdown(""""File Type: .json\n
Description:\n
Each JSON file represents a single fashion product with detailed metadata, attributes, brand information, pricing, seasonality, and image URLs.\n
""")
st.markdown("""1. id\n
Description:\n
Unique identifier assigned to each product in the catalog\n
Usage:\n
Primary key for product records\n
Used to map JSON metadata with product images\n

2. productDisplayName\n
Description:\n
Display name of the product as shown to customers.\n
Usage:\n
Used for product identification\n
Helps validate recommendation relevance\n

3. brandName\n
Description:\n
Brand associated with the product.\n
Usage:\n
Brand-level analysis\n
Recommendation filtering\n

4. gender\n
Description:\n
Target gender category of the product.\n
Usage:\n
Used to segment the dataset\n
One category is selected for recommendation modeling\n

5. baseColour\n
Description:\n
Primary color of the product.\n
Usage:\n
Used as a visual and descriptive attribute\n
Helps analyze color trends\n

6. usage\n
Description:\n
Intended usage of the product (Casual, Sports, Formal, etc.).\n
Usage:\n
Contextual analysis\n
Improves relevance of recommendations\n

7. season\n
Description:\n
Fashion season for which the product is targeted.\n
Usage:\n
Seasonal trend analysis\n
Supports season-aware filtering\n

8. year\n
Description:\n
Year in which the product was released or cataloged.\n
Usage:\n
Trend analysis across years\n
Helps differentiate older vs newer products\n

9. imageURL\n
Description: \n
URL of the product image.\n
Usage:\n
Used to download images\n
Input for CNN-based feature extraction\n""")

st.header("2. Image Mapping dataset\n")

st.markdown("""File Type: .csv\n
Columns:\n
filename – Image filename\n
link – Public image URL\n
Purpose:\n
Used to download and map product images\n
Acts as an image lookup table\n
""")

st.header("High level architecture of the  project\n")

st.markdown("""2 modules:\n
            1. image  classification system\n
            2. similarity based  product recommendation system\n""")

st.markdown("""
step 1: json ingestion and flattening\n
step 2: data cleaning and preprocessing\n
step 3: EDA\n
step 4: category selection for modelling\n
step 5: image  dataset for preparation\n
step 6: image classification model development\n
step 7: image embedding extraction\n
step 8: similarity computation and recommendation engine   \n      
 """)