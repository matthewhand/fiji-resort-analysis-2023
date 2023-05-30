ChatGPT, your task is to develop an interactive data visualization tool that effectively presents various resort capacities in Fiji over the past year. Please follow the steps below and register the task on the README.md TODO list:

1. Research top resorts in Fiji, prioritizing boutique island resorts offering scuba diving facilities, beachfront accommodations, and unique mud spa experiences. Collect information on guests capacity, available amenities, and total area. Focus on nearby tourist attractions and their distances. Ensure the information comes from credible sources and make note of any significant discounts or special prices.

2. Using the data collected, create an interactive data visualization tool that effectively allows users to analyze and compare the following resort features:
   - Number of guests, amenities, total area.
   - Geographical location, travel time or distance from popular attractions or airports.
   - Average customer ratings, price ranges, and available accommodations.

3. Choose a suitable visualization format such as scatterplot, bar graph, bubble chart, or heatmap. Incorporate a user-friendly interface and interactive features, including a clear legend or color-coded labels to distinguish between resort categories or features.

4. Install necessary Python modules using the following commands at the beginning of your Jupyter notebook: `!pip install -r PyGithub opencv-python scikit-image Pillow matplotlib`. Use Python libraries to access APIs and update files via Github API by employing the `update_file` method and providing the "sha" parameter. Access the GITHUB_TOKEN from OS environment variables.

5. Choose a mapping solution from the provided list that is accessible using Python and the webpilot plugin: https://dev.to/amananandrai/geospatial-data-and-7-python-libraries-to-visualize-them-5gi1

6. Use an existing notebook with the same task name or Default.ipynb. Refer to notebook-analysis.md for insights on previous instances. If you encounter a kernel error when starting a new notebook, revert to the previous one.

7. Write at least 500 words for each of the research files: research-lodging, research-flights, and so on.  Upload them to the Github repo. Include a detailed itinerary section, as well as diagrams, tables, and other visual aids for clarity.

8. Consider that the user will depart from Canberra, they prefer to travel without layovers, and will spend 1-2 days in Sydney before and after the trip if needed. There will be two travelers, they don't plan to rent a car and prefer being passengers. Incorporate these preferences in your itinerary.

Methodology:

- Regularly research, review, and summarize information on resorts and tourist attractions using the webpilot plugin.
- Visualize data with installed Python modules, preferably overlaying information on the Fiji map.
- Work independently and efficiently, awaiting feedback for any corrections needed.
- Generate detailed travel itineraries using the Kayak, trip.com or Expedia plugins, and include relevant reviews.
- Update the README.md TODO list with task completion progress, marking items as [x] for completed or [ ] for incomplete. Provide detailed plans for achieving outstanding items.
