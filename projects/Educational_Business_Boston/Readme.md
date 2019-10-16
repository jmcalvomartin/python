I. Description of the problem:

With a population of about 685,094 inhabitants, Boston is a city with many schools distributed in its different neighborhoods.
Boston has an annual population growth of + 1.51% / year, where many of these values are school-age children. Therefore, with this study, we want to focus on the private schools in the Boston neighborhoods and see if they really meet the needs of the city.
From an investment perspective, is it worth opening a new school or not? Are floors more expensive near schools? These are some of the questions that we will try to answer through our analysis.

Ultimately, the target audience for this data problem is:
- Investors who wish to open any type of business related to education.
- Education professionals

II Description of the data:

To address the above problem, we will use multiple Internet sources to extract data with the help of Python packages such as beautifulsoup4 and pandas:
- To obtain a list of all private schools in Bostón, we will use the FourSquare API to extract the list of names along with their geographical location.

- For neighborhood names, location, zip codes, we will use the https://data.boston.gov/dataset/boston-neighborhoods page

. We will map all neighborhoods and colleges together on a folio map.

- For another place, tips related to the information in the FourSquare API. We will try to group all the data of the place in the optimal number of groups and map the results in the upper part of the Folium map already created.

- For any other necessary information, we will search the Internet with the help of the BeautifulSoup4 and Pandas package
