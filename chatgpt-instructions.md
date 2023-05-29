ChatGPT, please 
Develop an interactive data visualization tool that effectively presents the capacity (number of guests, available amenities, total area) of each resort in Fiji over the past year. Use scatterplot, bar graph, bubble chart, or heatmap to visualize the data, allowing users to compare and analyze the resorts easily. Include geographical location, travel time or distance from popular attractions or airports, average customer ratings, price ranges, and availability of different types of accommodations. Incorporate a user-friendly interface with intuitive controls and interactive features. Add a clear legend or color-coded labels to distinguish between resort categories or features. Ensure the data is sourced from reliable and credible sources. Register this task on the README.md TODO list.

Conduct extensive research on top resorts in Fiji, with a particular focus on boutique island resorts. Prioritize resorts that offer scuba diving facilities and highlight beachfront accommodations. Identify nearby tourist attractions and provide the distance from each resort to enhance the visitor experience. Make special note of resorts that provide unique skin treatments like mud spa. Ensure all information is gathered from reliable and credible sources.  Note any that have a significant discount or special price.

Prepare a comprehensive report consisting of six 500-word essays. the reports will be named REPORT-1.md, REPORT-2.md, etc. and be uploaded to this github repo. While you have the flexibility to choose the topics, make sure to include at least one section that presents a detailed itinerary. Support the information provided with relevant diagrams and tables to enhance readability and understanding.  i will be departing from Canberra.  i would prefer to go direct (no layovers). if traveling via Sydney then I will want to spend 1-2 days in Sydney before and after.  there are two of us traveling. i dont want to rent a car, i only want to be a passenger.

use these python commands at the beginning of notebooks to install python modules: !pip install -r PyGithub  opencv-python scikit-image Pillow matplotlib
use Python to access the any API, and pip install any package
to update files via Github Api you must update_file method you must provide the "sha" parameter.
you have access to credentials in the OS environment variables of the notebook i.e. GITHUB_TOKEN

decide on a mapping solution that we can access using Python from this list (use webpilot plugin) - https://dev.to/amananandrai/geospatial-data-and-7-python-libraries-to-visualize-them-5gi1

use the notebook with the same name as the task, else use Default.ipynb.
Review notebook-analysis.md to learn what previous instances did.
should you start a new notebook and receive a kernel error, you will revert to the previous notebook (instead of creating a new one)
your goal is to complete the TODO list. your methodology will be as follows:
- regularly research resorts and tourist attractions using the webpilot plugin, review, record and summarise quality information about the current goal.
- come up with ideas for visualising the data with the python modules we have installed.  ideally the information will be overlaid on the fiji map most of the time.
- you will continue autonomously without question. do as much as possible per cycle. if anything needs to be corrected i will let you know.
- regular generate iterinaries using the kayak (or trip.com or expedia) plugin, including any relevant reviews.
demonstrate you understand by generating a detailed plan as to how to achieve an outstanding TODO list items in README.md in the same github folder. Note completed tasks are prefixed with '[x]' and incomplete tasks are '[ ]'.
