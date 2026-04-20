import streamlit as st

st.title("EXPLORATORY DATA ANALYSIS")

st.subheader("1. product count by gender")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\1.PNG")

st.write("INSIGHTS:\n"
"1. Men dominates other categories with a  variety of 20K+ products \n"
"2. Women category stands second by having nearly 18K products\n" 
"\n")

st.subheader(" 2. gender vs colour distribution ")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\2.PNG")

st.write("INSIGHTS:\n" \
"1. Black is the predominant  color among  men , women and unisex products\n" \
"2. White scores second dominant color for both  the categories.")

st.subheader("3. gender vs article type distribution")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\3.PNG")

st.write("INSIGHTS: \n" \
"1. Under men categroy, TShirts, Shirts and Shoes fill the stock at the largest\n" \
"2. Under Women category, Kurtaas, Tops, Handbags and Heels products fill the stock at the largest")

st.subheader("4. distribution of master category")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\4.PNG")

st.write("INSIGHTS:\n" \
"1. Apparel products such as garments, clothing are high compared to other master categories\n"
"2. The most  important master categories are Apparels, Accessories, Footwear and Personal care")

st.subheader("5. distribution of article type")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\5.PNG")

st.write("INISGHTS: \n" \
"1. The above chart shows the  top 15 article types among all other varieties of products\n" \
"2. This helps us identify the  area of investment and need for quick restocking of several products at the earliest")

st.subheader("6. color  distribution across  categories")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\6.PNG")

st.write("INSIGHTS:\n" \
"1. The above bar plot shows the top 15 colors of all other prodcuts\n" \
"2. This helps us identify people interests, likes and recomend similar products")

st.subheader("7. seasonal product trends")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\7.PNG")

st.write("INSIGHTS:\n" \
"1. The products for Summer season are high compared to other seasons\n" \
"2. While winter products and fall season products are  used moderately ")

st.subheader("8. year analysis")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\8.PNG")

st.write("INSIGHTS: \n" \
"1. The year 2012 should  have the highest selling record as there are more number of products being stocked compared to all other years")

st.subheader("9. brands analysis")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\9.PNG")

st.write("INSIGHTS: The  above graph shows the  top 15  brands chosen by  customers")

st.subheader("10. top brands with respect to gender")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\10.PNG")

st.write("INSIGHTS: Brands across genders\n" \
"1. Mens' category -> ADIDAS, PUMA and NIKE \n" \
"2. Womens' category -> CATWALK and UNITED COLORS OF BENETTON ")

st.subheader("11. price distriibution ")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\11.PNG")

st.write("INSIGHTS:\n" \
"1. The majority of products fall roughly between ₹500–₹3000, indicating a focus on affordable to mid-range fashion items.\n" \
"2. A small number of high-priced outliers (up to ~₹30,000) exist but are rare.")

st.subheader("12. brand vs price distribution")

st.image("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\eda images\\12.PNG")

st.write("INSIGHTS:\n" \
"1. It is clear that Womens' high-selling brands such Catwalk, Fabindia and  United colors of Benetton are of mid - high range yet most of them are affordable\n" \
"2. Mens' popular  brands such as adidas, puma and nike are the costliest brands of all")


st.subheader("EXPLANATION FOR CHOSEN CATEGORY IN THE PROJECT:")

st.markdown(""" 
            ***category*** -> women\n
            ***dataset*** -> medium to large\n
            ***varities*** -> many \n
            ***brands*** -> top brands including fabindia, catwalk, lino presso, united colors of benetton & more\n
            ***analysis level*** - easy to moderate\n
            ***product distribution*** -> almost evenly spread among all article types\n
            """)
